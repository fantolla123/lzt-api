from __future__ import annotations

import sys
import os

import httpx
import pytest
import respx

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from lzt_api.client import BaseClient, AsyncBaseClient
from lzt_api.exceptions import LolzAPIError, RateLimitError, AuthError, NotFoundError
from lzt_api.forum import ForumClient, AsyncForumClient
from lzt_api.market import MarketClient, AsyncMarketClient

FORUM_URL = "https://prod-api.lolz.live"
MARKET_URL = "https://prod-api.lzt.market"

SYSTEM_INFO = {"visitor_id": 1, "time": 1000}
MARKET_SYSTEM_INFO = {"visitor_id": 1, "time": 1000, "log_id": 1}

THREAD_DATA = {
    "thread_id": 123, "forum_id": 1, "thread_title": "test",
    "thread_view_count": 10, "creator_user_id": 1,
    "creator_username": "user", "creator_username_html": "<b>user</b>",
    "thread_create_date": 1000, "thread_update_date": 2000,
    "user_is_ignored": False, "thread_post_count": 5,
    "thread_is_published": True, "thread_is_deleted": False,
    "thread_is_sticky": False, "thread_is_closed": False,
    "thread_is_followed": False, "thread_is_starred": False,
    "thread_is_open": True, "first_post": {},
    "thread_prefixes": [], "thread_tags": {},
    "links": {}, "permissions": {},
    "node_title": "Forum", "restrictions": {},
    "last_post": {}, "contest": {},
}


