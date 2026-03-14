from __future__ import annotations

import sys
import os
import time

import httpx
import pytest
import respx

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from lzt_api.client import BaseClient, AsyncBaseClient
from lzt_api.exceptions import (
    LolzAPIError,
    RateLimitError,
    AuthError,
    NotFoundError,
)


class TestBaseClient:
    def test_successful_request(self):
        with respx.mock:
            respx.get("https://api.zelenka.guru/test").mock(
                return_value=httpx.Response(200, json={"ok": True})
            )
            client = BaseClient(token="test_token")
            result = client._request("GET", "/test")
            assert result == {"ok": True}
            client.close()

    def test_auth_header(self):
        with respx.mock:
            route = respx.get("https://api.zelenka.guru/test").mock(
                return_value=httpx.Response(200, json={})
            )
            client = BaseClient(token="my_token")
            client._request("GET", "/test")
            assert route.calls[0].request.headers["authorization"] == "Bearer my_token"
            client.close()

    def test_401_raises_auth_error(self):
        with respx.mock:
            respx.get("https://api.zelenka.guru/test").mock(
                return_value=httpx.Response(401, json={})
            )
            client = BaseClient(token="bad")
            with pytest.raises(AuthError):
                client._request("GET", "/test")
            client.close()

    def test_404_raises_not_found(self):
        with respx.mock:
            respx.get("https://api.zelenka.guru/test").mock(
                return_value=httpx.Response(404, json={})
            )
            client = BaseClient(token="t")
            with pytest.raises(NotFoundError):
                client._request("GET", "/test")
            client.close()

    def test_429_retries_then_raises(self):
        with respx.mock:
            respx.get("https://api.zelenka.guru/test").mock(
                return_value=httpx.Response(429, headers={"Retry-After": "0"})
            )
            client = BaseClient(token="t")
            with pytest.raises(RateLimitError):
                client._request("GET", "/test")
            client.close()

    def test_429_retry_success(self):
        with respx.mock:
            route = respx.get("https://api.zelenka.guru/test")
            route.side_effect = [
                httpx.Response(429, headers={"Retry-After": "0"}),
                httpx.Response(200, json={"ok": True}),
            ]
            client = BaseClient(token="t")
            result = client._request("GET", "/test")
            assert result == {"ok": True}
            assert route.call_count == 2
            client.close()

    def test_proxy_setting(self):
        client = BaseClient(token="t", proxy="http://proxy:8080")
        assert client._client._transport is not None
        client.close()

    def test_context_manager(self):
        with BaseClient(token="t") as client:
            assert client is not None


@pytest.mark.asyncio
class TestAsyncBaseClient:
    async def test_successful_request(self):
        async with respx.mock:
            respx.get("https://api.zelenka.guru/test").mock(
                return_value=httpx.Response(200, json={"ok": True})
            )
            client = AsyncBaseClient(token="test_token")
            result = await client._request("GET", "/test")
            assert result == {"ok": True}
            await client.close()

    async def test_context_manager(self):
        async with AsyncBaseClient(token="t") as client:
            assert client is not None


class TestExceptions:
    def test_lolz_api_error(self):
        err = LolzAPIError(500, "internal")
        assert err.status_code == 500
        assert "500" in str(err)

    def test_rate_limit_error(self):
        err = RateLimitError(retry_after=5.0)
        assert err.retry_after == 5.0
        assert err.status_code == 429
