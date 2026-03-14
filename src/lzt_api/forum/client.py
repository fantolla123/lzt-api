from __future__ import annotations

from typing import Any, BinaryIO

from lzt_api.client import BaseClient, AsyncBaseClient
from lzt_api.forum.models import Assets_CssResponse, Batch_ExecuteResponse, Chatbox_EditMessageResponse, Chatbox_GetIgnoreResponse, Chatbox_GetLeaderboardResponse, Chatbox_GetMessagesResponse, Chatbox_IndexResponse, Chatbox_OnlineResponse, Chatbox_PostMessageResponse, Chatbox_ReportReasonsResponse, Conversations_Alerts_DisableResponse, Conversations_Alerts_EnableResponse, Conversations_CreateResponse, Conversations_ListResponse, Conversations_Messages_CreateResponse, Conversations_Messages_EditResponse, Conversations_Messages_ListResponse, Conversations_ReadAllResponse, Conversations_SearchResponse, Conversations_StarResponse, Conversations_StartResponse, Conversations_UnstarResponse, Forms_CreateResponse, Forms_ListResponse, Forums_GetFeedOptionsResponse, Forums_GroupedResponse, Forums_ListResponse, Links_GetResponse, Links_ListResponse, OAuth_TokenResponse, Posts_Comments_EditResponse, Posts_CreateResponse, Posts_EditResponse, Posts_GetResponse, Posts_ReportReasonsResponse, ProfilePosts_Comments_EditResponse, ProfilePosts_ReportReasonsResponse, Search_AllResponse, Search_UsersResponse, Threads_ClaimResponse, Threads_CreateContestResponse, Threads_CreateResponse, Threads_EditResponse, Threads_GetResponse, Users_ClaimsResponse, Users_GetResponse, Users_IgnoredResponse, Users_LikesResponse, Users_ListResponse, Users_SA_ResetResponse, Users_SecretAnswerTypesResponse, Users_TrophiesResponse