class TestBaseClient:
    def test_successful_request(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/test").mock(
                return_value=httpx.Response(200, json={"ok": True})
            )
            client = BaseClient(token="t", base_url=FORUM_URL)
            result = client._request("GET", "/test")
            assert result == {"ok": True}
            client.close()

    def test_auth_header(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/test").mock(
                return_value=httpx.Response(200, json={})
            )
            client = BaseClient(token="my_token", base_url=FORUM_URL)
            client._request("GET", "/test")
            assert route.calls[0].request.headers["authorization"] == "Bearer my_token"
            client.close()

    def test_401_raises_auth_error(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/test").mock(
                return_value=httpx.Response(401, json={})
            )
            client = BaseClient(token="bad", base_url=FORUM_URL)
            with pytest.raises(AuthError):
                client._request("GET", "/test")
            client.close()

    def test_404_raises_not_found(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/test").mock(
                return_value=httpx.Response(404, json={})
            )
            client = BaseClient(token="t", base_url=FORUM_URL)
            with pytest.raises(NotFoundError):
                client._request("GET", "/test")
            client.close()

    def test_429_retries_then_raises(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/test").mock(
                return_value=httpx.Response(429, headers={"Retry-After": "0"})
            )
            client = BaseClient(token="t", base_url=FORUM_URL)
            with pytest.raises(RateLimitError):
                client._request("GET", "/test")
            client.close()

    def test_429_retry_success(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/test")
            route.side_effect = [
                httpx.Response(429, headers={"Retry-After": "0"}),
                httpx.Response(200, json={"ok": True}),
            ]
            client = BaseClient(token="t", base_url=FORUM_URL)
            result = client._request("GET", "/test")
            assert result == {"ok": True}
            assert route.call_count == 2
            client.close()

    def test_502_retries(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/test")
            route.side_effect = [
                httpx.Response(502),
                httpx.Response(200, json={"ok": True}),
            ]
            client = BaseClient(token="t", base_url=FORUM_URL)
            result = client._request("GET", "/test")
            assert result == {"ok": True}
            assert route.call_count == 2
            client.close()

    def test_503_retries(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/test")
            route.side_effect = [
                httpx.Response(503),
                httpx.Response(200, json={"ok": True}),
            ]
            client = BaseClient(token="t", base_url=FORUM_URL)
            result = client._request("GET", "/test")
            assert result == {"ok": True}
            assert route.call_count == 2
            client.close()

    def test_proxy_setting(self):
        client = BaseClient(token="t", base_url=FORUM_URL, proxy="http://proxy:8080")
        assert client._client._transport is not None
        client.close()

    def test_context_manager(self):
        with BaseClient(token="t", base_url=FORUM_URL) as client:
            assert client is not None

    def test_custom_timeout(self):
        client = BaseClient(token="t", base_url=FORUM_URL, timeout=60.0)
        assert client._client.timeout.connect == 60.0
        client.close()

    def test_api_error_message(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/test").mock(
                return_value=httpx.Response(
                    403, json={"error": {"message": "forbidden"}}
                )
            )
            client = BaseClient(token="t", base_url=FORUM_URL)
            with pytest.raises(LolzAPIError) as exc_info:
                client._request("GET", "/test")
            assert exc_info.value.status_code == 403
            assert "forbidden" in str(exc_info.value)
            client.close()


class TestForumClient:
    def test_threads_list(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/threads").mock(
                return_value=httpx.Response(200, json={"threads": []})
            )
            client = ForumClient(token="t")
            result = client.threads_list()
            assert result == {"threads": []}
            client.close()

    def test_threads_list_with_params(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/threads").mock(
                return_value=httpx.Response(200, json={"threads": []})
            )
            client = ForumClient(token="t")
            client.threads_list(forum_id=1, limit=10)
            request = route.calls[0].request
            assert "forum_id" in str(request.url)
            assert "limit" in str(request.url)
            client.close()

    def test_threads_get(self):
        with respx.mock:
            respx.get(f"{FORUM_URL}/threads/123").mock(
                return_value=httpx.Response(200, json={
                    "thread": THREAD_DATA, "system_info": SYSTEM_INFO,
                })
            )
            client = ForumClient(token="t")
            result = client.threads_get(thread_id=123)
            assert result.thread.thread_id == 123
            assert result.thread.thread_title == "test"
            client.close()

    def test_users_get_url(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/users/me").mock(
                return_value=httpx.Response(200, json={
                    "user": {
                        "user_id": 1, "username": "test", "username_html": "test",
                        "user_message_count": 0, "user_register_date": 0,
                        "user_like_count": 0, "user_like2_count": 0,
                        "contest_count": 0, "trophy_count": 0,
                        "short_link": "", "custom_title": "",
                        "is_banned": 0, "display_banner_id": 0,
                        "display_icon_group_id": 0,
                        "balance": "0", "hold": "0", "currency": "rub",
                        "user_email": "t@t.com",
                        "user_unread_notification_count": 0,
                        "user_unread_conversation_count": 0,
                        "conv_welcome_message": "",
                        "user_title": "", "user_deposit": 0,
                        "user_is_valid": True, "user_is_verified": True,
                        "user_is_followed": False, "user_last_seen_date": 0,
                        "links": {}, "permissions": {},
                        "user_is_ignored": False, "user_is_visitor": False,
                        "user_group_id": 1, "curator_titles": [],
                        "user_groups": [], "fields": [],
                        "user_timezone_offset": 0,
                        "user_external_authentications": [],
                        "self_permissions": {}, "edit_permissions": {},
                        "birthday": {}, "secret_answer_rendered": "",
                        "secret_answer_first_letter": "",
                        "user_following": {}, "user_followers": {},
                        "banner": "",
                    },
                    "system_info": SYSTEM_INFO,
                })
            )
            client = ForumClient(token="t")
            result = client.users_get(user_id="me")
            assert route.called
            assert result.user.username == "test"
            client.close()

    def test_path_param_substitution(self):
        with respx.mock:
            route = respx.get(f"{FORUM_URL}/threads/456").mock(
                return_value=httpx.Response(200, json={
                    "thread": THREAD_DATA, "system_info": SYSTEM_INFO,
                })
            )
            client = ForumClient(token="t")
            client.threads_get(thread_id=456)
            assert route.called
            client.close()


class TestMarketClient:
    def test_category_list(self):
        with respx.mock:
            respx.get(f"{MARKET_URL}/category").mock(
                return_value=httpx.Response(200, json={
                    "category": {}, "system_info": MARKET_SYSTEM_INFO,
                })
            )
            client = MarketClient(token="t")
            result = client.category_list()
            assert result is not None
            client.close()

    def test_custom_base_url(self):
        custom = "https://custom-api.example.com"
        with respx.mock:
            respx.get(f"{custom}/category").mock(
                return_value=httpx.Response(200, json={
                    "category": {}, "system_info": MARKET_SYSTEM_INFO,
                })
            )
            client = MarketClient(token="t", base_url=custom)
            result = client.category_list()
            assert result is not None
            client.close()


@pytest.mark.asyncio
class TestAsyncForumClient:
    async def test_successful_request(self):
        async with respx.mock:
            respx.get(f"{FORUM_URL}/threads").mock(
                return_value=httpx.Response(200, json={"threads": []})
            )
            async with AsyncForumClient(token="t") as client:
                result = await client.threads_list()
                assert result is not None

    async def test_context_manager(self):
        async with AsyncForumClient(token="t") as client:
            assert client is not None


@pytest.mark.asyncio
class TestAsyncMarketClient:
    async def test_successful_request(self):
        async with respx.mock:
            respx.get(f"{MARKET_URL}/category").mock(
                return_value=httpx.Response(200, json={
                    "category": {}, "system_info": MARKET_SYSTEM_INFO,
                })
            )
            async with AsyncMarketClient(token="t") as client:
                result = await client.category_list()
                assert result is not None


class TestModels:
    def test_forum_response_model(self):
        from lzt_api.forum.models import Threads_GetResponse
        data = {"thread": THREAD_DATA, "system_info": SYSTEM_INFO}
        model = Threads_GetResponse.model_validate(data)
        assert model.thread.thread_id == 123

    def test_market_response_model(self):
        from lzt_api.market.models import Category_ListResponse
        data = {"category": {}, "system_info": MARKET_SYSTEM_INFO}
        model = Category_ListResponse.model_validate(data)
        assert model.system_info.visitor_id == 1

    def test_model_extra_fields(self):
        from lzt_api.forum.models import Threads_GetResponse
        data = {"thread": THREAD_DATA, "system_info": SYSTEM_INFO, "some_new_field": 42}
        model = Threads_GetResponse.model_validate(data)
        assert model is not None


class TestExceptions:
    def test_lolz_api_error(self):
        err = LolzAPIError(500, "internal")
        assert err.status_code == 500
        assert "500" in str(err)

    def test_rate_limit_error(self):
        err = RateLimitError(retry_after=5.0)
        assert err.retry_after == 5.0
        assert err.status_code == 429

    def test_not_found_error(self):
        err = NotFoundError()
        assert err.status_code == 404

    def test_auth_error(self):
        err = AuthError()
        assert err.status_code == 401


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
