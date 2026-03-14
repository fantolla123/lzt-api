from __future__ import annotations

import time
import asyncio
from typing import Any

import httpx

from lzt_api.exceptions import LolzAPIError, RateLimitError, AuthError, NotFoundError


_RETRY_STATUSES = {429, 502, 503}
_MAX_RETRIES = 5
_BACKOFF_BASE = 1.0
_BACKOFF_MAX = 60.0


def _handle_error(response: httpx.Response) -> None:
    if response.status_code == 401:
        raise AuthError()
    if response.status_code == 404:
        raise NotFoundError()
    if response.status_code >= 400:
        try:
            body = response.json()
            msg = body.get("error", {}).get("message", response.text)
        except Exception:
            msg = response.text
        raise LolzAPIError(response.status_code, msg)


def _get_retry_delay(response: httpx.Response, attempt: int) -> float:
    retry_after = response.headers.get("Retry-After")
    if retry_after:
        try:
            return float(retry_after)
        except ValueError:
            pass
    delay = min(_BACKOFF_BASE * (2 ** attempt), _BACKOFF_MAX)
    return delay


class BaseClient:
    def __init__(
        self,
        token: str,
        base_url: str = "https://api.zelenka.guru",
        proxy: str | None = None,
        timeout: float = 30.0,
    ):
        self._client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {token}"},
            proxy=proxy,
            timeout=timeout,
        )

    def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        for attempt in range(_MAX_RETRIES):
            response = self._client.request(method, path, **kwargs)
            if response.status_code in _RETRY_STATUSES:
                if attempt == _MAX_RETRIES - 1:
                    if response.status_code == 429:
                        raise RateLimitError()
                    _handle_error(response)
                delay = _get_retry_delay(response, attempt)
                time.sleep(delay)
                continue
            _handle_error(response)
            return response.json()
        return {}

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncBaseClient:
    def __init__(
        self,
        token: str,
        base_url: str = "https://api.zelenka.guru",
        proxy: str | None = None,
        timeout: float = 30.0,
    ):
        self._client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {token}"},
            proxy=proxy,
            timeout=timeout,
        )

    async def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        for attempt in range(_MAX_RETRIES):
            response = await self._client.request(method, path, **kwargs)
            if response.status_code in _RETRY_STATUSES:
                if attempt == _MAX_RETRIES - 1:
                    if response.status_code == 429:
                        raise RateLimitError()
                    _handle_error(response)
                delay = _get_retry_delay(response, attempt)
                await asyncio.sleep(delay)
                continue
            _handle_error(response)
            return response.json()
        return {}

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