class ForumClient(BaseClient):
    def __init__(self, token: str, base_url: str = "https://prod-api.lolz.live", proxy: str | None = None, timeout: float = 30.0):
        super().__init__(token=token, base_url=base_url, proxy=proxy, timeout=timeout)

    def o_auth_token(
        self,
    ) -> OAuth_TokenResponse:

        path = "/oauth/token"
        raw = self._request("POST", path)
        return OAuth_TokenResponse.model_validate(raw)

    def assets_css(
        self,
        css: list[str] | None = None,
    ) -> Assets_CssResponse:

        path = "/css"
        params: dict[str, Any] = {}
        if css is not None:
            params["css"] = css
        raw = self._request("GET", path, params=params)
        return Assets_CssResponse.model_validate(raw)

    def categories_list(
        self,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:

        path = "/categories"
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        raw = self._request("GET", path, params=params)
        return raw

    def categories_get(
        self,
        category_id: int,
    ) -> dict[str, Any]:

        path = "/categories/{category_id}"
        path = path.replace("{category_id}", str(category_id))
        raw = self._request("GET", path)
        return raw

    def forums_list(
        self,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: str | None = None,
    ) -> Forums_ListResponse:

        path = "/forums"
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        raw = self._request("GET", path, params=params)
        return Forums_ListResponse.model_validate(raw)

    def forums_grouped(
        self,
    ) -> Forums_GroupedResponse:

        path = "/forums/grouped"
        raw = self._request("GET", path)
        return Forums_GroupedResponse.model_validate(raw)

    def forums_get(
        self,
        forum_id: int,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}"
        path = path.replace("{forum_id}", str(forum_id))
        raw = self._request("GET", path)
        return raw

    def forums_followers(
        self,
        forum_id: int,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}/followers"
        path = path.replace("{forum_id}", str(forum_id))
        raw = self._request("GET", path)
        return raw

    def forums_follow(
        self,
        forum_id: int,
        post: bool | None = None,
        alert: bool | None = None,
        email: bool | None = None,
        prefix_ids: list[int] | None = None,
        minimal_contest_amount: int | None = None,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}/followers"
        path = path.replace("{forum_id}", str(forum_id))
        data: dict[str, Any] = {}
        if post is not None:
            data["post"] = post
        if alert is not None:
            data["alert"] = alert
        if email is not None:
            data["email"] = email
        if prefix_ids is not None:
            data["prefix_ids"] = prefix_ids
        if minimal_contest_amount is not None:
            data["minimal_contest_amount"] = minimal_contest_amount
        raw = self._request("POST", path, json=data)
        return raw

    def forums_unfollow(
        self,
        forum_id: int,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}/followers"
        path = path.replace("{forum_id}", str(forum_id))
        raw = self._request("DELETE", path)
        return raw

    def forums_followed(
        self,
        total: bool | None = None,
    ) -> dict[str, Any]:

        path = "/forums/followed"
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        raw = self._request("GET", path, params=params)
        return raw

    def forums_get_feed_options(
        self,
    ) -> Forums_GetFeedOptionsResponse:

        path = "/forums/feed/options"
        raw = self._request("GET", path)
        return Forums_GetFeedOptionsResponse.model_validate(raw)

    def forums_edit_feed_options(
        self,
        node_ids: list[int] | None = None,
        keywords: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/forums/feed/options"
        data: dict[str, Any] = {}
        if node_ids is not None:
            data["node_ids"] = node_ids
        if keywords is not None:
            data["keywords"] = keywords
        raw = self._request("PUT", path, json=data)
        return raw

    def links_list(
        self,
    ) -> Links_ListResponse:

        path = "/link-forums"
        raw = self._request("GET", path)
        return Links_ListResponse.model_validate(raw)

    def links_get(
        self,
        link_id: int,
    ) -> Links_GetResponse:

        path = "/link-forums/{link_id}"
        path = path.replace("{link_id}", str(link_id))
        raw = self._request("GET", path)
        return Links_GetResponse.model_validate(raw)

    def pages_list(
        self,
        parent_page_id: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:

        path = "/pages"
        params: dict[str, Any] = {}
        if parent_page_id is not None:
            params["parent_page_id"] = parent_page_id
        if order is not None:
            params["order"] = order
        raw = self._request("GET", path, params=params)
        return raw

    def pages_get(
        self,
        page_id: int,
    ) -> dict[str, Any]:

        path = "/pages/{page_id}"
        path = path.replace("{page_id}", str(page_id))
        raw = self._request("GET", path)
        return raw

    def navigation_list(
        self,
        parent: int | None = None,
    ) -> dict[str, Any]:

        path = "/navigation"
        params: dict[str, Any] = {}
        if parent is not None:
            params["parent"] = parent
        raw = self._request("GET", path, params=params)
        return raw

    def threads_list(
        self,
        forum_id: int | None = None,
        tab: str | None = None,
        state: str | None = None,
        period: str | None = None,
        title: str | None = None,
        title_only: bool | None = None,
        creator_user_id: int | None = None,
        sticky: bool | None = None,
        prefix_ids: list[int] | None = None,
        prefix_ids_not: list[int] | None = None,
        thread_tag_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        direction: str | None = None,
        thread_create_date: int | None = None,
        thread_update_date: int | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/threads"
        params: dict[str, Any] = {}
        if forum_id is not None:
            params["forum_id"] = forum_id
        if tab is not None:
            params["tab"] = tab
        if state is not None:
            params["state"] = state
        if period is not None:
            params["period"] = period
        if title is not None:
            params["title"] = title
        if title_only is not None:
            params["title_only"] = title_only
        if creator_user_id is not None:
            params["creator_user_id"] = creator_user_id
        if sticky is not None:
            params["sticky"] = sticky
        if prefix_ids is not None:
            params["prefix_ids[]"] = prefix_ids
        if prefix_ids_not is not None:
            params["prefix_ids_not[]"] = prefix_ids_not
        if thread_tag_id is not None:
            params["thread_tag_id"] = thread_tag_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if direction is not None:
            params["direction"] = direction
        if thread_create_date is not None:
            params["thread_create_date"] = thread_create_date
        if thread_update_date is not None:
            params["thread_update_date"] = thread_update_date
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return raw

    def threads_create(
        self,
        post_body: str,
        forum_id: int,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
    ) -> Threads_CreateResponse:

        path = "/threads"
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if forum_id is not None:
            data["forum_id"] = forum_id
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if prefix_id is not None:
            data["prefix_id"] = prefix_id
        if tags is not None:
            data["tags"] = tags
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            data["schedule_date"] = schedule_date
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            data["watch_thread_email"] = watch_thread_email
        raw = self._request("POST", path, json=data)
        return Threads_CreateResponse.model_validate(raw)

    def threads_create_contest(
        self,
        post_body: str,
        contest_type: str,
        prize_type: str,
        require_like_count: int,
        require_total_like_count: int,
        title: str | None = None,
        title_en: str | None = None,
        length_value: int | None = None,
        length_option: str | None = None,
        count_winners: int | None = None,
        prize_data_money: float | None = None,
        is_money_places: bool | None = None,
        prize_data_places: list[float] | None = None,
        prize_data_upgrade: int | None = None,
        secret_answer: str | None = None,
        tags: list[str] | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
    ) -> Threads_CreateContestResponse:

        path = "/contests"
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if contest_type is not None:
            data["contest_type"] = contest_type
        if length_value is not None:
            data["length_value"] = length_value
        if length_option is not None:
            data["length_option"] = length_option
        if prize_type is not None:
            data["prize_type"] = prize_type
        if count_winners is not None:
            data["count_winners"] = count_winners
        if prize_data_money is not None:
            data["prize_data_money"] = prize_data_money
        if is_money_places is not None:
            data["is_money_places"] = is_money_places
        if prize_data_places is not None:
            data["prize_data_places"] = prize_data_places
        if prize_data_upgrade is not None:
            data["prize_data_upgrade"] = prize_data_upgrade
        if require_like_count is not None:
            data["require_like_count"] = require_like_count
        if require_total_like_count is not None:
            data["require_total_like_count"] = require_total_like_count
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        if tags is not None:
            data["tags"] = tags
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            data["dont_alert_followers"] = dont_alert_followers
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if schedule_date is not None:
            data["schedule_date"] = schedule_date
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            data["watch_thread_email"] = watch_thread_email
        raw = self._request("POST", path, json=data)
        return Threads_CreateContestResponse.model_validate(raw)

    def threads_claim(
        self,
        as_responder: str,
        as_is_market_deal: bool,
        as_amount: float,
        transfer_type: str,
        post_body: str,
        as_market_item_id: int | None = None,
        as_data: str | None = None,
        currency: str | None = None,
        pay_claim: str | None = None,
        as_funds_receipt: str | None = None,
        as_tg_login_screenshot: str | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
    ) -> Threads_ClaimResponse:

        path = "/claims"
        data: dict[str, Any] = {}
        if as_responder is not None:
            data["as_responder"] = as_responder
        if as_is_market_deal is not None:
            data["as_is_market_deal"] = as_is_market_deal
        if as_market_item_id is not None:
            data["as_market_item_id"] = as_market_item_id
        if as_data is not None:
            data["as_data"] = as_data
        if as_amount is not None:
            data["as_amount"] = as_amount
        if currency is not None:
            data["currency"] = currency
        if transfer_type is not None:
            data["transfer_type"] = transfer_type
        if pay_claim is not None:
            data["pay_claim"] = pay_claim
        if as_funds_receipt is not None:
            data["as_funds_receipt"] = as_funds_receipt
        if as_tg_login_screenshot is not None:
            data["as_tg_login_screenshot"] = as_tg_login_screenshot
        if tags is not None:
            data["tags"] = tags
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            data["schedule_date"] = schedule_date
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            data["watch_thread_email"] = watch_thread_email
        if post_body is not None:
            data["post_body"] = post_body
        raw = self._request("POST", path, json=data)
        return Threads_ClaimResponse.model_validate(raw)

    def threads_get(
        self,
        thread_id: int,
        fields_include: list[str] | None = None,
    ) -> Threads_GetResponse:

        path = "/threads/{thread_id}"
        path = path.replace("{thread_id}", str(thread_id))
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return Threads_GetResponse.model_validate(raw)

    def threads_edit(
        self,
        thread_id: int,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        discussion_open: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = None,
        comment_ignore_group: bool | None = None,
    ) -> Threads_EditResponse:

        path = "/threads/{thread_id}"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if prefix_id is not None:
            data["prefix_id"] = prefix_id
        if tags is not None:
            data["tags"] = tags
        if discussion_open is not None:
            data["discussion_open"] = discussion_open
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        raw = self._request("PUT", path, json=data)
        return Threads_EditResponse.model_validate(raw)

    def threads_delete(
        self,
        thread_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if reason is not None:
            data["reason"] = reason
        raw = self._request("DELETE", path, json=data)
        return raw

    def threads_move(
        self,
        thread_id: int,
        node_id: str,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        apply_thread_prefix: bool | None = None,
        send_alert: bool | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/move"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if node_id is not None:
            data["node_id"] = node_id
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if prefix_id is not None:
            data["prefix_id"] = prefix_id
        if apply_thread_prefix is not None:
            data["apply_thread_prefix"] = apply_thread_prefix
        if send_alert is not None:
            data["send_alert"] = send_alert
        raw = self._request("POST", path, json=data)
        return raw

    def threads_bump(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/bump"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("POST", path)
        return raw

    def threads_hide(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/hide"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("POST", path)
        return raw

    def threads_star(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/star"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("POST", path)
        return raw

    def threads_unstar(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/star"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("DELETE", path)
        return raw

    def threads_followers(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/followers"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("GET", path)
        return raw

    def threads_follow(
        self,
        thread_id: int,
        email: bool | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/followers"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if email is not None:
            data["email"] = email
        raw = self._request("POST", path, json=data)
        return raw

    def threads_unfollow(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/followers"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("DELETE", path)
        return raw

    def threads_followed(
        self,
        total: bool | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/threads/followed"
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return raw

    def threads_navigation(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/navigation"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("GET", path)
        return raw

    def threads_poll_get(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/poll"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("GET", path)
        return raw

    def threads_poll_vote(
        self,
        thread_id: int,
        response_id: int | None = None,
        response_ids: list[int] | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/poll/votes"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if response_id is not None:
            data["response_id"] = response_id
        if response_ids is not None:
            data["response_ids"] = response_ids
        raw = self._request("POST", path, json=data)
        return raw

    def threads_unread(
        self,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/threads/new"
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        raw = self._request("GET", path, params=params)
        return raw

    def threads_recent(
        self,
        days: int | None = None,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/threads/recent"
        params: dict[str, Any] = {}
        if days is not None:
            params["days"] = days
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        raw = self._request("GET", path, params=params)
        return raw

    def threads_finish(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/contests/{thread_id}/finish"
        path = path.replace("{thread_id}", str(thread_id))
        raw = self._request("POST", path)
        return raw

    def posts_list(
        self,
        thread_id: int | None = None,
        page_of_post_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:

        path = "/posts"
        params: dict[str, Any] = {}
        if thread_id is not None:
            params["thread_id"] = thread_id
        if page_of_post_id is not None:
            params["page_of_post_id"] = page_of_post_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        raw = self._request("GET", path, params=params)
        return raw

    def posts_create(
        self,
        post_body: str,
        thread_id: int | None = None,
        quote_post_id: int | None = None,
    ) -> Posts_CreateResponse:

        path = "/posts"
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if thread_id is not None:
            data["thread_id"] = thread_id
        if quote_post_id is not None:
            data["quote_post_id"] = quote_post_id
        raw = self._request("POST", path, json=data)
        return Posts_CreateResponse.model_validate(raw)

    def posts_get(
        self,
        post_id: int,
    ) -> Posts_GetResponse:

        path = "/posts/{post_id}"
        path = path.replace("{post_id}", str(post_id))
        raw = self._request("GET", path)
        return Posts_GetResponse.model_validate(raw)

    def posts_edit(
        self,
        post_id: int,
        post_body: str | None = None,
    ) -> Posts_EditResponse:

        path = "/posts/{post_id}"
        path = path.replace("{post_id}", str(post_id))
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        raw = self._request("PUT", path, json=data)
        return Posts_EditResponse.model_validate(raw)

    def posts_delete(
        self,
        post_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}"
        path = path.replace("{post_id}", str(post_id))
        data: dict[str, Any] = {}
        if reason is not None:
            data["reason"] = reason
        raw = self._request("DELETE", path, json=data)
        return raw

    def posts_likes(
        self,
        post_id: int,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/likes"
        path = path.replace("{post_id}", str(post_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def posts_like(
        self,
        post_id: int,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/likes"
        path = path.replace("{post_id}", str(post_id))
        raw = self._request("POST", path)
        return raw

    def posts_unlike(
        self,
        post_id: int,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/likes"
        path = path.replace("{post_id}", str(post_id))
        raw = self._request("DELETE", path)
        return raw

    def posts_report_reasons(
        self,
        post_id: int,
    ) -> Posts_ReportReasonsResponse:

        path = "/posts/{post_id}/report"
        path = path.replace("{post_id}", str(post_id))
        raw = self._request("GET", path)
        return Posts_ReportReasonsResponse.model_validate(raw)

    def posts_report(
        self,
        post_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/report"
        path = path.replace("{post_id}", str(post_id))
        data: dict[str, Any] = {}
        if message is not None:
            data["message"] = message
        raw = self._request("POST", path, json=data)
        return raw

    def posts_comments_get(
        self,
        post_id: int,
        before: int | None = None,
        before_comment: int | None = None,
    ) -> dict[str, Any]:

        path = "/posts/comments"
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if before is not None:
            params["before"] = before
        if before_comment is not None:
            params["before_comment"] = before_comment
        raw = self._request("GET", path, params=params)
        return raw

    def posts_comments_create(
        self,
        post_id: int,
        comment_body: str,
    ) -> dict[str, Any]:

        path = "/posts/comments"
        data: dict[str, Any] = {}
        if post_id is not None:
            data["post_id"] = post_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = self._request("POST", path, json=data)
        return raw

    def posts_comments_edit(
        self,
        post_comment_id: int,
        comment_body: str,
    ) -> Posts_Comments_EditResponse:

        path = "/posts/comments"
        data: dict[str, Any] = {}
        if post_comment_id is not None:
            data["post_comment_id"] = post_comment_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = self._request("PUT", path, json=data)
        return Posts_Comments_EditResponse.model_validate(raw)

    def posts_comments_delete(
        self,
        post_comment_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/posts/comments"
        data: dict[str, Any] = {}
        if post_comment_id is not None:
            data["post_comment_id"] = post_comment_id
        if reason is not None:
            data["reason"] = reason
        raw = self._request("DELETE", path, json=data)
        return raw

    def posts_comments_report(
        self,
        post_comment_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/posts/comments/report"
        data: dict[str, Any] = {}
        if post_comment_id is not None:
            data["post_comment_id"] = post_comment_id
        if message is not None:
            data["message"] = message
        raw = self._request("POST", path, json=data)
        return raw

    def users_list(
        self,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[str] | None = None,
    ) -> Users_ListResponse:

        path = "/users"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return Users_ListResponse.model_validate(raw)

    def users_fields(
        self,
    ) -> dict[str, Any]:

        path = "/users/fields"
        raw = self._request("GET", path)
        return raw

    def users_find(
        self,
        username: str | None = None,
        custom_fields: dict[str, Any] | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/users/find"
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if custom_fields is not None:
            params["custom_fields"] = custom_fields
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return raw

    def users_get(
        self,
        user_id: UserIDModel,
        fields_include: list[str] | None = None,
    ) -> Users_GetResponse:

        path = "/users/{user_id}"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return Users_GetResponse.model_validate(raw)

    def users_edit(
        self,
        user_id: UserIDModel,
        username: str | None = None,
        user_title: str | None = None,
        display_group_id: int | None = None,
        display_icon_group_id: int | None = None,
        display_banner_id: int | None = None,
        conv_welcome_message: str | None = None,
        user_dob_day: int | None = None,
        user_dob_month: int | None = None,
        user_dob_year: int | None = None,
        secret_answer: str | None = None,
        secret_answer_type: int | None = None,
        short_link: str | None = None,
        language_id: int | None = None,
        gender: str | None = None,
        timezone: str | None = None,
        receive_admin_email: bool | None = None,
        activity_visible: bool | None = None,
        show_dob_date: bool | None = None,
        show_dob_year: bool | None = None,
        hide_username_change_logs: bool | None = None,
        allow_view_profile: str | None = None,
        allow_post_profile: str | None = None,
        allow_send_personal_conversation: str | None = None,
        allow_invite_group: str | None = None,
        allow_receive_news_feed: str | None = None,
        alert: dict[str, Any] | None = None,
        fields: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if username is not None:
            data["username"] = username
        if user_title is not None:
            data["user_title"] = user_title
        if display_group_id is not None:
            data["display_group_id"] = display_group_id
        if display_icon_group_id is not None:
            data["display_icon_group_id"] = display_icon_group_id
        if display_banner_id is not None:
            data["display_banner_id"] = display_banner_id
        if conv_welcome_message is not None:
            data["conv_welcome_message"] = conv_welcome_message
        if user_dob_day is not None:
            data["user_dob_day"] = user_dob_day
        if user_dob_month is not None:
            data["user_dob_month"] = user_dob_month
        if user_dob_year is not None:
            data["user_dob_year"] = user_dob_year
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        if secret_answer_type is not None:
            data["secret_answer_type"] = secret_answer_type
        if short_link is not None:
            data["short_link"] = short_link
        if language_id is not None:
            data["language_id"] = language_id
        if gender is not None:
            data["gender"] = gender
        if timezone is not None:
            data["timezone"] = timezone
        if receive_admin_email is not None:
            data["receive_admin_email"] = receive_admin_email
        if activity_visible is not None:
            data["activity_visible"] = activity_visible
        if show_dob_date is not None:
            data["show_dob_date"] = show_dob_date
        if show_dob_year is not None:
            data["show_dob_year"] = show_dob_year
        if hide_username_change_logs is not None:
            data["hide_username_change_logs"] = hide_username_change_logs
        if allow_view_profile is not None:
            data["allow_view_profile"] = allow_view_profile
        if allow_post_profile is not None:
            data["allow_post_profile"] = allow_post_profile
        if allow_send_personal_conversation is not None:
            data["allow_send_personal_conversation"] = allow_send_personal_conversation
        if allow_invite_group is not None:
            data["allow_invite_group"] = allow_invite_group
        if allow_receive_news_feed is not None:
            data["allow_receive_news_feed"] = allow_receive_news_feed
        if alert is not None:
            data["alert"] = alert
        if fields is not None:
            data["fields"] = fields
        raw = self._request("PUT", path, json=data)
        return raw

    def users_claims(
        self,
        user_id: UserIDModel,
        type_: str | None = None,
        claim_state: str | None = None,
    ) -> Users_ClaimsResponse:

        path = "/users/{user_id}/claims"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if claim_state is not None:
            params["claim_state"] = claim_state
        raw = self._request("GET", path, params=params)
        return Users_ClaimsResponse.model_validate(raw)

    def users_avatar_upload(
        self,
        user_id: UserIDModel,
        avatar: BinaryIO,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/avatar"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if avatar is not None:
            files["avatar"] = avatar
        raw = self._request("POST", path, data=data, files=files)
        return raw

    def users_avatar_delete(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/avatar"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("DELETE", path)
        return raw

    def users_avatar_crop(
        self,
        user_id: UserIDModel,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/avatar/crop"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        raw = self._request("POST", path, json=data)
        return raw

    def users_background_upload(
        self,
        user_id: UserIDModel,
        background: BinaryIO,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/background"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if background is not None:
            files["background"] = background
        raw = self._request("POST", path, data=data, files=files)
        return raw

    def users_background_delete(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/background"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("DELETE", path)
        return raw

    def users_background_crop(
        self,
        user_id: UserIDModel,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/background/crop"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        raw = self._request("POST", path, json=data)
        return raw

    def users_followers(
        self,
        user_id: UserIDModel,
        order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followers"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def users_follow(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followers"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("POST", path)
        return raw

    def users_unfollow(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followers"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("DELETE", path)
        return raw

    def users_followings(
        self,
        user_id: UserIDModel,
        order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followings"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def users_likes(
        self,
        user_id: UserIDModel,
        node_id: int | None = None,
        like_type: str | None = None,
        type_: str | None = "gotten",
        page: int | None = None,
        content_type: str | None = "post",
        search_user_id: int | None = None,
        stats: bool | None = None,
    ) -> Users_LikesResponse:

        path = "/users/{user_id}/likes"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if node_id is not None:
            params["node_id"] = node_id
        if like_type is not None:
            params["like_type"] = like_type
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if content_type is not None:
            params["content_type"] = content_type
        if search_user_id is not None:
            params["search_user_id"] = search_user_id
        if stats is not None:
            params["stats"] = stats
        raw = self._request("GET", path, params=params)
        return Users_LikesResponse.model_validate(raw)

    def users_ignored(
        self,
        total: bool | None = None,
    ) -> Users_IgnoredResponse:

        path = "/users/ignored"
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        raw = self._request("GET", path, params=params)
        return Users_IgnoredResponse.model_validate(raw)

    def users_ignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/ignore"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("POST", path)
        return raw

    def users_ignore_edit(
        self,
        user_id: UserIDModel,
        ignore_conversations: bool | None = None,
        ignore_content: bool | None = None,
        restrict_view_profile: bool | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/ignore"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if ignore_conversations is not None:
            params["ignore_conversations"] = ignore_conversations
        if ignore_content is not None:
            params["ignore_content"] = ignore_content
        if restrict_view_profile is not None:
            params["restrict_view_profile"] = restrict_view_profile
        raw = self._request("PUT", path, params=params)
        return raw

    def users_unignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/ignore"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("DELETE", path)
        return raw

    def users_contents(
        self,
        user_id: UserIDModel,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/timeline"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def users_trophies(
        self,
        user_id: UserIDModel,
    ) -> Users_TrophiesResponse:

        path = "/users/{user_id}/trophies"
        path = path.replace("{user_id}", str(user_id))
        raw = self._request("GET", path)
        return Users_TrophiesResponse.model_validate(raw)

    def users_secret_answer_types(
        self,
    ) -> Users_SecretAnswerTypesResponse:

        path = "/users/secret-answer/types"
        raw = self._request("GET", path)
        return Users_SecretAnswerTypesResponse.model_validate(raw)

    def users_sa_reset(
        self,
    ) -> Users_SA_ResetResponse:

        path = "/account/secret-answer/reset"
        raw = self._request("POST", path)
        return Users_SA_ResetResponse.model_validate(raw)

    def users_sa_cancel_reset(
        self,
    ) -> dict[str, Any]:

        path = "/account/secret-answer/reset"
        raw = self._request("DELETE", path)
        return raw

    def profile_posts_list(
        self,
        user_id: UserIDModel,
        posts_user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/profile-posts"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if posts_user_id is not None:
            params["posts_user_id"] = posts_user_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = self._request("GET", path, params=params)
        return raw

    def profile_posts_get(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("GET", path)
        return raw

    def profile_posts_edit(
        self,
        profile_post_id: int,
        post_body: str | None = None,
        disable_comments: bool | None = None,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if disable_comments is not None:
            data["disable_comments"] = disable_comments
        raw = self._request("PUT", path, json=data)
        return raw

    def profile_posts_delete(
        self,
        profile_post_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        params: dict[str, Any] = {}
        if reason is not None:
            params["reason"] = reason
        raw = self._request("DELETE", path, params=params)
        return raw

    def profile_posts_report_reasons(
        self,
        profile_post_id: int,
    ) -> ProfilePosts_ReportReasonsResponse:

        path = "/profile-posts/{profile_post_id}/report"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("GET", path)
        return ProfilePosts_ReportReasonsResponse.model_validate(raw)

    def profile_posts_report(
        self,
        profile_post_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/report"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        data: dict[str, Any] = {}
        if message is not None:
            data["message"] = message
        raw = self._request("POST", path, json=data)
        return raw

    def profile_posts_create(
        self,
        user_id: UserIDModel,
        post_body: str,
    ) -> dict[str, Any]:

        path = "/profile-posts"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        if post_body is not None:
            data["post_body"] = post_body
        raw = self._request("POST", path, json=data)
        return raw

    def profile_posts_stick(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/stick"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("POST", path)
        return raw

    def profile_posts_unstick(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/stick"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("DELETE", path)
        return raw

    def profile_posts_likes(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/likes"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("GET", path)
        return raw

    def profile_posts_like(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/likes"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("POST", path)
        return raw

    def profile_posts_unlike(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/likes"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = self._request("DELETE", path)
        return raw

    def profile_posts_comments_list(
        self,
        profile_post_id: int,
        before: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments"
        params: dict[str, Any] = {}
        if profile_post_id is not None:
            params["profile_post_id"] = profile_post_id
        if before is not None:
            params["before"] = before
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def profile_posts_comments_create(
        self,
        profile_post_id: int,
        comment_body: str,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments"
        data: dict[str, Any] = {}
        if profile_post_id is not None:
            data["profile_post_id"] = profile_post_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = self._request("POST", path, json=data)
        return raw

    def profile_posts_comments_edit(
        self,
        comment_id: int,
        comment_body: str,
    ) -> ProfilePosts_Comments_EditResponse:

        path = "/profile-posts/comments"
        data: dict[str, Any] = {}
        if comment_id is not None:
            data["comment_id"] = comment_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = self._request("PUT", path, json=data)
        return ProfilePosts_Comments_EditResponse.model_validate(raw)

    def profile_posts_comments_delete(
        self,
        comment_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments"
        data: dict[str, Any] = {}
        if comment_id is not None:
            data["comment_id"] = comment_id
        raw = self._request("DELETE", path, json=data)
        return raw

    def profile_posts_comments_get(
        self,
        profile_post_id: int,
        comment_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/comments/{comment_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        path = path.replace("{comment_id}", str(comment_id))
        raw = self._request("GET", path)
        return raw

    def profile_posts_comments_report(
        self,
        comment_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments/{comment_id}/report"
        path = path.replace("{comment_id}", str(comment_id))
        data: dict[str, Any] = {}
        if message is not None:
            data["message"] = message
        raw = self._request("POST", path, json=data)
        return raw

    def conversations_list(
        self,
        folder: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Conversations_ListResponse:

        path = "/conversations"
        params: dict[str, Any] = {}
        if folder is not None:
            params["folder"] = folder
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return Conversations_ListResponse.model_validate(raw)

    def conversations_create(
        self,
        recipient_id: int | None = None,
        recipients: list[str] | None = None,
        is_group: bool | None = False,
        title: str | None = None,
        open_invite: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
        message_body: str | None = None,
    ) -> Conversations_CreateResponse:

        path = "/conversations"
        data: dict[str, Any] = {}
        if recipient_id is not None:
            data["recipient_id"] = recipient_id
        if recipients is not None:
            data["recipients"] = recipients
        if is_group is not None:
            data["is_group"] = is_group
        if title is not None:
            data["title"] = title
        if open_invite is not None:
            data["open_invite"] = open_invite
        if allow_edit_messages is not None:
            data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            data["allow_delete_own_messages"] = allow_delete_own_messages
        if message_body is not None:
            data["message_body"] = message_body
        raw = self._request("POST", path, json=data)
        return Conversations_CreateResponse.model_validate(raw)

    def conversations_update(
        self,
        conversation_id: int,
        title: str | None = None,
        open_invite: bool | None = None,
        history_open: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
    ) -> dict[str, Any]:

        path = "/conversations"
        data: dict[str, Any] = {}
        if conversation_id is not None:
            data["conversation_id"] = conversation_id
        if title is not None:
            data["title"] = title
        if open_invite is not None:
            data["open_invite"] = open_invite
        if history_open is not None:
            data["history_open"] = history_open
        if allow_edit_messages is not None:
            data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            data["allow_delete_own_messages"] = allow_delete_own_messages
        raw = self._request("PUT", path, json=data)
        return raw

    def conversations_delete(
        self,
        conversation_id: int,
        delete_type: str,
    ) -> dict[str, Any]:

        path = "/conversations"
        data: dict[str, Any] = {}
        if conversation_id is not None:
            data["conversation_id"] = conversation_id
        if delete_type is not None:
            data["delete_type"] = delete_type
        raw = self._request("DELETE", path, json=data)
        return raw

    def conversations_start(
        self,
        user_id: UserIDModel,
    ) -> Conversations_StartResponse:

        path = "/conversations/start"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = self._request("POST", path, json=data)
        return Conversations_StartResponse.model_validate(raw)

    def conversations_save(
        self,
        link: str,
    ) -> dict[str, Any]:

        path = "/conversations/save"
        data: dict[str, Any] = {}
        if link is not None:
            data["link"] = link
        raw = self._request("POST", path, json=data)
        return raw

    def conversations_get(
        self,
        conversation_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = self._request("GET", path)
        return raw

    def conversations_messages_list(
        self,
        conversation_id: int,
        page: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        before: int | None = None,
        after: int | None = None,
    ) -> Conversations_Messages_ListResponse:

        path = "/conversations/{conversation_id}/messages"
        path = path.replace("{conversation_id}", str(conversation_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        raw = self._request("GET", path, params=params)
        return Conversations_Messages_ListResponse.model_validate(raw)

    def conversations_messages_create(
        self,
        conversation_id: int,
        message_body: str,
        reply_message_id: int | None = None,
    ) -> Conversations_Messages_CreateResponse:

        path = "/conversations/{conversation_id}/messages"
        path = path.replace("{conversation_id}", str(conversation_id))
        data: dict[str, Any] = {}
        if reply_message_id is not None:
            data["reply_message_id"] = reply_message_id
        if message_body is not None:
            data["message_body"] = message_body
        raw = self._request("POST", path, json=data)
        return Conversations_Messages_CreateResponse.model_validate(raw)

    def conversations_search(
        self,
        q: str | None = None,
        conversation_id: int | None = None,
        search_recipients: bool | None = None,
    ) -> Conversations_SearchResponse:

        path = "/conversations/search"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if conversation_id is not None:
            data["conversation_id"] = conversation_id
        if search_recipients is not None:
            data["search_recipients"] = search_recipients
        raw = self._request("POST", path, json=data)
        return Conversations_SearchResponse.model_validate(raw)

    def conversations_messages_get(
        self,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/messages/{message_id}"
        path = path.replace("{message_id}", str(message_id))
        raw = self._request("GET", path)
        return raw

    def conversations_messages_edit(
        self,
        conversation_id: int,
        message_id: int,
        message_body: str,
    ) -> Conversations_Messages_EditResponse:

        path = "/conversations/{conversation_id}/messages/{message_id}"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        data: dict[str, Any] = {}
        if message_body is not None:
            data["message_body"] = message_body
        raw = self._request("PUT", path, json=data)
        return Conversations_Messages_EditResponse.model_validate(raw)

    def conversations_messages_delete(
        self,
        conversation_id: int,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/messages/{message_id}"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        raw = self._request("DELETE", path)
        return raw

    def conversations_invite(
        self,
        conversation_id: int,
        recipients: list[str],
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/invite"
        path = path.replace("{conversation_id}", str(conversation_id))
        data: dict[str, Any] = {}
        if recipients is not None:
            data["recipients"] = recipients
        raw = self._request("POST", path, json=data)
        return raw

    def conversations_kick(
        self,
        conversation_id: int,
        user_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/kick"
        path = path.replace("{conversation_id}", str(conversation_id))
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = self._request("POST", path, json=data)
        return raw

    def conversations_read(
        self,
        conversation_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/read"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = self._request("POST", path)
        return raw

    def conversations_read_all(
        self,
    ) -> Conversations_ReadAllResponse:

        path = "/conversations/read-all"
        raw = self._request("POST", path)
        return Conversations_ReadAllResponse.model_validate(raw)

    def conversations_messages_stick(
        self,
        conversation_id: int,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/messages/{message_id}/stick"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        raw = self._request("POST", path)
        return raw

    def conversations_messages_unstick(
        self,
        conversation_id: int,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/messages/{message_id}/stick"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        raw = self._request("DELETE", path)
        return raw

    def conversations_star(
        self,
        conversation_id: int,
    ) -> Conversations_StarResponse:

        path = "/conversations/{conversation_id}/star"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = self._request("POST", path)
        return Conversations_StarResponse.model_validate(raw)

    def conversations_unstar(
        self,
        conversation_id: int,
    ) -> Conversations_UnstarResponse:

        path = "/conversations/{conversation_id}/star"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = self._request("DELETE", path)
        return Conversations_UnstarResponse.model_validate(raw)

    def conversations_alerts_enable(
        self,
        conversation_id: int,
    ) -> Conversations_Alerts_EnableResponse:

        path = "/conversations/{conversation_id}/alerts"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = self._request("POST", path)
        return Conversations_Alerts_EnableResponse.model_validate(raw)

    def conversations_alerts_disable(
        self,
        conversation_id: int,
    ) -> Conversations_Alerts_DisableResponse:

        path = "/conversations/{conversation_id}/alerts"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = self._request("DELETE", path)
        return Conversations_Alerts_DisableResponse.model_validate(raw)

    def notifications_list(
        self,
        type_: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/notifications"
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def notifications_get(
        self,
        notification_id: int,
    ) -> dict[str, Any]:

        path = "/notifications/{notification_id}/content"
        path = path.replace("{notification_id}", str(notification_id))
        raw = self._request("GET", path)
        return raw

    def notifications_read(
        self,
        notification_id: int | None = None,
    ) -> dict[str, Any]:

        path = "/notifications/read"
        data: dict[str, Any] = {}
        if notification_id is not None:
            data["notification_id"] = notification_id
        raw = self._request("POST", path, json=data)
        return raw

    def tags_popular(
        self,
    ) -> dict[str, Any]:

        path = "/tags"
        raw = self._request("GET", path)
        return raw

    def tags_list(
        self,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/tags/list"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def tags_get(
        self,
        tag_id: int,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/tags/{tag_id}"
        path = path.replace("{tag_id}", str(tag_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = self._request("GET", path, params=params)
        return raw

    def tags_find(
        self,
        tag: str,
    ) -> dict[str, Any]:

        path = "/tags/find"
        params: dict[str, Any] = {}
        if tag is not None:
            params["tag"] = tag
        raw = self._request("GET", path, params=params)
        return raw

    def search_all(
        self,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: UserIDModel | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Search_AllResponse:

        path = "/search"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if tag is not None:
            data["tag"] = tag
        if forum_id is not None:
            data["forum_id"] = forum_id
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = self._request("POST", path, json=data)
        return Search_AllResponse.model_validate(raw)

    def search_threads(
        self,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: UserIDModel | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/threads"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if tag is not None:
            data["tag"] = tag
        if forum_id is not None:
            data["forum_id"] = forum_id
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        if data_limit is not None:
            data["data_limit"] = data_limit
        raw = self._request("POST", path, json=data)
        return raw

    def search_posts(
        self,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: UserIDModel | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/posts"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if tag is not None:
            data["tag"] = tag
        if forum_id is not None:
            data["forum_id"] = forum_id
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        if data_limit is not None:
            data["data_limit"] = data_limit
        raw = self._request("POST", path, json=data)
        return raw

    def search_users(
        self,
        q: str | None = None,
    ) -> Search_UsersResponse:

        path = "/search/users"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        raw = self._request("POST", path, json=data)
        return Search_UsersResponse.model_validate(raw)

    def search_profile_posts(
        self,
        q: str | None = None,
        user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/profile-posts"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = self._request("POST", path, json=data)
        return raw

    def search_tagged(
        self,
        tag: str | None = None,
        tags: list[str] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/tagged"
        data: dict[str, Any] = {}
        if tag is not None:
            data["tag"] = tag
        if tags is not None:
            data["tags"] = tags
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = self._request("POST", path, json=data)
        return raw

    def search_results(
        self,
        search_id: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/{search_id}/results"
        path = path.replace("{search_id}", str(search_id))
        data: dict[str, Any] = {}
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = self._request("GET", path, json=data)
        return raw

    def batch_execute(
        self,
    ) -> Batch_ExecuteResponse:

        path = "/batch"
        raw = self._request("POST", path)
        return Batch_ExecuteResponse.model_validate(raw)

    def chatbox_index(
        self,
        room_id: RoomIDModel | None = None,
    ) -> Chatbox_IndexResponse:

        path = "/chatbox"
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        raw = self._request("GET", path, params=params)
        return Chatbox_IndexResponse.model_validate(raw)

    def chatbox_get_messages(
        self,
        room_id: RoomIDModel,
        before_message_id: int | None = None,
    ) -> Chatbox_GetMessagesResponse:

        path = "/chatbox/messages"
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        if before_message_id is not None:
            params["before_message_id"] = before_message_id
        raw = self._request("GET", path, params=params)
        return Chatbox_GetMessagesResponse.model_validate(raw)

    def chatbox_post_message(
        self,
        room_id: RoomIDModel,
        message: str,
        reply_message_id: int | None = None,
    ) -> Chatbox_PostMessageResponse:

        path = "/chatbox/messages"
        data: dict[str, Any] = {}
        if room_id is not None:
            data["room_id"] = room_id
        if reply_message_id is not None:
            data["reply_message_id"] = reply_message_id
        if message is not None:
            data["message"] = message
        raw = self._request("POST", path, json=data)
        return Chatbox_PostMessageResponse.model_validate(raw)

    def chatbox_edit_message(
        self,
        message_id: int,
        message: str,
    ) -> Chatbox_EditMessageResponse:

        path = "/chatbox/messages"
        data: dict[str, Any] = {}
        if message_id is not None:
            data["message_id"] = message_id
        if message is not None:
            data["message"] = message
        raw = self._request("PUT", path, json=data)
        return Chatbox_EditMessageResponse.model_validate(raw)

    def chatbox_delete_message(
        self,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/chatbox/messages"
        data: dict[str, Any] = {}
        if message_id is not None:
            data["message_id"] = message_id
        raw = self._request("DELETE", path, json=data)
        return raw

    def chatbox_online(
        self,
        room_id: RoomIDModel,
    ) -> Chatbox_OnlineResponse:

        path = "/chatbox/messages/online"
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        raw = self._request("GET", path, params=params)
        return Chatbox_OnlineResponse.model_validate(raw)

    def chatbox_report_reasons(
        self,
        message_id: int,
    ) -> Chatbox_ReportReasonsResponse:

        path = "/chatbox/messages/report"
        params: dict[str, Any] = {}
        if message_id is not None:
            params["message_id"] = message_id
        raw = self._request("GET", path, params=params)
        return Chatbox_ReportReasonsResponse.model_validate(raw)

    def chatbox_report(
        self,
        message_id: int,
        reason: str,
    ) -> dict[str, Any]:

        path = "/chatbox/messages/report"
        data: dict[str, Any] = {}
        if message_id is not None:
            data["message_id"] = message_id
        if reason is not None:
            data["reason"] = reason
        raw = self._request("POST", path, json=data)
        return raw

    def chatbox_get_leaderboard(
        self,
        duration: str | None = None,
    ) -> Chatbox_GetLeaderboardResponse:

        path = "/chatbox/messages/leaderboard"
        params: dict[str, Any] = {}
        if duration is not None:
            params["duration"] = duration
        raw = self._request("GET", path, params=params)
        return Chatbox_GetLeaderboardResponse.model_validate(raw)

    def chatbox_get_ignore(
        self,
    ) -> Chatbox_GetIgnoreResponse:

        path = "/chatbox/ignore"
        raw = self._request("GET", path)
        return Chatbox_GetIgnoreResponse.model_validate(raw)

    def chatbox_post_ignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/chatbox/ignore"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = self._request("POST", path, json=data)
        return raw

    def chatbox_delete_ignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/chatbox/ignore"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = self._request("DELETE", path, json=data)
        return raw

    def forms_list(
        self,
        page: int | None = None,
    ) -> Forms_ListResponse:

        path = "/forms"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        raw = self._request("GET", path, params=params)
        return Forms_ListResponse.model_validate(raw)

    def forms_create(
        self,
    ) -> Forms_CreateResponse:

        path = "/forms/save"
        raw = self._request("POST", path)
        return Forms_CreateResponse.model_validate(raw)


class AsyncForumClient(AsyncBaseClient):
    def __init__(self, token: str, base_url: str = "https://prod-api.lolz.live", proxy: str | None = None, timeout: float = 30.0):
        super().__init__(token=token, base_url=base_url, proxy=proxy, timeout=timeout)

    async def o_auth_token(
        self,
    ) -> OAuth_TokenResponse:

        path = "/oauth/token"
        raw = await self._request("POST", path)
        return OAuth_TokenResponse.model_validate(raw)

    async def assets_css(
        self,
        css: list[str] | None = None,
    ) -> Assets_CssResponse:

        path = "/css"
        params: dict[str, Any] = {}
        if css is not None:
            params["css"] = css
        raw = await self._request("GET", path, params=params)
        return Assets_CssResponse.model_validate(raw)

    async def categories_list(
        self,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:

        path = "/categories"
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        raw = await self._request("GET", path, params=params)
        return raw

    async def categories_get(
        self,
        category_id: int,
    ) -> dict[str, Any]:

        path = "/categories/{category_id}"
        path = path.replace("{category_id}", str(category_id))
        raw = await self._request("GET", path)
        return raw

    async def forums_list(
        self,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: str | None = None,
    ) -> Forums_ListResponse:

        path = "/forums"
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        raw = await self._request("GET", path, params=params)
        return Forums_ListResponse.model_validate(raw)

    async def forums_grouped(
        self,
    ) -> Forums_GroupedResponse:

        path = "/forums/grouped"
        raw = await self._request("GET", path)
        return Forums_GroupedResponse.model_validate(raw)

    async def forums_get(
        self,
        forum_id: int,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}"
        path = path.replace("{forum_id}", str(forum_id))
        raw = await self._request("GET", path)
        return raw

    async def forums_followers(
        self,
        forum_id: int,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}/followers"
        path = path.replace("{forum_id}", str(forum_id))
        raw = await self._request("GET", path)
        return raw

    async def forums_follow(
        self,
        forum_id: int,
        post: bool | None = None,
        alert: bool | None = None,
        email: bool | None = None,
        prefix_ids: list[int] | None = None,
        minimal_contest_amount: int | None = None,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}/followers"
        path = path.replace("{forum_id}", str(forum_id))
        data: dict[str, Any] = {}
        if post is not None:
            data["post"] = post
        if alert is not None:
            data["alert"] = alert
        if email is not None:
            data["email"] = email
        if prefix_ids is not None:
            data["prefix_ids"] = prefix_ids
        if minimal_contest_amount is not None:
            data["minimal_contest_amount"] = minimal_contest_amount
        raw = await self._request("POST", path, json=data)
        return raw

    async def forums_unfollow(
        self,
        forum_id: int,
    ) -> dict[str, Any]:

        path = "/forums/{forum_id}/followers"
        path = path.replace("{forum_id}", str(forum_id))
        raw = await self._request("DELETE", path)
        return raw

    async def forums_followed(
        self,
        total: bool | None = None,
    ) -> dict[str, Any]:

        path = "/forums/followed"
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        raw = await self._request("GET", path, params=params)
        return raw

    async def forums_get_feed_options(
        self,
    ) -> Forums_GetFeedOptionsResponse:

        path = "/forums/feed/options"
        raw = await self._request("GET", path)
        return Forums_GetFeedOptionsResponse.model_validate(raw)

    async def forums_edit_feed_options(
        self,
        node_ids: list[int] | None = None,
        keywords: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/forums/feed/options"
        data: dict[str, Any] = {}
        if node_ids is not None:
            data["node_ids"] = node_ids
        if keywords is not None:
            data["keywords"] = keywords
        raw = await self._request("PUT", path, json=data)
        return raw

    async def links_list(
        self,
    ) -> Links_ListResponse:

        path = "/link-forums"
        raw = await self._request("GET", path)
        return Links_ListResponse.model_validate(raw)

    async def links_get(
        self,
        link_id: int,
    ) -> Links_GetResponse:

        path = "/link-forums/{link_id}"
        path = path.replace("{link_id}", str(link_id))
        raw = await self._request("GET", path)
        return Links_GetResponse.model_validate(raw)

    async def pages_list(
        self,
        parent_page_id: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:

        path = "/pages"
        params: dict[str, Any] = {}
        if parent_page_id is not None:
            params["parent_page_id"] = parent_page_id
        if order is not None:
            params["order"] = order
        raw = await self._request("GET", path, params=params)
        return raw

    async def pages_get(
        self,
        page_id: int,
    ) -> dict[str, Any]:

        path = "/pages/{page_id}"
        path = path.replace("{page_id}", str(page_id))
        raw = await self._request("GET", path)
        return raw

    async def navigation_list(
        self,
        parent: int | None = None,
    ) -> dict[str, Any]:

        path = "/navigation"
        params: dict[str, Any] = {}
        if parent is not None:
            params["parent"] = parent
        raw = await self._request("GET", path, params=params)
        return raw

    async def threads_list(
        self,
        forum_id: int | None = None,
        tab: str | None = None,
        state: str | None = None,
        period: str | None = None,
        title: str | None = None,
        title_only: bool | None = None,
        creator_user_id: int | None = None,
        sticky: bool | None = None,
        prefix_ids: list[int] | None = None,
        prefix_ids_not: list[int] | None = None,
        thread_tag_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        direction: str | None = None,
        thread_create_date: int | None = None,
        thread_update_date: int | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/threads"
        params: dict[str, Any] = {}
        if forum_id is not None:
            params["forum_id"] = forum_id
        if tab is not None:
            params["tab"] = tab
        if state is not None:
            params["state"] = state
        if period is not None:
            params["period"] = period
        if title is not None:
            params["title"] = title
        if title_only is not None:
            params["title_only"] = title_only
        if creator_user_id is not None:
            params["creator_user_id"] = creator_user_id
        if sticky is not None:
            params["sticky"] = sticky
        if prefix_ids is not None:
            params["prefix_ids[]"] = prefix_ids
        if prefix_ids_not is not None:
            params["prefix_ids_not[]"] = prefix_ids_not
        if thread_tag_id is not None:
            params["thread_tag_id"] = thread_tag_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if direction is not None:
            params["direction"] = direction
        if thread_create_date is not None:
            params["thread_create_date"] = thread_create_date
        if thread_update_date is not None:
            params["thread_update_date"] = thread_update_date
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return raw

    async def threads_create(
        self,
        post_body: str,
        forum_id: int,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
    ) -> Threads_CreateResponse:

        path = "/threads"
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if forum_id is not None:
            data["forum_id"] = forum_id
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if prefix_id is not None:
            data["prefix_id"] = prefix_id
        if tags is not None:
            data["tags"] = tags
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            data["schedule_date"] = schedule_date
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            data["watch_thread_email"] = watch_thread_email
        raw = await self._request("POST", path, json=data)
        return Threads_CreateResponse.model_validate(raw)

    async def threads_create_contest(
        self,
        post_body: str,
        contest_type: str,
        prize_type: str,
        require_like_count: int,
        require_total_like_count: int,
        title: str | None = None,
        title_en: str | None = None,
        length_value: int | None = None,
        length_option: str | None = None,
        count_winners: int | None = None,
        prize_data_money: float | None = None,
        is_money_places: bool | None = None,
        prize_data_places: list[float] | None = None,
        prize_data_upgrade: int | None = None,
        secret_answer: str | None = None,
        tags: list[str] | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
    ) -> Threads_CreateContestResponse:

        path = "/contests"
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if contest_type is not None:
            data["contest_type"] = contest_type
        if length_value is not None:
            data["length_value"] = length_value
        if length_option is not None:
            data["length_option"] = length_option
        if prize_type is not None:
            data["prize_type"] = prize_type
        if count_winners is not None:
            data["count_winners"] = count_winners
        if prize_data_money is not None:
            data["prize_data_money"] = prize_data_money
        if is_money_places is not None:
            data["is_money_places"] = is_money_places
        if prize_data_places is not None:
            data["prize_data_places"] = prize_data_places
        if prize_data_upgrade is not None:
            data["prize_data_upgrade"] = prize_data_upgrade
        if require_like_count is not None:
            data["require_like_count"] = require_like_count
        if require_total_like_count is not None:
            data["require_total_like_count"] = require_total_like_count
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        if tags is not None:
            data["tags"] = tags
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            data["dont_alert_followers"] = dont_alert_followers
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if schedule_date is not None:
            data["schedule_date"] = schedule_date
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            data["watch_thread_email"] = watch_thread_email
        raw = await self._request("POST", path, json=data)
        return Threads_CreateContestResponse.model_validate(raw)

    async def threads_claim(
        self,
        as_responder: str,
        as_is_market_deal: bool,
        as_amount: float,
        transfer_type: str,
        post_body: str,
        as_market_item_id: int | None = None,
        as_data: str | None = None,
        currency: str | None = None,
        pay_claim: str | None = None,
        as_funds_receipt: str | None = None,
        as_tg_login_screenshot: str | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
    ) -> Threads_ClaimResponse:

        path = "/claims"
        data: dict[str, Any] = {}
        if as_responder is not None:
            data["as_responder"] = as_responder
        if as_is_market_deal is not None:
            data["as_is_market_deal"] = as_is_market_deal
        if as_market_item_id is not None:
            data["as_market_item_id"] = as_market_item_id
        if as_data is not None:
            data["as_data"] = as_data
        if as_amount is not None:
            data["as_amount"] = as_amount
        if currency is not None:
            data["currency"] = currency
        if transfer_type is not None:
            data["transfer_type"] = transfer_type
        if pay_claim is not None:
            data["pay_claim"] = pay_claim
        if as_funds_receipt is not None:
            data["as_funds_receipt"] = as_funds_receipt
        if as_tg_login_screenshot is not None:
            data["as_tg_login_screenshot"] = as_tg_login_screenshot
        if tags is not None:
            data["tags"] = tags
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            data["schedule_date"] = schedule_date
        if schedule_time is not None:
            data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            data["watch_thread_email"] = watch_thread_email
        if post_body is not None:
            data["post_body"] = post_body
        raw = await self._request("POST", path, json=data)
        return Threads_ClaimResponse.model_validate(raw)

    async def threads_get(
        self,
        thread_id: int,
        fields_include: list[str] | None = None,
    ) -> Threads_GetResponse:

        path = "/threads/{thread_id}"
        path = path.replace("{thread_id}", str(thread_id))
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return Threads_GetResponse.model_validate(raw)

    async def threads_edit(
        self,
        thread_id: int,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        discussion_open: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = None,
        comment_ignore_group: bool | None = None,
    ) -> Threads_EditResponse:

        path = "/threads/{thread_id}"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if prefix_id is not None:
            data["prefix_id"] = prefix_id
        if tags is not None:
            data["tags"] = tags
        if discussion_open is not None:
            data["discussion_open"] = discussion_open
        if hide_contacts is not None:
            data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            data["comment_ignore_group"] = comment_ignore_group
        raw = await self._request("PUT", path, json=data)
        return Threads_EditResponse.model_validate(raw)

    async def threads_delete(
        self,
        thread_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if reason is not None:
            data["reason"] = reason
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def threads_move(
        self,
        thread_id: int,
        node_id: str,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        apply_thread_prefix: bool | None = None,
        send_alert: bool | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/move"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if node_id is not None:
            data["node_id"] = node_id
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if prefix_id is not None:
            data["prefix_id"] = prefix_id
        if apply_thread_prefix is not None:
            data["apply_thread_prefix"] = apply_thread_prefix
        if send_alert is not None:
            data["send_alert"] = send_alert
        raw = await self._request("POST", path, json=data)
        return raw

    async def threads_bump(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/bump"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("POST", path)
        return raw

    async def threads_hide(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/hide"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("POST", path)
        return raw

    async def threads_star(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/star"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("POST", path)
        return raw

    async def threads_unstar(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/star"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("DELETE", path)
        return raw

    async def threads_followers(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/followers"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("GET", path)
        return raw

    async def threads_follow(
        self,
        thread_id: int,
        email: bool | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/followers"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if email is not None:
            data["email"] = email
        raw = await self._request("POST", path, json=data)
        return raw

    async def threads_unfollow(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/followers"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("DELETE", path)
        return raw

    async def threads_followed(
        self,
        total: bool | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/threads/followed"
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return raw

    async def threads_navigation(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/navigation"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("GET", path)
        return raw

    async def threads_poll_get(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/poll"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("GET", path)
        return raw

    async def threads_poll_vote(
        self,
        thread_id: int,
        response_id: int | None = None,
        response_ids: list[int] | None = None,
    ) -> dict[str, Any]:

        path = "/threads/{thread_id}/poll/votes"
        path = path.replace("{thread_id}", str(thread_id))
        data: dict[str, Any] = {}
        if response_id is not None:
            data["response_id"] = response_id
        if response_ids is not None:
            data["response_ids"] = response_ids
        raw = await self._request("POST", path, json=data)
        return raw

    async def threads_unread(
        self,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/threads/new"
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def threads_recent(
        self,
        days: int | None = None,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/threads/recent"
        params: dict[str, Any] = {}
        if days is not None:
            params["days"] = days
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def threads_finish(
        self,
        thread_id: int,
    ) -> dict[str, Any]:

        path = "/contests/{thread_id}/finish"
        path = path.replace("{thread_id}", str(thread_id))
        raw = await self._request("POST", path)
        return raw

    async def posts_list(
        self,
        thread_id: int | None = None,
        page_of_post_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: str | None = None,
    ) -> dict[str, Any]:

        path = "/posts"
        params: dict[str, Any] = {}
        if thread_id is not None:
            params["thread_id"] = thread_id
        if page_of_post_id is not None:
            params["page_of_post_id"] = page_of_post_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        raw = await self._request("GET", path, params=params)
        return raw

    async def posts_create(
        self,
        post_body: str,
        thread_id: int | None = None,
        quote_post_id: int | None = None,
    ) -> Posts_CreateResponse:

        path = "/posts"
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if thread_id is not None:
            data["thread_id"] = thread_id
        if quote_post_id is not None:
            data["quote_post_id"] = quote_post_id
        raw = await self._request("POST", path, json=data)
        return Posts_CreateResponse.model_validate(raw)

    async def posts_get(
        self,
        post_id: int,
    ) -> Posts_GetResponse:

        path = "/posts/{post_id}"
        path = path.replace("{post_id}", str(post_id))
        raw = await self._request("GET", path)
        return Posts_GetResponse.model_validate(raw)

    async def posts_edit(
        self,
        post_id: int,
        post_body: str | None = None,
    ) -> Posts_EditResponse:

        path = "/posts/{post_id}"
        path = path.replace("{post_id}", str(post_id))
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        raw = await self._request("PUT", path, json=data)
        return Posts_EditResponse.model_validate(raw)

    async def posts_delete(
        self,
        post_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}"
        path = path.replace("{post_id}", str(post_id))
        data: dict[str, Any] = {}
        if reason is not None:
            data["reason"] = reason
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def posts_likes(
        self,
        post_id: int,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/likes"
        path = path.replace("{post_id}", str(post_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def posts_like(
        self,
        post_id: int,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/likes"
        path = path.replace("{post_id}", str(post_id))
        raw = await self._request("POST", path)
        return raw

    async def posts_unlike(
        self,
        post_id: int,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/likes"
        path = path.replace("{post_id}", str(post_id))
        raw = await self._request("DELETE", path)
        return raw

    async def posts_report_reasons(
        self,
        post_id: int,
    ) -> Posts_ReportReasonsResponse:

        path = "/posts/{post_id}/report"
        path = path.replace("{post_id}", str(post_id))
        raw = await self._request("GET", path)
        return Posts_ReportReasonsResponse.model_validate(raw)

    async def posts_report(
        self,
        post_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/posts/{post_id}/report"
        path = path.replace("{post_id}", str(post_id))
        data: dict[str, Any] = {}
        if message is not None:
            data["message"] = message
        raw = await self._request("POST", path, json=data)
        return raw

    async def posts_comments_get(
        self,
        post_id: int,
        before: int | None = None,
        before_comment: int | None = None,
    ) -> dict[str, Any]:

        path = "/posts/comments"
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if before is not None:
            params["before"] = before
        if before_comment is not None:
            params["before_comment"] = before_comment
        raw = await self._request("GET", path, params=params)
        return raw

    async def posts_comments_create(
        self,
        post_id: int,
        comment_body: str,
    ) -> dict[str, Any]:

        path = "/posts/comments"
        data: dict[str, Any] = {}
        if post_id is not None:
            data["post_id"] = post_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = await self._request("POST", path, json=data)
        return raw

    async def posts_comments_edit(
        self,
        post_comment_id: int,
        comment_body: str,
    ) -> Posts_Comments_EditResponse:

        path = "/posts/comments"
        data: dict[str, Any] = {}
        if post_comment_id is not None:
            data["post_comment_id"] = post_comment_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = await self._request("PUT", path, json=data)
        return Posts_Comments_EditResponse.model_validate(raw)

    async def posts_comments_delete(
        self,
        post_comment_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/posts/comments"
        data: dict[str, Any] = {}
        if post_comment_id is not None:
            data["post_comment_id"] = post_comment_id
        if reason is not None:
            data["reason"] = reason
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def posts_comments_report(
        self,
        post_comment_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/posts/comments/report"
        data: dict[str, Any] = {}
        if post_comment_id is not None:
            data["post_comment_id"] = post_comment_id
        if message is not None:
            data["message"] = message
        raw = await self._request("POST", path, json=data)
        return raw

    async def users_list(
        self,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[str] | None = None,
    ) -> Users_ListResponse:

        path = "/users"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return Users_ListResponse.model_validate(raw)

    async def users_fields(
        self,
    ) -> dict[str, Any]:

        path = "/users/fields"
        raw = await self._request("GET", path)
        return raw

    async def users_find(
        self,
        username: str | None = None,
        custom_fields: dict[str, Any] | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/users/find"
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if custom_fields is not None:
            params["custom_fields"] = custom_fields
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return raw

    async def users_get(
        self,
        user_id: UserIDModel,
        fields_include: list[str] | None = None,
    ) -> Users_GetResponse:

        path = "/users/{user_id}"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return Users_GetResponse.model_validate(raw)

    async def users_edit(
        self,
        user_id: UserIDModel,
        username: str | None = None,
        user_title: str | None = None,
        display_group_id: int | None = None,
        display_icon_group_id: int | None = None,
        display_banner_id: int | None = None,
        conv_welcome_message: str | None = None,
        user_dob_day: int | None = None,
        user_dob_month: int | None = None,
        user_dob_year: int | None = None,
        secret_answer: str | None = None,
        secret_answer_type: int | None = None,
        short_link: str | None = None,
        language_id: int | None = None,
        gender: str | None = None,
        timezone: str | None = None,
        receive_admin_email: bool | None = None,
        activity_visible: bool | None = None,
        show_dob_date: bool | None = None,
        show_dob_year: bool | None = None,
        hide_username_change_logs: bool | None = None,
        allow_view_profile: str | None = None,
        allow_post_profile: str | None = None,
        allow_send_personal_conversation: str | None = None,
        allow_invite_group: str | None = None,
        allow_receive_news_feed: str | None = None,
        alert: dict[str, Any] | None = None,
        fields: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if username is not None:
            data["username"] = username
        if user_title is not None:
            data["user_title"] = user_title
        if display_group_id is not None:
            data["display_group_id"] = display_group_id
        if display_icon_group_id is not None:
            data["display_icon_group_id"] = display_icon_group_id
        if display_banner_id is not None:
            data["display_banner_id"] = display_banner_id
        if conv_welcome_message is not None:
            data["conv_welcome_message"] = conv_welcome_message
        if user_dob_day is not None:
            data["user_dob_day"] = user_dob_day
        if user_dob_month is not None:
            data["user_dob_month"] = user_dob_month
        if user_dob_year is not None:
            data["user_dob_year"] = user_dob_year
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        if secret_answer_type is not None:
            data["secret_answer_type"] = secret_answer_type
        if short_link is not None:
            data["short_link"] = short_link
        if language_id is not None:
            data["language_id"] = language_id
        if gender is not None:
            data["gender"] = gender
        if timezone is not None:
            data["timezone"] = timezone
        if receive_admin_email is not None:
            data["receive_admin_email"] = receive_admin_email
        if activity_visible is not None:
            data["activity_visible"] = activity_visible
        if show_dob_date is not None:
            data["show_dob_date"] = show_dob_date
        if show_dob_year is not None:
            data["show_dob_year"] = show_dob_year
        if hide_username_change_logs is not None:
            data["hide_username_change_logs"] = hide_username_change_logs
        if allow_view_profile is not None:
            data["allow_view_profile"] = allow_view_profile
        if allow_post_profile is not None:
            data["allow_post_profile"] = allow_post_profile
        if allow_send_personal_conversation is not None:
            data["allow_send_personal_conversation"] = allow_send_personal_conversation
        if allow_invite_group is not None:
            data["allow_invite_group"] = allow_invite_group
        if allow_receive_news_feed is not None:
            data["allow_receive_news_feed"] = allow_receive_news_feed
        if alert is not None:
            data["alert"] = alert
        if fields is not None:
            data["fields"] = fields
        raw = await self._request("PUT", path, json=data)
        return raw

    async def users_claims(
        self,
        user_id: UserIDModel,
        type_: str | None = None,
        claim_state: str | None = None,
    ) -> Users_ClaimsResponse:

        path = "/users/{user_id}/claims"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if claim_state is not None:
            params["claim_state"] = claim_state
        raw = await self._request("GET", path, params=params)
        return Users_ClaimsResponse.model_validate(raw)

    async def users_avatar_upload(
        self,
        user_id: UserIDModel,
        avatar: BinaryIO,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/avatar"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if avatar is not None:
            files["avatar"] = avatar
        raw = await self._request("POST", path, data=data, files=files)
        return raw

    async def users_avatar_delete(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/avatar"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("DELETE", path)
        return raw

    async def users_avatar_crop(
        self,
        user_id: UserIDModel,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/avatar/crop"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        raw = await self._request("POST", path, json=data)
        return raw

    async def users_background_upload(
        self,
        user_id: UserIDModel,
        background: BinaryIO,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/background"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if background is not None:
            files["background"] = background
        raw = await self._request("POST", path, data=data, files=files)
        return raw

    async def users_background_delete(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/background"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("DELETE", path)
        return raw

    async def users_background_crop(
        self,
        user_id: UserIDModel,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/background/crop"
        path = path.replace("{user_id}", str(user_id))
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        raw = await self._request("POST", path, json=data)
        return raw

    async def users_followers(
        self,
        user_id: UserIDModel,
        order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followers"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def users_follow(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followers"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("POST", path)
        return raw

    async def users_unfollow(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followers"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("DELETE", path)
        return raw

    async def users_followings(
        self,
        user_id: UserIDModel,
        order: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/followings"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def users_likes(
        self,
        user_id: UserIDModel,
        node_id: int | None = None,
        like_type: str | None = None,
        type_: str | None = "gotten",
        page: int | None = None,
        content_type: str | None = "post",
        search_user_id: int | None = None,
        stats: bool | None = None,
    ) -> Users_LikesResponse:

        path = "/users/{user_id}/likes"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if node_id is not None:
            params["node_id"] = node_id
        if like_type is not None:
            params["like_type"] = like_type
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if content_type is not None:
            params["content_type"] = content_type
        if search_user_id is not None:
            params["search_user_id"] = search_user_id
        if stats is not None:
            params["stats"] = stats
        raw = await self._request("GET", path, params=params)
        return Users_LikesResponse.model_validate(raw)

    async def users_ignored(
        self,
        total: bool | None = None,
    ) -> Users_IgnoredResponse:

        path = "/users/ignored"
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        raw = await self._request("GET", path, params=params)
        return Users_IgnoredResponse.model_validate(raw)

    async def users_ignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/ignore"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("POST", path)
        return raw

    async def users_ignore_edit(
        self,
        user_id: UserIDModel,
        ignore_conversations: bool | None = None,
        ignore_content: bool | None = None,
        restrict_view_profile: bool | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/ignore"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if ignore_conversations is not None:
            params["ignore_conversations"] = ignore_conversations
        if ignore_content is not None:
            params["ignore_content"] = ignore_content
        if restrict_view_profile is not None:
            params["restrict_view_profile"] = restrict_view_profile
        raw = await self._request("PUT", path, params=params)
        return raw

    async def users_unignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/ignore"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("DELETE", path)
        return raw

    async def users_contents(
        self,
        user_id: UserIDModel,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/timeline"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def users_trophies(
        self,
        user_id: UserIDModel,
    ) -> Users_TrophiesResponse:

        path = "/users/{user_id}/trophies"
        path = path.replace("{user_id}", str(user_id))
        raw = await self._request("GET", path)
        return Users_TrophiesResponse.model_validate(raw)

    async def users_secret_answer_types(
        self,
    ) -> Users_SecretAnswerTypesResponse:

        path = "/users/secret-answer/types"
        raw = await self._request("GET", path)
        return Users_SecretAnswerTypesResponse.model_validate(raw)

    async def users_sa_reset(
        self,
    ) -> Users_SA_ResetResponse:

        path = "/account/secret-answer/reset"
        raw = await self._request("POST", path)
        return Users_SA_ResetResponse.model_validate(raw)

    async def users_sa_cancel_reset(
        self,
    ) -> dict[str, Any]:

        path = "/account/secret-answer/reset"
        raw = await self._request("DELETE", path)
        return raw

    async def profile_posts_list(
        self,
        user_id: UserIDModel,
        posts_user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:

        path = "/users/{user_id}/profile-posts"
        path = path.replace("{user_id}", str(user_id))
        params: dict[str, Any] = {}
        if posts_user_id is not None:
            params["posts_user_id"] = posts_user_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        raw = await self._request("GET", path, params=params)
        return raw

    async def profile_posts_get(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("GET", path)
        return raw

    async def profile_posts_edit(
        self,
        profile_post_id: int,
        post_body: str | None = None,
        disable_comments: bool | None = None,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        data: dict[str, Any] = {}
        if post_body is not None:
            data["post_body"] = post_body
        if disable_comments is not None:
            data["disable_comments"] = disable_comments
        raw = await self._request("PUT", path, json=data)
        return raw

    async def profile_posts_delete(
        self,
        profile_post_id: int,
        reason: str | None = None,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        params: dict[str, Any] = {}
        if reason is not None:
            params["reason"] = reason
        raw = await self._request("DELETE", path, params=params)
        return raw

    async def profile_posts_report_reasons(
        self,
        profile_post_id: int,
    ) -> ProfilePosts_ReportReasonsResponse:

        path = "/profile-posts/{profile_post_id}/report"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("GET", path)
        return ProfilePosts_ReportReasonsResponse.model_validate(raw)

    async def profile_posts_report(
        self,
        profile_post_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/report"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        data: dict[str, Any] = {}
        if message is not None:
            data["message"] = message
        raw = await self._request("POST", path, json=data)
        return raw

    async def profile_posts_create(
        self,
        user_id: UserIDModel,
        post_body: str,
    ) -> dict[str, Any]:

        path = "/profile-posts"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        if post_body is not None:
            data["post_body"] = post_body
        raw = await self._request("POST", path, json=data)
        return raw

    async def profile_posts_stick(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/stick"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("POST", path)
        return raw

    async def profile_posts_unstick(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/stick"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("DELETE", path)
        return raw

    async def profile_posts_likes(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/likes"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("GET", path)
        return raw

    async def profile_posts_like(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/likes"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("POST", path)
        return raw

    async def profile_posts_unlike(
        self,
        profile_post_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/likes"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        raw = await self._request("DELETE", path)
        return raw

    async def profile_posts_comments_list(
        self,
        profile_post_id: int,
        before: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments"
        params: dict[str, Any] = {}
        if profile_post_id is not None:
            params["profile_post_id"] = profile_post_id
        if before is not None:
            params["before"] = before
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def profile_posts_comments_create(
        self,
        profile_post_id: int,
        comment_body: str,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments"
        data: dict[str, Any] = {}
        if profile_post_id is not None:
            data["profile_post_id"] = profile_post_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = await self._request("POST", path, json=data)
        return raw

    async def profile_posts_comments_edit(
        self,
        comment_id: int,
        comment_body: str,
    ) -> ProfilePosts_Comments_EditResponse:

        path = "/profile-posts/comments"
        data: dict[str, Any] = {}
        if comment_id is not None:
            data["comment_id"] = comment_id
        if comment_body is not None:
            data["comment_body"] = comment_body
        raw = await self._request("PUT", path, json=data)
        return ProfilePosts_Comments_EditResponse.model_validate(raw)

    async def profile_posts_comments_delete(
        self,
        comment_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments"
        data: dict[str, Any] = {}
        if comment_id is not None:
            data["comment_id"] = comment_id
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def profile_posts_comments_get(
        self,
        profile_post_id: int,
        comment_id: int,
    ) -> dict[str, Any]:

        path = "/profile-posts/{profile_post_id}/comments/{comment_id}"
        path = path.replace("{profile_post_id}", str(profile_post_id))
        path = path.replace("{comment_id}", str(comment_id))
        raw = await self._request("GET", path)
        return raw

    async def profile_posts_comments_report(
        self,
        comment_id: int,
        message: str,
    ) -> dict[str, Any]:

        path = "/profile-posts/comments/{comment_id}/report"
        path = path.replace("{comment_id}", str(comment_id))
        data: dict[str, Any] = {}
        if message is not None:
            data["message"] = message
        raw = await self._request("POST", path, json=data)
        return raw

    async def conversations_list(
        self,
        folder: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Conversations_ListResponse:

        path = "/conversations"
        params: dict[str, Any] = {}
        if folder is not None:
            params["folder"] = folder
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return Conversations_ListResponse.model_validate(raw)

    async def conversations_create(
        self,
        recipient_id: int | None = None,
        recipients: list[str] | None = None,
        is_group: bool | None = False,
        title: str | None = None,
        open_invite: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
        message_body: str | None = None,
    ) -> Conversations_CreateResponse:

        path = "/conversations"
        data: dict[str, Any] = {}
        if recipient_id is not None:
            data["recipient_id"] = recipient_id
        if recipients is not None:
            data["recipients"] = recipients
        if is_group is not None:
            data["is_group"] = is_group
        if title is not None:
            data["title"] = title
        if open_invite is not None:
            data["open_invite"] = open_invite
        if allow_edit_messages is not None:
            data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            data["allow_delete_own_messages"] = allow_delete_own_messages
        if message_body is not None:
            data["message_body"] = message_body
        raw = await self._request("POST", path, json=data)
        return Conversations_CreateResponse.model_validate(raw)

    async def conversations_update(
        self,
        conversation_id: int,
        title: str | None = None,
        open_invite: bool | None = None,
        history_open: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
    ) -> dict[str, Any]:

        path = "/conversations"
        data: dict[str, Any] = {}
        if conversation_id is not None:
            data["conversation_id"] = conversation_id
        if title is not None:
            data["title"] = title
        if open_invite is not None:
            data["open_invite"] = open_invite
        if history_open is not None:
            data["history_open"] = history_open
        if allow_edit_messages is not None:
            data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            data["allow_delete_own_messages"] = allow_delete_own_messages
        raw = await self._request("PUT", path, json=data)
        return raw

    async def conversations_delete(
        self,
        conversation_id: int,
        delete_type: str,
    ) -> dict[str, Any]:

        path = "/conversations"
        data: dict[str, Any] = {}
        if conversation_id is not None:
            data["conversation_id"] = conversation_id
        if delete_type is not None:
            data["delete_type"] = delete_type
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def conversations_start(
        self,
        user_id: UserIDModel,
    ) -> Conversations_StartResponse:

        path = "/conversations/start"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = await self._request("POST", path, json=data)
        return Conversations_StartResponse.model_validate(raw)

    async def conversations_save(
        self,
        link: str,
    ) -> dict[str, Any]:

        path = "/conversations/save"
        data: dict[str, Any] = {}
        if link is not None:
            data["link"] = link
        raw = await self._request("POST", path, json=data)
        return raw

    async def conversations_get(
        self,
        conversation_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = await self._request("GET", path)
        return raw

    async def conversations_messages_list(
        self,
        conversation_id: int,
        page: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        before: int | None = None,
        after: int | None = None,
    ) -> Conversations_Messages_ListResponse:

        path = "/conversations/{conversation_id}/messages"
        path = path.replace("{conversation_id}", str(conversation_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        raw = await self._request("GET", path, params=params)
        return Conversations_Messages_ListResponse.model_validate(raw)

    async def conversations_messages_create(
        self,
        conversation_id: int,
        message_body: str,
        reply_message_id: int | None = None,
    ) -> Conversations_Messages_CreateResponse:

        path = "/conversations/{conversation_id}/messages"
        path = path.replace("{conversation_id}", str(conversation_id))
        data: dict[str, Any] = {}
        if reply_message_id is not None:
            data["reply_message_id"] = reply_message_id
        if message_body is not None:
            data["message_body"] = message_body
        raw = await self._request("POST", path, json=data)
        return Conversations_Messages_CreateResponse.model_validate(raw)

    async def conversations_search(
        self,
        q: str | None = None,
        conversation_id: int | None = None,
        search_recipients: bool | None = None,
    ) -> Conversations_SearchResponse:

        path = "/conversations/search"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if conversation_id is not None:
            data["conversation_id"] = conversation_id
        if search_recipients is not None:
            data["search_recipients"] = search_recipients
        raw = await self._request("POST", path, json=data)
        return Conversations_SearchResponse.model_validate(raw)

    async def conversations_messages_get(
        self,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/messages/{message_id}"
        path = path.replace("{message_id}", str(message_id))
        raw = await self._request("GET", path)
        return raw

    async def conversations_messages_edit(
        self,
        conversation_id: int,
        message_id: int,
        message_body: str,
    ) -> Conversations_Messages_EditResponse:

        path = "/conversations/{conversation_id}/messages/{message_id}"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        data: dict[str, Any] = {}
        if message_body is not None:
            data["message_body"] = message_body
        raw = await self._request("PUT", path, json=data)
        return Conversations_Messages_EditResponse.model_validate(raw)

    async def conversations_messages_delete(
        self,
        conversation_id: int,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/messages/{message_id}"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        raw = await self._request("DELETE", path)
        return raw

    async def conversations_invite(
        self,
        conversation_id: int,
        recipients: list[str],
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/invite"
        path = path.replace("{conversation_id}", str(conversation_id))
        data: dict[str, Any] = {}
        if recipients is not None:
            data["recipients"] = recipients
        raw = await self._request("POST", path, json=data)
        return raw

    async def conversations_kick(
        self,
        conversation_id: int,
        user_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/kick"
        path = path.replace("{conversation_id}", str(conversation_id))
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = await self._request("POST", path, json=data)
        return raw

    async def conversations_read(
        self,
        conversation_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/read"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = await self._request("POST", path)
        return raw

    async def conversations_read_all(
        self,
    ) -> Conversations_ReadAllResponse:

        path = "/conversations/read-all"
        raw = await self._request("POST", path)
        return Conversations_ReadAllResponse.model_validate(raw)

    async def conversations_messages_stick(
        self,
        conversation_id: int,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/messages/{message_id}/stick"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        raw = await self._request("POST", path)
        return raw

    async def conversations_messages_unstick(
        self,
        conversation_id: int,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/conversations/{conversation_id}/messages/{message_id}/stick"
        path = path.replace("{conversation_id}", str(conversation_id))
        path = path.replace("{message_id}", str(message_id))
        raw = await self._request("DELETE", path)
        return raw

    async def conversations_star(
        self,
        conversation_id: int,
    ) -> Conversations_StarResponse:

        path = "/conversations/{conversation_id}/star"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = await self._request("POST", path)
        return Conversations_StarResponse.model_validate(raw)

    async def conversations_unstar(
        self,
        conversation_id: int,
    ) -> Conversations_UnstarResponse:

        path = "/conversations/{conversation_id}/star"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = await self._request("DELETE", path)
        return Conversations_UnstarResponse.model_validate(raw)

    async def conversations_alerts_enable(
        self,
        conversation_id: int,
    ) -> Conversations_Alerts_EnableResponse:

        path = "/conversations/{conversation_id}/alerts"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = await self._request("POST", path)
        return Conversations_Alerts_EnableResponse.model_validate(raw)

    async def conversations_alerts_disable(
        self,
        conversation_id: int,
    ) -> Conversations_Alerts_DisableResponse:

        path = "/conversations/{conversation_id}/alerts"
        path = path.replace("{conversation_id}", str(conversation_id))
        raw = await self._request("DELETE", path)
        return Conversations_Alerts_DisableResponse.model_validate(raw)

    async def notifications_list(
        self,
        type_: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/notifications"
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def notifications_get(
        self,
        notification_id: int,
    ) -> dict[str, Any]:

        path = "/notifications/{notification_id}/content"
        path = path.replace("{notification_id}", str(notification_id))
        raw = await self._request("GET", path)
        return raw

    async def notifications_read(
        self,
        notification_id: int | None = None,
    ) -> dict[str, Any]:

        path = "/notifications/read"
        data: dict[str, Any] = {}
        if notification_id is not None:
            data["notification_id"] = notification_id
        raw = await self._request("POST", path, json=data)
        return raw

    async def tags_popular(
        self,
    ) -> dict[str, Any]:

        path = "/tags"
        raw = await self._request("GET", path)
        return raw

    async def tags_list(
        self,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/tags/list"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def tags_get(
        self,
        tag_id: int,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/tags/{tag_id}"
        path = path.replace("{tag_id}", str(tag_id))
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        raw = await self._request("GET", path, params=params)
        return raw

    async def tags_find(
        self,
        tag: str,
    ) -> dict[str, Any]:

        path = "/tags/find"
        params: dict[str, Any] = {}
        if tag is not None:
            params["tag"] = tag
        raw = await self._request("GET", path, params=params)
        return raw

    async def search_all(
        self,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: UserIDModel | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Search_AllResponse:

        path = "/search"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if tag is not None:
            data["tag"] = tag
        if forum_id is not None:
            data["forum_id"] = forum_id
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = await self._request("POST", path, json=data)
        return Search_AllResponse.model_validate(raw)

    async def search_threads(
        self,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: UserIDModel | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/threads"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if tag is not None:
            data["tag"] = tag
        if forum_id is not None:
            data["forum_id"] = forum_id
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        if data_limit is not None:
            data["data_limit"] = data_limit
        raw = await self._request("POST", path, json=data)
        return raw

    async def search_posts(
        self,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: UserIDModel | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/posts"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if tag is not None:
            data["tag"] = tag
        if forum_id is not None:
            data["forum_id"] = forum_id
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        if data_limit is not None:
            data["data_limit"] = data_limit
        raw = await self._request("POST", path, json=data)
        return raw

    async def search_users(
        self,
        q: str | None = None,
    ) -> Search_UsersResponse:

        path = "/search/users"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        raw = await self._request("POST", path, json=data)
        return Search_UsersResponse.model_validate(raw)

    async def search_profile_posts(
        self,
        q: str | None = None,
        user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/profile-posts"
        data: dict[str, Any] = {}
        if q is not None:
            data["q"] = q
        if user_id is not None:
            data["user_id"] = user_id
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = await self._request("POST", path, json=data)
        return raw

    async def search_tagged(
        self,
        tag: str | None = None,
        tags: list[str] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/tagged"
        data: dict[str, Any] = {}
        if tag is not None:
            data["tag"] = tag
        if tags is not None:
            data["tags"] = tags
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = await self._request("POST", path, json=data)
        return raw

    async def search_results(
        self,
        search_id: str,
        page: int | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:

        path = "/search/{search_id}/results"
        path = path.replace("{search_id}", str(search_id))
        data: dict[str, Any] = {}
        if page is not None:
            data["page"] = page
        if limit is not None:
            data["limit"] = limit
        raw = await self._request("GET", path, json=data)
        return raw

    async def batch_execute(
        self,
    ) -> Batch_ExecuteResponse:

        path = "/batch"
        raw = await self._request("POST", path)
        return Batch_ExecuteResponse.model_validate(raw)

    async def chatbox_index(
        self,
        room_id: RoomIDModel | None = None,
    ) -> Chatbox_IndexResponse:

        path = "/chatbox"
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        raw = await self._request("GET", path, params=params)
        return Chatbox_IndexResponse.model_validate(raw)

    async def chatbox_get_messages(
        self,
        room_id: RoomIDModel,
        before_message_id: int | None = None,
    ) -> Chatbox_GetMessagesResponse:

        path = "/chatbox/messages"
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        if before_message_id is not None:
            params["before_message_id"] = before_message_id
        raw = await self._request("GET", path, params=params)
        return Chatbox_GetMessagesResponse.model_validate(raw)

    async def chatbox_post_message(
        self,
        room_id: RoomIDModel,
        message: str,
        reply_message_id: int | None = None,
    ) -> Chatbox_PostMessageResponse:

        path = "/chatbox/messages"
        data: dict[str, Any] = {}
        if room_id is not None:
            data["room_id"] = room_id
        if reply_message_id is not None:
            data["reply_message_id"] = reply_message_id
        if message is not None:
            data["message"] = message
        raw = await self._request("POST", path, json=data)
        return Chatbox_PostMessageResponse.model_validate(raw)

    async def chatbox_edit_message(
        self,
        message_id: int,
        message: str,
    ) -> Chatbox_EditMessageResponse:

        path = "/chatbox/messages"
        data: dict[str, Any] = {}
        if message_id is not None:
            data["message_id"] = message_id
        if message is not None:
            data["message"] = message
        raw = await self._request("PUT", path, json=data)
        return Chatbox_EditMessageResponse.model_validate(raw)

    async def chatbox_delete_message(
        self,
        message_id: int,
    ) -> dict[str, Any]:

        path = "/chatbox/messages"
        data: dict[str, Any] = {}
        if message_id is not None:
            data["message_id"] = message_id
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def chatbox_online(
        self,
        room_id: RoomIDModel,
    ) -> Chatbox_OnlineResponse:

        path = "/chatbox/messages/online"
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        raw = await self._request("GET", path, params=params)
        return Chatbox_OnlineResponse.model_validate(raw)

    async def chatbox_report_reasons(
        self,
        message_id: int,
    ) -> Chatbox_ReportReasonsResponse:

        path = "/chatbox/messages/report"
        params: dict[str, Any] = {}
        if message_id is not None:
            params["message_id"] = message_id
        raw = await self._request("GET", path, params=params)
        return Chatbox_ReportReasonsResponse.model_validate(raw)

    async def chatbox_report(
        self,
        message_id: int,
        reason: str,
    ) -> dict[str, Any]:

        path = "/chatbox/messages/report"
        data: dict[str, Any] = {}
        if message_id is not None:
            data["message_id"] = message_id
        if reason is not None:
            data["reason"] = reason
        raw = await self._request("POST", path, json=data)
        return raw

    async def chatbox_get_leaderboard(
        self,
        duration: str | None = None,
    ) -> Chatbox_GetLeaderboardResponse:

        path = "/chatbox/messages/leaderboard"
        params: dict[str, Any] = {}
        if duration is not None:
            params["duration"] = duration
        raw = await self._request("GET", path, params=params)
        return Chatbox_GetLeaderboardResponse.model_validate(raw)

    async def chatbox_get_ignore(
        self,
    ) -> Chatbox_GetIgnoreResponse:

        path = "/chatbox/ignore"
        raw = await self._request("GET", path)
        return Chatbox_GetIgnoreResponse.model_validate(raw)

    async def chatbox_post_ignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/chatbox/ignore"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = await self._request("POST", path, json=data)
        return raw

    async def chatbox_delete_ignore(
        self,
        user_id: UserIDModel,
    ) -> dict[str, Any]:

        path = "/chatbox/ignore"
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        raw = await self._request("DELETE", path, json=data)
        return raw

    async def forms_list(
        self,
        page: int | None = None,
    ) -> Forms_ListResponse:

        path = "/forms"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        raw = await self._request("GET", path, params=params)
        return Forms_ListResponse.model_validate(raw)

    async def forms_create(
        self,
    ) -> Forms_CreateResponse:

        path = "/forms/save"
        raw = await self._request("POST", path)
        return Forms_CreateResponse.model_validate(raw)

