from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Parameter:
    name: str
    python_name: str
    location: str
    required: bool
    type_hint: str
    default: Any = None
    description: str = ""
    enum: list[str] | None = None


@dataclass
class Endpoint:
    path: str
    method: str
    operation_id: str
    method_name: str
    tag: str
    parameters: list[Parameter] = field(default_factory=list)
    request_body_params: list[Parameter] = field(default_factory=list)
    response_model: str | None = None
    description: str = ""


@dataclass
class SchemaField:
    name: str
    python_name: str
    type_hint: str
    required: bool
    default: Any = None


@dataclass
class SchemaModel:
    name: str
    class_name: str
    fields: list[SchemaField] = field(default_factory=list)


def _to_snake_case(name: str) -> str:
    name = name.replace(".", "_")
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"[\-\s]+", "_", name)
    return name.lower()


def _sanitize_python_name(name: str) -> str:
    result = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    result = result.strip("_")
    if result and result[0].isdigit():
        result = f"p_{result}"
    keywords = {"in", "from", "class", "type", "import", "global", "return", "for", "is", "not", "and", "or", "with", "as", "if", "else", "elif", "try", "except", "finally", "while", "break", "continue", "pass", "def", "del", "lambda", "yield", "raise", "assert", "True", "False", "None"}
    if result in keywords:
        result = f"{result}_"
    return result


def _openapi_type_to_python(schema: dict[str, Any]) -> str:
    if not schema:
        return "Any"

    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        return ref_name

    schema_type = schema.get("type")
    if isinstance(schema_type, list):
        schema_type = next((t for t in schema_type if t != "null"), schema_type[0])

    if schema_type == "integer":
        return "int"
    if schema_type == "number":
        return "float"
    if schema_type == "boolean":
        return "bool"
    if schema_type == "string":
        fmt = schema.get("format")
        if fmt == "binary":
            return "bytes"
        return "str"
    if schema_type == "array":
        items = schema.get("items", {})
        item_type = _openapi_type_to_python(items)
        return f"list[{item_type}]"
    if schema_type == "object":
        return "dict[str, Any]"

    any_of = schema.get("anyOf") or schema.get("oneOf")
    if any_of:
        types = [_openapi_type_to_python(s) for s in any_of if s.get("type") != "null"]
        if len(types) == 1:
            return types[0]
        return f"{' | '.join(types)}"

    return "Any"


def _resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any]:
    parts = ref.lstrip("#/").split("/")
    current = spec
    for part in parts:
        current = current[part]
    return current


class OpenAPIParser:
    def __init__(self, spec_path: str | Path):
        with open(spec_path, encoding="utf-8") as f:
            self.spec = json.load(f)
        self.endpoints: list[Endpoint] = []
        self.models: list[SchemaModel] = []

    def parse(self) -> None:
        self._parse_schemas()
        self._parse_paths()

    def _parse_schemas(self) -> None:
        schemas = self.spec.get("components", {}).get("schemas", {})
        for name, schema in schemas.items():
            if schema.get("type") not in ("object", None) and "properties" not in schema:
                continue
            model = SchemaModel(
                name=name,
                class_name=name.replace("-", "_").replace(".", "_"),
            )
            properties = schema.get("properties", {})
            required_fields = set(schema.get("required", []))
            for prop_name, prop_schema in properties.items():
                type_hint = _openapi_type_to_python(prop_schema)
                is_required = prop_name in required_fields
                model.fields.append(SchemaField(
                    name=prop_name,
                    python_name=_sanitize_python_name(prop_name),
                    type_hint=type_hint,
                    required=is_required,
                    default=prop_schema.get("default"),
                ))
            self.models.append(model)

    def _resolve_parameter(self, param: dict[str, Any]) -> dict[str, Any]:
        if "$ref" in param:
            return _resolve_ref(self.spec, param["$ref"])
        return param

    def _parse_paths(self) -> None:
        paths = self.spec.get("paths", {})
        for path, methods in paths.items():
            for method, spec in methods.items():
                if method not in ("get", "post", "put", "delete", "patch"):
                    continue
                operation_id = spec.get("operationId", "")
                if not operation_id:
                    continue

                method_name = _to_snake_case(operation_id)
                tag = spec.get("tags", [""])[0] if spec.get("tags") else ""

                endpoint = Endpoint(
                    path=path,
                    method=method.upper(),
                    operation_id=operation_id,
                    method_name=method_name,
                    tag=tag,
                    description=spec.get("summary", ""),
                )

                for raw_param in spec.get("parameters", []):
                    param = self._resolve_parameter(raw_param)
                    schema = param.get("schema", {})
                    type_hint = _openapi_type_to_python(schema)
                    endpoint.parameters.append(Parameter(
                        name=param["name"],
                        python_name=_sanitize_python_name(param["name"]),
                        location=param.get("in", "query"),
                        required=param.get("required", False),
                        type_hint=type_hint,
                        default=schema.get("default"),
                        description=param.get("description", ""),
                        enum=schema.get("enum"),
                    ))

                request_body = spec.get("requestBody", {})
                if request_body:
                    content = request_body.get("content", {})
                    for content_type, ct_spec in content.items():
                        body_schema = ct_spec.get("schema", {})
                        if "$ref" in body_schema:
                            body_schema = _resolve_ref(self.spec, body_schema["$ref"])
                        properties = body_schema.get("properties", {})
                        required_fields = set(body_schema.get("required", []))
                        for prop_name, prop_schema in properties.items():
                            type_hint = _openapi_type_to_python(prop_schema)
                            endpoint.request_body_params.append(Parameter(
                                name=prop_name,
                                python_name=_sanitize_python_name(prop_name),
                                location="body",
                                required=prop_name in required_fields,
                                type_hint=type_hint,
                                default=prop_schema.get("default"),
                                description=prop_schema.get("description", ""),
                                enum=prop_schema.get("enum"),
                            ))
                        break

                # Extract response model
                responses = spec.get("responses", {})
                success_resp = responses.get("200") or responses.get("201") or responses.get("2XX")
                if success_resp:
                    content = success_resp.get("content", {})
                    for ct, ct_spec in content.items():
                        resp_schema = ct_spec.get("schema", {})
                        if "$ref" in resp_schema:
                            ref_name = resp_schema["$ref"].split("/")[-1]
                            endpoint.response_model = ref_name.replace("-", "_").replace(".", "_")
                        elif resp_schema.get("type") == "object" and resp_schema.get("properties"):
                            # Inline schema — create a model for it
                            model_name = operation_id + "Response"
                            class_name_resp = model_name.replace("-", "_").replace(".", "_")
                            model = SchemaModel(name=model_name, class_name=class_name_resp)
                            properties = resp_schema.get("properties", {})
                            required_fields = set(resp_schema.get("required", []))
                            for prop_name, prop_schema in properties.items():
                                type_hint = _openapi_type_to_python(prop_schema)
                                model.fields.append(SchemaField(
                                    name=prop_name,
                                    python_name=_sanitize_python_name(prop_name),
                                    type_hint=type_hint,
                                    required=prop_name in required_fields,
                                    default=prop_schema.get("default"),
                                ))
                            self.models.append(model)
                            endpoint.response_model = class_name_resp
                        break

                self.endpoints.append(endpoint)
