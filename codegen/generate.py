from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from codegen.parser import OpenAPIParser, Endpoint, Parameter


@dataclass
class TemplateEndpoint:
    path: str
    method: str
    method_name: str
    path_params: list[Parameter]
    required_params: list[Parameter]
    optional_params: list[Parameter]
    query_params: list[Parameter]
    body_params: list[Parameter]
    file_params: list[Parameter]
    is_multipart: bool = False
    response_model: str | None = None


def _repr_value(value):
    if value is None:
        return "None"
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, str):
        return f'"{value}"'
    return str(value)


def _deduplicate_params(params: list[Parameter]) -> list[Parameter]:
    seen: set[str] = set()
    result: list[Parameter] = []
    for p in params:
        if p.python_name not in seen:
            seen.add(p.python_name)
            result.append(p)
    return result


def _check_method_name_collisions(endpoints: list[TemplateEndpoint]) -> list[TemplateEndpoint]:
    name_counts: dict[str, int] = {}
    for ep in endpoints:
        name_counts[ep.method_name] = name_counts.get(ep.method_name, 0) + 1

    name_indices: dict[str, int] = {}
    for ep in endpoints:
        if name_counts[ep.method_name] > 1:
            idx = name_indices.get(ep.method_name, 0)
            name_indices[ep.method_name] = idx + 1
            method_suffix = ep.method.lower()
            ep.method_name = f"{ep.method_name}_{method_suffix}" if idx == 0 else f"{ep.method_name}_{method_suffix}_{idx}"
    return endpoints


def prepare_endpoints(parser: OpenAPIParser) -> list[TemplateEndpoint]:
    template_endpoints: list[TemplateEndpoint] = []

    for ep in parser.endpoints:
        all_params = ep.parameters + ep.request_body_params
        all_params = _deduplicate_params(all_params)

        path_params = [p for p in all_params if p.location == "path"]
        query_params = [p for p in all_params if p.location == "query"]
        body_params = [p for p in all_params if p.location == "body"]
        file_params = [p for p in all_params if p.location == "file"]

        all_non_path = query_params + body_params + file_params
        required_non_path = [p for p in all_non_path if p.required]
        optional_non_path = [p for p in all_non_path if not p.required]

        template_endpoints.append(TemplateEndpoint(
            path=ep.path,
            method=ep.method,
            method_name=ep.method_name,
            path_params=path_params,
            required_params=required_non_path,
            optional_params=optional_non_path,
            query_params=query_params,
            body_params=body_params,
            file_params=file_params,
            is_multipart=ep.is_multipart,
            response_model=ep.response_model,
        ))

    template_endpoints = _check_method_name_collisions(template_endpoints)
    return template_endpoints


def get_base_url(spec: dict) -> str:
    servers = spec.get("servers", [])
    for server in servers:
        url = server.get("url", "")
        if "api." in url:
            return url
    if servers:
        return servers[0].get("url", "")
    return ""


def generate(schema_path: str, output_dir: str, class_name: str) -> None:
    parser = OpenAPIParser(schema_path)
    parser.parse()

    templates_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["repr_value"] = _repr_value

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    base_url = get_base_url(parser.spec)

    template_endpoints = prepare_endpoints(parser)

    # Collect used response models for import
    response_models = sorted({
        ep.response_model for ep in template_endpoints if ep.response_model
    })

    client_template = env.get_template("client.py.j2")
    # Derive module prefix from output dir (e.g. src/lzt_api/forum/ -> lzt_api.forum)
    output_parts = Path(output_dir).parts
    try:
        src_idx = list(output_parts).index("src")
        module_prefix = ".".join(output_parts[src_idx + 1:])
    except ValueError:
        module_prefix = ".".join(output_parts[-2:])
    module_prefix = module_prefix.rstrip(".")

    client_code = client_template.render(
        class_name=class_name,
        endpoints=template_endpoints,
        base_url=base_url,
        response_models=response_models,
        module_prefix=module_prefix,
    )
    (output / "client.py").write_text(client_code, encoding="utf-8")

    models_template = env.get_template("models.py.j2")
    models_code = models_template.render(models=parser.models)
    (output / "models.py").write_text(models_code, encoding="utf-8")

    print(f"Generated {len(template_endpoints)} methods in {class_name}")
    print(f"Generated {len(parser.models)} models")
    print(f"Output: {output}")


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--schema", required=True)
    arg_parser.add_argument("--output", required=True)
    arg_parser.add_argument("--class-name", required=True)
    args = arg_parser.parse_args()
    generate(args.schema, args.output, args.class_name)


if __name__ == "__main__":
    main()
