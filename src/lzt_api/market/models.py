from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class DiscountModel(BaseModel):
    category_id: int
    discount_id: int
    discount_percent: int
    discount_user_id: int
    max_price: int
    min_price: int
    user_id: int

    model_config = {"populate_by_name": True}


class UserModel(BaseModel):
    active_items_count: int
    activity_visible: bool
    age: int
    balance: str
    balances: list[dict[str, Any]]
    bump_item_period: int
    can_edit: bool
    can_follow: bool
    can_ignore: bool
    can_post_profile: bool
    can_view_profile: bool
    can_view_profile_posts: bool
    can_warn: bool
    contest_count: int
    conv_welcome_message: str
    convertedBalance: int
    convertedDeposit: int
    convertedHold: int
    currency: str
    currencyPhrase: str
    custom_account_download_format: str
    custom_fields: dict[str, Any]
    custom_title: str
    deposit: int
    dob: dict[str, Any]
    feedback_data: dict[str, Any]
    hold: str
    homepage: str
    imap_data: dict[str, Any]
    is_admin: bool
    is_banned: bool
    is_followed: bool
    is_ignored: bool
    is_moderator: bool
    is_staff: bool
    is_super_admin: bool
    joined_date: int
    last_activity: int
    like2_count: int
    like_count: int
    location: str
    market_custom_title: str
    max_discount_percent: int
    message_count: int
    paid_mail_left: int
    public_tags: list[dict[str, Any]]
    register_date: int
    rendered: dict[str, Any]
    restore_count: int
    restore_data: dict[str, Any]
    short_link: str
    sold_items_count: int
    tags: list[dict[str, Any]]
    telegram_client: dict[str, Any]
    trophy_points: int
    user_allow_ask_discount: bool
    user_id: int
    user_title: str
    username: str
    view_url: str
    visible: bool
    warning_points: int

    model_config = {"populate_by_name": True}


class BalanceModel(BaseModel):
    balance: str
    balance_id: int
    custom_title: Any
    fullTitle: str
    merchant_id: int
    title: str
    type_: str = Field(alias="type")
    user_id: int

    model_config = {"populate_by_name": True}


class ExtraModel(BaseModel):
    proxy: str | None = None
    close_item: bool | None = None
    region: str | None = None
    service: str | None = None
    system: str | None = None
    confirmationCode: str | None = None
    cookies: str | None = None
    login_without_cookies: bool | None = None
    cookie_login: bool | None = None
    mfa_file: str | None = None
    dota2_mmr: int | None = None
    ea_games: bool | None = None
    uplay_games: bool | None = None
    the_quarry: bool | None = None
    warframe: bool | None = None
    ark: bool | None = None
    ark_ascended: bool | None = None
    genshin_currency: int | None = None
    honkai_currency: int | None = None
    zenless_currency: int | None = None
    password: str | None = None
    telegramClient: str | None = None
    telegramJson: str | None = None
    checkChannels: bool | None = None
    checkSpam: bool | None = None
    checkHypixelBan: bool | None = None

    model_config = {"populate_by_name": True}


class ConfirmationCodeModel(BaseModel):
    item: ItemModel
    codeData: dict[str, Any]

    model_config = {"populate_by_name": True}


class ItemListModel(BaseModel):
    items: list[ItemFromListModel]
    totalItems: int
    totalItemsPrice: Any
    hasNextPage: bool
    perPage: int
    page: int
    searchUrl: str
    stickyItems: list[ItemFromListModel]
    system_info: Resp_SystemInfo

    model_config = {"populate_by_name": True}


