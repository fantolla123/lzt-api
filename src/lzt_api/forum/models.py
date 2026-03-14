from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class Resp_NotificationModel(BaseModel):
    notification_id: int
    notification_create_date: int
    content_type: str
    content_id: int
    content_action: str
    notification_is_unread: bool
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    notification_type: str
    links: dict[str, Any]
    notification_html: str

    model_config = {"populate_by_name": True}


class Resp_LinkModel(BaseModel):
    link_id: int
    link_title: str
    link_description: str
    links: dict[str, Any]
    permissions: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_ChatboxMessageModel(BaseModel):
    can_report: bool
    date: int
    is_deleted: bool
    message: str
    message_id: int
    messageJson: str
    messageRaw: str
    room: dict[str, Any]
    user: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_UserModel(BaseModel):
    user_id: int
    username: str
    username_html: str
    user_message_count: int
    user_register_date: int
    user_like_count: int
    user_like2_count: int
    contest_count: int
    trophy_count: int
    short_link: str
    custom_title: str
    is_banned: int
    display_banner_id: int
    display_icon_group_id: int
    balance: str
    hold: str
    currency: str
    user_email: str
    user_unread_notification_count: int
    user_unread_conversation_count: int
    conv_welcome_message: str
    user_title: str
    user_deposit: int
    user_is_valid: bool
    user_is_verified: bool
    user_is_followed: bool
    user_last_seen_date: int
    links: dict[str, Any]
    permissions: dict[str, Any]
    user_is_ignored: bool
    user_is_visitor: bool
    user_group_id: int
    curator_titles: list[str]
    user_groups: list[dict[str, Any]]
    fields: list[dict[str, Any]]
    user_timezone_offset: int
    user_external_authentications: list[dict[str, Any]]
    self_permissions: dict[str, Any]
    edit_permissions: dict[str, Any]
    birthday: dict[str, Any]
    secret_answer_rendered: str
    secret_answer_first_letter: str
    user_following: dict[str, Any]
    user_followers: dict[str, Any]
    banner: str

    model_config = {"populate_by_name": True}


class Resp_ThreadModel(BaseModel):
    thread_id: int
    forum_id: int
    thread_title: str
    thread_view_count: int
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    thread_create_date: int
    thread_update_date: int
    user_is_ignored: bool
    thread_post_count: int
    thread_is_published: bool
    thread_is_deleted: bool
    thread_is_sticky: bool
    thread_is_closed: bool
    thread_is_followed: bool
    thread_is_starred: bool
    first_post: dict[str, Any]
    thread_prefixes: list[Any]
    thread_tags: dict[str, Any]
    links: dict[str, Any]
    permissions: dict[str, Any]
    node_title: str
    restrictions: dict[str, Any]
    last_post: dict[str, Any]
    contest: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_PostModel(BaseModel):
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_body_html: str
    post_body_plain_text: str
    signature: str
    signature_html: str
    signature_plain_text: str
    post_like_count: int
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_update_date: int
    post_is_first_post: bool
    links: dict[str, Any]
    permissions: dict[str, Any]
    thread_is_deleted: bool

    model_config = {"populate_by_name": True}


class Resp_PostCommentModel(BaseModel):
    post_comment_id: int
    post_id: int
    thread_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_comment_create_date: int
    post_comment_body: str
    post_comment_body_html: str
    post_comment_body_plain_text: str
    post_comment_like_count: int
    user_is_ignored: bool
    post_comment_is_published: bool
    post_comment_is_deleted: bool
    post_comment_update_date: int
    links: dict[str, Any]
    permissions: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_ProfilePostModel(BaseModel):
    profile_post_id: int
    timeline_user_id: int
    poster_user_id: int
    poster_username: str
    poster_username_html: str
    post_create_date: int
    post_body: str
    post_body_html: str
    post_body_plain_text: str
    post_like_count: int
    post_comment_count: int
    post_comments_is_disabled: int
    timeline_username: str
    user_is_ignored: bool
    post_is_published: bool
    post_is_deleted: bool
    post_is_liked: bool
    post_is_sticked: bool
    links: dict[str, Any]
    permissions: dict[str, Any]
    timeline_user: Resp_UserModel

    model_config = {"populate_by_name": True}


class Resp_ProfilePostCommentModel(BaseModel):
    comment_id: int
    profile_post_id: int
    comment_user_id: int
    comment_username: str
    comment_username_html: str
    comment_create_date: int
    comment_body: str
    comment_body_html: str
    comment_body_plain_text: str
    user_is_ignored: bool
    timeline_user_id: int
    links: dict[str, Any]
    permissions: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_ConversationModel(BaseModel):
    conversation_id: int
    conversation_title: str
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    conversation_create_date: int
    conversation_update_date: int
    conversation_last_read_date: int
    conversation_online_count: int
    is_starred: int
    is_group: int
    is_unread: int
    alerts: int
    permissions: dict[str, Any]
    conversation_message_count: int
    conversation_is_new: bool
    creator_is_ignored: bool
    conversation_is_open: bool
    conversation_is_deleted: bool
    recipient: dict[str, Any]
    recipients: list[dict[str, Any]]
    links: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_ConversationMessageModel(BaseModel):
    message_id: int
    conversation_id: int
    creator_user_id: int
    creator_username: str
    creator_username_html: str
    message_create_date: int
    message_is_unread: int
    message_need_translate: bool
    message_is_system: bool
    message_edit_date: int
    message_body: str
    message_body_html: str
    message_body_plain_text: str
    user_is_ignored: bool
    links: dict[str, Any]
    permissions: dict[str, Any]

    model_config = {"populate_by_name": True}


class Resp_SystemInfo(BaseModel):
    visitor_id: int
    time: int

    model_config = {"populate_by_name": True}