class ItemFromListModel(BaseModel):
    item_id: int | None = 0
    item_state: str | None = "active"
    category_id: int | None = 0
    published_date: int | None = 0
    title: str | None = "Title"
    description: str | None = "Description"
    price: int | None = 0
    update_stat_date: int | None = 0
    refreshed_date: int | None = 0
    view_count: int | None = 0
    is_sticky: int | None = 0
    item_origin: str | None = "string"
    extended_guarantee: int | None = 0
    nsb: int | None = 0
    allow_ask_discount: int | None = 0
    title_en: str | None = "Title EN"
    description_en: str | None = "Description EN"
    item_domain: str | None = "string"
    resale_item_origin: str | None = "string"
    isIgnored: int | None = 0
    guarantee: bool | None = None
    canViewLoginData: bool | None = False
    canUpdateItemStats: bool | None = False
    canViewEmailLoginData: bool | None = False
    showGetEmailCodeButton: bool | None = False
    canOpenItem: bool | None = False
    canCloseItem: bool | None = False
    canEditItem: bool | None = False
    canDeleteItem: bool | None = False
    canStickItem: bool | None = False
    canUnstickItem: bool | None = False
    bumpSettings: dict[str, Any] | None = None
    canBumpItem: bool | None = False
    canBuyItem: bool | None = False
    rub_price: int | None = 0
    price_currency: str | None = "rub"
    canValidateAccount: bool | None = False
    canResellItemAfterPurchase: bool | None = False
    canViewAccountLink: bool | None = False
    itemOriginPhrase: str | None = "string"
    tags: list[str] | None = None
    note_text: str | None = None
    description_html: str | None = "Description HTML"
    description_html_en: str | None = "Description HTML EN"
    seller: dict[str, Any] | None = None

    model_config = {"populate_by_name": True}


class ItemModel(BaseModel):
    item_id: int
    item_state: str
    category_id: int
    published_date: int
    title: str
    description: str
    price: int
    update_stat_date: int
    refreshed_date: int
    edit_date: int
    pending_deletion_date: int
    login: str
    temp_email: str
    view_count: int
    is_sticky: int
    information: str
    item_origin: str
    extended_guarantee: int
    nsb: int
    allow_ask_discount: int
    title_en: str
    description_en: str
    information_en: str
    email_type: str
    email_provider: str
    item_domain: str
    resale_item_origin: str
    note_text: str
    content_type: Any
    content_id: Any
    delete_date: int
    delete_user_id: int
    delete_username: str
    delete_reason: str
    user_allow_ask_discount: int
    max_discount_percent: int
    market_custom_title: str
    feedback_data: str
    buyer_display_icon_group_id: int
    buyer_uniq_banner: str
    buyer_avatar_date: int
    buyer_user_group_id: int
    is_fave: Any
    in_cart: Any
    cart_price: Any
    canResellItem: bool
    priceWithSellerFee: float
    guarantee: dict[str, Any]
    canViewLoginData: bool
    canUpdateItemStats: bool
    canReportItem: bool
    canViewItemViews: bool
    loginData: dict[str, Any]
    canViewEmailLoginData: bool
    copyFormatData: dict[str, Any]
    showGetEmailCodeButton: bool
    getEmailCodeDisplayLogin: Any
    buyer: dict[str, Any]
    isPersonalAccount: bool
    rub_price: int
    price_currency: str
    priceWithSellerFeeLabel: str
    canValidateAccount: bool
    canResellItemAfterPurchase: bool
    isSmallExf: bool
    account_last_activity: int
    canViewAccountLink: bool
    accountLinks: list[dict[str, Any]]
    accountLink: str
    imagePreviewLinks: list[str]
    canChangePassword: bool
    canChangeEmailPassword: bool
    uniqueKeyExists: bool
    itemOriginPhrase: str
    visitorIsAuthor: bool
    canAskDiscount: bool
    tags: dict[str, Any]
    customFields: dict[str, Any]
    externalAuth: list[Any]
    isTrusted: bool
    isBirthdayToday: bool
    isIgnored: bool
    deposit: int
    extraPrices: list[dict[str, Any]]
    canViewAccountLoginAndTempEmail: bool
    bumpSettings: dict[str, Any]
    canCheckGuarantee: bool
    canShareItem: bool
    canCheckAiPrice: bool
    aiPrice: int
    aiPriceCheckDate: int
    needToRequireVideoToViewLoginData: bool
    canCheckAutoBuyPrice: bool
    autoBuyPrice: int
    autoBuyPriceCheckDate: int
    descriptionHtml: str
    descriptionEnHtml: str
    descriptionPlain: str
    descriptionEnPlain: str
    seller: dict[str, Any]

    model_config = {"populate_by_name": True}


class InvoiceModel(BaseModel):
    additional_data: str
    amount: int
    comment: str
    expires_at: int
    invoice_date: int
    invoice_id: int
    is_test: bool
    merchant_id: int
    paid_date: int
    payer_user_id: int
    payment_id: str
    resend_attempts: int
    status: str
    url: str
    url_callback: str
    url_success: str
    user_id: int

    model_config = {"populate_by_name": True}


class Resp_SystemInfo(BaseModel):
    visitor_id: int
    time: int
    log_id: int

    model_config = {"populate_by_name": True}

