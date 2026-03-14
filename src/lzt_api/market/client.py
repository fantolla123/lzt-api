from __future__ import annotations

from typing import Any

from lzt_api.client import BaseClient, AsyncBaseClient


class MarketClient(BaseClient):
    def __init__(self, token: str, base_url: str = "https://prod-api.lzt.market", proxy: str | None = None, timeout: float = 30.0):
        super().__init__(token=token, base_url=base_url, proxy=proxy, timeout=timeout)

    def category_all(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        return self._request("GET", path, params=params)

    def category_steam(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_type: list[str] | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        item_domain: str | None = None,
        game: list[int] | None = None,
        hours_played: dict[str, Any] | None = None,
        hours_played_max: dict[str, Any] | None = None,
        eg: int | None = None,
        vac: list[int] | None = None,
        vac_skip_game_check: bool | None = None,
        rt: str | None = "no",
        trade_ban: YesNoNoMatterScheme | None = None,
        trade_limit: YesNoNoMatterScheme | None = None,
        daybreak: int | None = None,
        limit: YesNoNoMatterScheme | None = None,
        mafile: YesNoNoMatterScheme | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        lmin: int | None = None,
        lmax: int | None = None,
        rmin: int | None = None,
        rmax: int | None = None,
        wingman_rmin: int | None = None,
        wingman_rmax: int | None = None,
        no_vac: bool | None = None,
        mm_ban: YesNoNoMatterScheme | None = None,
        balance_min: int | None = None,
        balance_max: int | None = None,
        inv_game: int | None = None,
        inv_min: float | None = None,
        inv_max: float | None = None,
        friends_min: int | None = None,
        friends_max: int | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        win_count_min: int | None = None,
        win_count_max: int | None = None,
        medal_id: list[int] | None = None,
        medal_operator_or: bool | None = None,
        medal_min: int | None = None,
        medal_max: int | None = None,
        gift: list[str] | None = None,
        gift_min: int | None = None,
        gift_max: int | None = None,
        recently_hours_min: int | None = None,
        recently_hours_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        cs2_profile_rank_min: int | None = None,
        cs2_profile_rank_max: int | None = None,
        solommr_min: int | None = None,
        solommr_max: int | None = None,
        d2_game_count_min: int | None = None,
        d2_game_count_max: int | None = None,
        d2_win_count_min: int | None = None,
        d2_win_count_max: int | None = None,
        d2_behavior_min: int | None = None,
        d2_behavior_max: int | None = None,
        faceit_lvl_min: int | None = None,
        faceit_lvl_max: int | None = None,
        points_min: int | None = None,
        points_max: int | None = None,
        relevant_gmin: int | None = None,
        relevant_gmax: int | None = None,
        last_trans_date: int | None = None,
        last_trans_date_period: str | None = None,
        last_trans_date_later: int | None = None,
        last_trans_date_period_later: DatePeriodModel | None = None,
        no_trans: bool | None = None,
        trans: bool | None = None,
        gifts_purchase_min: float | None = None,
        gifts_purchase_max: float | None = None,
        refunds_purchase_min: float | None = None,
        refunds_purchase_max: float | None = None,
        ingame_purchase_min: float | None = None,
        ingame_purchase_max: float | None = None,
        games_purchase_min: float | None = None,
        games_purchase_max: float | None = None,
        purchase_min: float | None = None,
        purchase_max: float | None = None,
        has_activated_keys: YesNoNoMatterScheme | None = None,
        elo_min: int | None = None,
        elo_max: int | None = None,
        cs2_map_rank: int | None = None,
        cs2_map_rmin: int | None = None,
        cs2_map_rmax: int | None = None,
        has_faceit: YesNoNoMatterScheme | None = None,
        faceit_csgo_lvl_min: int | None = None,
        faceit_csgo_lvl_max: int | None = None,
        rust_deaths_min: int | None = None,
        rust_deaths_max: int | None = None,
        rust_kills_min: int | None = None,
        rust_kills_max: int | None = None,
        d2_last_match_date: int | None = None,
        d2_last_match_date_period: str | None = None,
        cards_min: int | None = None,
        cards_max: int | None = None,
        cards_games_min: int | None = None,
        cards_games_max: int | None = None,
        skip_vac_inv: bool | None = None,
    ) -> dict[str, Any]:
        path = "/steam"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_type is not None:
            params["email_type[]"] = email_type
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if item_domain is not None:
            params["item_domain"] = item_domain
        if game is not None:
            params["game[]"] = game
        if hours_played is not None:
            params["hours_played"] = hours_played
        if hours_played_max is not None:
            params["hours_played_max"] = hours_played_max
        if eg is not None:
            params["eg"] = eg
        if vac is not None:
            params["vac[]"] = vac
        if vac_skip_game_check is not None:
            params["vac_skip_game_check"] = vac_skip_game_check
        if rt is not None:
            params["rt"] = rt
        if trade_ban is not None:
            params["trade_ban"] = trade_ban
        if trade_limit is not None:
            params["trade_limit"] = trade_limit
        if daybreak is not None:
            params["daybreak"] = daybreak
        if limit is not None:
            params["limit"] = limit
        if mafile is not None:
            params["mafile"] = mafile
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if lmin is not None:
            params["lmin"] = lmin
        if lmax is not None:
            params["lmax"] = lmax
        if rmin is not None:
            params["rmin"] = rmin
        if rmax is not None:
            params["rmax"] = rmax
        if wingman_rmin is not None:
            params["wingman_rmin"] = wingman_rmin
        if wingman_rmax is not None:
            params["wingman_rmax"] = wingman_rmax
        if no_vac is not None:
            params["no_vac"] = no_vac
        if mm_ban is not None:
            params["mm_ban"] = mm_ban
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        if inv_game is not None:
            params["inv_game"] = inv_game
        if inv_min is not None:
            params["inv_min"] = inv_min
        if inv_max is not None:
            params["inv_max"] = inv_max
        if friends_min is not None:
            params["friends_min"] = friends_min
        if friends_max is not None:
            params["friends_max"] = friends_max
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if win_count_min is not None:
            params["win_count_min"] = win_count_min
        if win_count_max is not None:
            params["win_count_max"] = win_count_max
        if medal_id is not None:
            params["medal_id[]"] = medal_id
        if medal_operator_or is not None:
            params["medal_operator_or"] = medal_operator_or
        if medal_min is not None:
            params["medal_min"] = medal_min
        if medal_max is not None:
            params["medal_max"] = medal_max
        if gift is not None:
            params["gift[]"] = gift
        if gift_min is not None:
            params["gift_min"] = gift_min
        if gift_max is not None:
            params["gift_max"] = gift_max
        if recently_hours_min is not None:
            params["recently_hours_min"] = recently_hours_min
        if recently_hours_max is not None:
            params["recently_hours_max"] = recently_hours_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if cs2_profile_rank_min is not None:
            params["cs2_profile_rank_min"] = cs2_profile_rank_min
        if cs2_profile_rank_max is not None:
            params["cs2_profile_rank_max"] = cs2_profile_rank_max
        if solommr_min is not None:
            params["solommr_min"] = solommr_min
        if solommr_max is not None:
            params["solommr_max"] = solommr_max
        if d2_game_count_min is not None:
            params["d2_game_count_min"] = d2_game_count_min
        if d2_game_count_max is not None:
            params["d2_game_count_max"] = d2_game_count_max
        if d2_win_count_min is not None:
            params["d2_win_count_min"] = d2_win_count_min
        if d2_win_count_max is not None:
            params["d2_win_count_max"] = d2_win_count_max
        if d2_behavior_min is not None:
            params["d2_behavior_min"] = d2_behavior_min
        if d2_behavior_max is not None:
            params["d2_behavior_max"] = d2_behavior_max
        if faceit_lvl_min is not None:
            params["faceit_lvl_min"] = faceit_lvl_min
        if faceit_lvl_max is not None:
            params["faceit_lvl_max"] = faceit_lvl_max
        if points_min is not None:
            params["points_min"] = points_min
        if points_max is not None:
            params["points_max"] = points_max
        if relevant_gmin is not None:
            params["relevant_gmin"] = relevant_gmin
        if relevant_gmax is not None:
            params["relevant_gmax"] = relevant_gmax
        if last_trans_date is not None:
            params["last_trans_date"] = last_trans_date
        if last_trans_date_period is not None:
            params["last_trans_date_period"] = last_trans_date_period
        if last_trans_date_later is not None:
            params["last_trans_date_later"] = last_trans_date_later
        if last_trans_date_period_later is not None:
            params["last_trans_date_period_later"] = last_trans_date_period_later
        if no_trans is not None:
            params["no_trans"] = no_trans
        if trans is not None:
            params["trans"] = trans
        if gifts_purchase_min is not None:
            params["gifts_purchase_min"] = gifts_purchase_min
        if gifts_purchase_max is not None:
            params["gifts_purchase_max"] = gifts_purchase_max
        if refunds_purchase_min is not None:
            params["refunds_purchase_min"] = refunds_purchase_min
        if refunds_purchase_max is not None:
            params["refunds_purchase_max"] = refunds_purchase_max
        if ingame_purchase_min is not None:
            params["ingame_purchase_min"] = ingame_purchase_min
        if ingame_purchase_max is not None:
            params["ingame_purchase_max"] = ingame_purchase_max
        if games_purchase_min is not None:
            params["games_purchase_min"] = games_purchase_min
        if games_purchase_max is not None:
            params["games_purchase_max"] = games_purchase_max
        if purchase_min is not None:
            params["purchase_min"] = purchase_min
        if purchase_max is not None:
            params["purchase_max"] = purchase_max
        if has_activated_keys is not None:
            params["has_activated_keys"] = has_activated_keys
        if elo_min is not None:
            params["elo_min"] = elo_min
        if elo_max is not None:
            params["elo_max"] = elo_max
        if cs2_map_rank is not None:
            params["cs2_map_rank"] = cs2_map_rank
        if cs2_map_rmin is not None:
            params["cs2_map_rmin"] = cs2_map_rmin
        if cs2_map_rmax is not None:
            params["cs2_map_rmax"] = cs2_map_rmax
        if has_faceit is not None:
            params["has_faceit"] = has_faceit
        if faceit_csgo_lvl_min is not None:
            params["faceit_csgo_lvl_min"] = faceit_csgo_lvl_min
        if faceit_csgo_lvl_max is not None:
            params["faceit_csgo_lvl_max"] = faceit_csgo_lvl_max
        if rust_deaths_min is not None:
            params["rust_deaths_min"] = rust_deaths_min
        if rust_deaths_max is not None:
            params["rust_deaths_max"] = rust_deaths_max
        if rust_kills_min is not None:
            params["rust_kills_min"] = rust_kills_min
        if rust_kills_max is not None:
            params["rust_kills_max"] = rust_kills_max
        if d2_last_match_date is not None:
            params["d2_last_match_date"] = d2_last_match_date
        if d2_last_match_date_period is not None:
            params["d2_last_match_date_period"] = d2_last_match_date_period
        if cards_min is not None:
            params["cards_min"] = cards_min
        if cards_max is not None:
            params["cards_max"] = cards_max
        if cards_games_min is not None:
            params["cards_games_min"] = cards_games_min
        if cards_games_max is not None:
            params["cards_games_max"] = cards_games_max
        if skip_vac_inv is not None:
            params["skip_vac_inv"] = skip_vac_inv
        return self._request("GET", path, params=params)

    def category_fortnite(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        email_type: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        temp_email: str | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        smin: int | None = None,
        smax: int | None = None,
        vbmin: int | None = None,
        vbmax: int | None = None,
        skin: list[str] | None = None,
        pickaxe: list[str] | None = None,
        glider: list[str] | None = None,
        dance: list[str] | None = None,
        change_email: str | None = None,
        platform: list[str] | None = None,
        skins_shop_min: int | None = None,
        skins_shop_max: int | None = None,
        pickaxes_shop_min: int | None = None,
        pickaxes_shop_max: int | None = None,
        dances_shop_min: int | None = None,
        dances_shop_max: int | None = None,
        gliders_shop_min: int | None = None,
        gliders_shop_max: int | None = None,
        skins_shop_vbmin: int | None = None,
        skins_shop_vbmax: int | None = None,
        pickaxes_shop_vbmin: int | None = None,
        pickaxes_shop_vbmax: int | None = None,
        dances_shop_vbmin: int | None = None,
        dances_shop_vbmax: int | None = None,
        gliders_shop_vbmin: int | None = None,
        gliders_shop_vbmax: int | None = None,
        bp: YesNoNoMatterScheme | None = None,
        lmin: int | None = None,
        lmax: int | None = None,
        bp_lmin: int | None = None,
        bp_lmax: int | None = None,
        last_trans_date: int | None = None,
        last_trans_date_period: str | None = None,
        no_trans: bool | None = None,
        xbox_linkable: YesNoNoMatterScheme | None = None,
        psn_linkable: YesNoNoMatterScheme | None = None,
        daybreak: int | None = None,
        rl_purchases: bool | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        refund_credits_min: int | None = None,
        refund_credits_max: int | None = None,
        pickaxe_min: int | None = None,
        pickaxe_max: int | None = None,
        dmin: int | None = None,
        dmax: int | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/fortnite"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if email_type is not None:
            params["email_type[]"] = email_type
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if temp_email is not None:
            params["temp_email"] = temp_email
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if smin is not None:
            params["smin"] = smin
        if smax is not None:
            params["smax"] = smax
        if vbmin is not None:
            params["vbmin"] = vbmin
        if vbmax is not None:
            params["vbmax"] = vbmax
        if skin is not None:
            params["skin[]"] = skin
        if pickaxe is not None:
            params["pickaxe[]"] = pickaxe
        if glider is not None:
            params["glider[]"] = glider
        if dance is not None:
            params["dance[]"] = dance
        if change_email is not None:
            params["change_email"] = change_email
        if platform is not None:
            params["platform[]"] = platform
        if skins_shop_min is not None:
            params["skins_shop_min"] = skins_shop_min
        if skins_shop_max is not None:
            params["skins_shop_max"] = skins_shop_max
        if pickaxes_shop_min is not None:
            params["pickaxes_shop_min"] = pickaxes_shop_min
        if pickaxes_shop_max is not None:
            params["pickaxes_shop_max"] = pickaxes_shop_max
        if dances_shop_min is not None:
            params["dances_shop_min"] = dances_shop_min
        if dances_shop_max is not None:
            params["dances_shop_max"] = dances_shop_max
        if gliders_shop_min is not None:
            params["gliders_shop_min"] = gliders_shop_min
        if gliders_shop_max is not None:
            params["gliders_shop_max"] = gliders_shop_max
        if skins_shop_vbmin is not None:
            params["skins_shop_vbmin"] = skins_shop_vbmin
        if skins_shop_vbmax is not None:
            params["skins_shop_vbmax"] = skins_shop_vbmax
        if pickaxes_shop_vbmin is not None:
            params["pickaxes_shop_vbmin"] = pickaxes_shop_vbmin
        if pickaxes_shop_vbmax is not None:
            params["pickaxes_shop_vbmax"] = pickaxes_shop_vbmax
        if dances_shop_vbmin is not None:
            params["dances_shop_vbmin"] = dances_shop_vbmin
        if dances_shop_vbmax is not None:
            params["dances_shop_vbmax"] = dances_shop_vbmax
        if gliders_shop_vbmin is not None:
            params["gliders_shop_vbmin"] = gliders_shop_vbmin
        if gliders_shop_vbmax is not None:
            params["gliders_shop_vbmax"] = gliders_shop_vbmax
        if bp is not None:
            params["bp"] = bp
        if lmin is not None:
            params["lmin"] = lmin
        if lmax is not None:
            params["lmax"] = lmax
        if bp_lmin is not None:
            params["bp_lmin"] = bp_lmin
        if bp_lmax is not None:
            params["bp_lmax"] = bp_lmax
        if last_trans_date is not None:
            params["last_trans_date"] = last_trans_date
        if last_trans_date_period is not None:
            params["last_trans_date_period"] = last_trans_date_period
        if no_trans is not None:
            params["no_trans"] = no_trans
        if xbox_linkable is not None:
            params["xbox_linkable"] = xbox_linkable
        if psn_linkable is not None:
            params["psn_linkable"] = psn_linkable
        if daybreak is not None:
            params["daybreak"] = daybreak
        if rl_purchases is not None:
            params["rl_purchases"] = rl_purchases
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if refund_credits_min is not None:
            params["refund_credits_min"] = refund_credits_min
        if refund_credits_max is not None:
            params["refund_credits_max"] = refund_credits_max
        if pickaxe_min is not None:
            params["pickaxe_min"] = pickaxe_min
        if pickaxe_max is not None:
            params["pickaxe_max"] = pickaxe_max
        if dmin is not None:
            params["dmin"] = dmin
        if dmax is not None:
            params["dmax"] = dmax
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        return self._request("GET", path, params=params)

    def category_mihoyo(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        email_type: list[str] | None = None,
        parse_same_item_ids: bool | None = None,
        item_domain: str | None = None,
        email: str | None = None,
        ea: YesNoNoMatterScheme | None = None,
        region: list[str] | None = None,
        not_region: list[str] | None = None,
        genshin_character: list[int] | None = None,
        genshin_character_constellations: dict[str, Any] | None = None,
        genshin_character_constellations_max: dict[str, Any] | None = None,
        genshin_weapon: list[int] | None = None,
        genshin_char_min: int | None = None,
        genshin_char_max: int | None = None,
        genshin_legendary_min: int | None = None,
        genshin_legendary_max: int | None = None,
        genshin_level_min: int | None = None,
        genshin_level_max: int | None = None,
        genshin_legendary_weapon_min: int | None = None,
        genshin_legendary_weapon_max: int | None = None,
        constellations_min: int | None = None,
        constellations_max: int | None = None,
        genshin_achievement_min: int | None = None,
        genshin_achievement_max: int | None = None,
        genshin_currency_min: int | None = None,
        genshin_currency_max: int | None = None,
        honkai_character: list[int] | None = None,
        honkai_character_eidolons: dict[str, Any] | None = None,
        honkai_character_eidolons_max: dict[str, Any] | None = None,
        honkai_weapon: list[int] | None = None,
        honkai_char_min: int | None = None,
        honkai_char_max: int | None = None,
        honkai_legendary_min: int | None = None,
        honkai_legendary_max: int | None = None,
        honkai_level_min: int | None = None,
        honkai_level_max: int | None = None,
        honkai_legendary_weapon_min: int | None = None,
        honkai_legendary_weapon_max: int | None = None,
        eidolons_min: int | None = None,
        eidolons_max: int | None = None,
        honkai_achievement_min: int | None = None,
        honkai_achievement_max: int | None = None,
        honkai_currency_min: int | None = None,
        honkai_currency_max: int | None = None,
        zenless_character: list[int] | None = None,
        zenless_character_cinemas: dict[str, Any] | None = None,
        zenless_character_cinemas_max: dict[str, Any] | None = None,
        zenless_weapon: list[int] | None = None,
        zenless_legendary_min: int | None = None,
        zenless_legendary_max: int | None = None,
        cinemas_min: int | None = None,
        cinemas_max: int | None = None,
        zenless_legendary_weapon_min: int | None = None,
        zenless_legendary_weapon_max: int | None = None,
        zenless_char_min: int | None = None,
        zenless_char_max: int | None = None,
        zenless_level_min: int | None = None,
        zenless_level_max: int | None = None,
        zenless_achievement_min: int | None = None,
        zenless_achievement_max: int | None = None,
        zenless_currency_min: int | None = None,
        zenless_currency_max: int | None = None,
        daybreak: int | None = None,
    ) -> dict[str, Any]:
        path = "/mihoyo"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if email_type is not None:
            params["email_type[]"] = email_type
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if item_domain is not None:
            params["item_domain"] = item_domain
        if email is not None:
            params["email"] = email
        if ea is not None:
            params["ea"] = ea
        if region is not None:
            params["region"] = region
        if not_region is not None:
            params["not_region"] = not_region
        if genshin_character is not None:
            params["genshin_character[]"] = genshin_character
        if genshin_character_constellations is not None:
            params["genshin_character_constellations"] = genshin_character_constellations
        if genshin_character_constellations_max is not None:
            params["genshin_character_constellations_max"] = genshin_character_constellations_max
        if genshin_weapon is not None:
            params["genshin_weapon[]"] = genshin_weapon
        if genshin_char_min is not None:
            params["genshin_char_min"] = genshin_char_min
        if genshin_char_max is not None:
            params["genshin_char_max"] = genshin_char_max
        if genshin_legendary_min is not None:
            params["genshin_legendary_min"] = genshin_legendary_min
        if genshin_legendary_max is not None:
            params["genshin_legendary_max"] = genshin_legendary_max
        if genshin_level_min is not None:
            params["genshin_level_min"] = genshin_level_min
        if genshin_level_max is not None:
            params["genshin_level_max"] = genshin_level_max
        if genshin_legendary_weapon_min is not None:
            params["genshin_legendary_weapon_min"] = genshin_legendary_weapon_min
        if genshin_legendary_weapon_max is not None:
            params["genshin_legendary_weapon_max"] = genshin_legendary_weapon_max
        if constellations_min is not None:
            params["constellations_min"] = constellations_min
        if constellations_max is not None:
            params["constellations_max"] = constellations_max
        if genshin_achievement_min is not None:
            params["genshin_achievement_min"] = genshin_achievement_min
        if genshin_achievement_max is not None:
            params["genshin_achievement_max"] = genshin_achievement_max
        if genshin_currency_min is not None:
            params["genshin_currency_min"] = genshin_currency_min
        if genshin_currency_max is not None:
            params["genshin_currency_max"] = genshin_currency_max
        if honkai_character is not None:
            params["honkai_character[]"] = honkai_character
        if honkai_character_eidolons is not None:
            params["honkai_character_eidolons"] = honkai_character_eidolons
        if honkai_character_eidolons_max is not None:
            params["honkai_character_eidolons_max"] = honkai_character_eidolons_max
        if honkai_weapon is not None:
            params["honkai_weapon[]"] = honkai_weapon
        if honkai_char_min is not None:
            params["honkai_char_min"] = honkai_char_min
        if honkai_char_max is not None:
            params["honkai_char_max"] = honkai_char_max
        if honkai_legendary_min is not None:
            params["honkai_legendary_min"] = honkai_legendary_min
        if honkai_legendary_max is not None:
            params["honkai_legendary_max"] = honkai_legendary_max
        if honkai_level_min is not None:
            params["honkai_level_min"] = honkai_level_min
        if honkai_level_max is not None:
            params["honkai_level_max"] = honkai_level_max
        if honkai_legendary_weapon_min is not None:
            params["honkai_legendary_weapon_min"] = honkai_legendary_weapon_min
        if honkai_legendary_weapon_max is not None:
            params["honkai_legendary_weapon_max"] = honkai_legendary_weapon_max
        if eidolons_min is not None:
            params["eidolons_min"] = eidolons_min
        if eidolons_max is not None:
            params["eidolons_max"] = eidolons_max
        if honkai_achievement_min is not None:
            params["honkai_achievement_min"] = honkai_achievement_min
        if honkai_achievement_max is not None:
            params["honkai_achievement_max"] = honkai_achievement_max
        if honkai_currency_min is not None:
            params["honkai_currency_min"] = honkai_currency_min
        if honkai_currency_max is not None:
            params["honkai_currency_max"] = honkai_currency_max
        if zenless_character is not None:
            params["zenless_character[]"] = zenless_character
        if zenless_character_cinemas is not None:
            params["zenless_character_cinemas"] = zenless_character_cinemas
        if zenless_character_cinemas_max is not None:
            params["zenless_character_cinemas_max"] = zenless_character_cinemas_max
        if zenless_weapon is not None:
            params["zenless_weapon[]"] = zenless_weapon
        if zenless_legendary_min is not None:
            params["zenless_legendary_min"] = zenless_legendary_min
        if zenless_legendary_max is not None:
            params["zenless_legendary_max"] = zenless_legendary_max
        if cinemas_min is not None:
            params["cinemas_min"] = cinemas_min
        if cinemas_max is not None:
            params["cinemas_max"] = cinemas_max
        if zenless_legendary_weapon_min is not None:
            params["zenless_legendary_weapon_min"] = zenless_legendary_weapon_min
        if zenless_legendary_weapon_max is not None:
            params["zenless_legendary_weapon_max"] = zenless_legendary_weapon_max
        if zenless_char_min is not None:
            params["zenless_char_min"] = zenless_char_min
        if zenless_char_max is not None:
            params["zenless_char_max"] = zenless_char_max
        if zenless_level_min is not None:
            params["zenless_level_min"] = zenless_level_min
        if zenless_level_max is not None:
            params["zenless_level_max"] = zenless_level_max
        if zenless_achievement_min is not None:
            params["zenless_achievement_min"] = zenless_achievement_min
        if zenless_achievement_max is not None:
            params["zenless_achievement_max"] = zenless_achievement_max
        if zenless_currency_min is not None:
            params["zenless_currency_min"] = zenless_currency_min
        if zenless_currency_max is not None:
            params["zenless_currency_max"] = zenless_currency_max
        if daybreak is not None:
            params["daybreak"] = daybreak
        return self._request("GET", path, params=params)

    def category_riot(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        rmin: int | None = None,
        rmax: int | None = None,
        last_rmin: int | None = None,
        last_rmax: int | None = None,
        previous_rmin: int | None = None,
        previous_rmax: int | None = None,
        weaponSkin: list[str] | None = None,
        buddy: list[str] | None = None,
        agent: list[str] | None = None,
        champion: list[str] | None = None,
        skin: list[str] | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        valorant_level_min: int | None = None,
        valorant_level_max: int | None = None,
        lol_level_min: int | None = None,
        lol_level_max: int | None = None,
        inv_min: int | None = None,
        inv_max: int | None = None,
        vp_min: int | None = None,
        vp_max: int | None = None,
        valorant_smin: int | None = None,
        valorant_smax: int | None = None,
        valorant_rank_type: list[str] | None = None,
        amin: int | None = None,
        amax: int | None = None,
        valorant_region: list[str] | None = None,
        valorant_not_region: list[str] | None = None,
        lol_region: list[str] | None = None,
        lol_not_region: list[str] | None = None,
        knife: bool | None = None,
        lol_smin: int | None = None,
        lol_smax: int | None = None,
        champion_min: int | None = None,
        champion_max: int | None = None,
        win_rate_min: int | None = None,
        win_rate_max: int | None = None,
        blue_min: int | None = None,
        blue_max: int | None = None,
        orange_min: int | None = None,
        orange_max: int | None = None,
        mythic_min: int | None = None,
        mythic_max: int | None = None,
        riot_min: int | None = None,
        riot_max: int | None = None,
        email: str | None = None,
        tel: str | None = None,
        valorant_knife_min: int | None = None,
        valorant_knife_max: int | None = None,
        rp_min: int | None = None,
        rp_max: int | None = None,
        fa_min: int | None = None,
        fa_max: int | None = None,
        lol_rank: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/riot"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if rmin is not None:
            params["rmin"] = rmin
        if rmax is not None:
            params["rmax"] = rmax
        if last_rmin is not None:
            params["last_rmin"] = last_rmin
        if last_rmax is not None:
            params["last_rmax"] = last_rmax
        if previous_rmin is not None:
            params["previous_rmin"] = previous_rmin
        if previous_rmax is not None:
            params["previous_rmax"] = previous_rmax
        if weaponSkin is not None:
            params["weaponSkin[]"] = weaponSkin
        if buddy is not None:
            params["buddy[]"] = buddy
        if agent is not None:
            params["agent[]"] = agent
        if champion is not None:
            params["champion[]"] = champion
        if skin is not None:
            params["skin[]"] = skin
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if valorant_level_min is not None:
            params["valorant_level_min"] = valorant_level_min
        if valorant_level_max is not None:
            params["valorant_level_max"] = valorant_level_max
        if lol_level_min is not None:
            params["lol_level_min"] = lol_level_min
        if lol_level_max is not None:
            params["lol_level_max"] = lol_level_max
        if inv_min is not None:
            params["inv_min"] = inv_min
        if inv_max is not None:
            params["inv_max"] = inv_max
        if vp_min is not None:
            params["vp_min"] = vp_min
        if vp_max is not None:
            params["vp_max"] = vp_max
        if valorant_smin is not None:
            params["valorant_smin"] = valorant_smin
        if valorant_smax is not None:
            params["valorant_smax"] = valorant_smax
        if valorant_rank_type is not None:
            params["valorant_rank_type[]"] = valorant_rank_type
        if amin is not None:
            params["amin"] = amin
        if amax is not None:
            params["amax"] = amax
        if valorant_region is not None:
            params["valorant_region[]"] = valorant_region
        if valorant_not_region is not None:
            params["valorant_not_region[]"] = valorant_not_region
        if lol_region is not None:
            params["lol_region[]"] = lol_region
        if lol_not_region is not None:
            params["lol_not_region[]"] = lol_not_region
        if knife is not None:
            params["knife"] = knife
        if lol_smin is not None:
            params["lol_smin"] = lol_smin
        if lol_smax is not None:
            params["lol_smax"] = lol_smax
        if champion_min is not None:
            params["champion_min"] = champion_min
        if champion_max is not None:
            params["champion_max"] = champion_max
        if win_rate_min is not None:
            params["win_rate_min"] = win_rate_min
        if win_rate_max is not None:
            params["win_rate_max"] = win_rate_max
        if blue_min is not None:
            params["blue_min"] = blue_min
        if blue_max is not None:
            params["blue_max"] = blue_max
        if orange_min is not None:
            params["orange_min"] = orange_min
        if orange_max is not None:
            params["orange_max"] = orange_max
        if mythic_min is not None:
            params["mythic_min"] = mythic_min
        if mythic_max is not None:
            params["mythic_max"] = mythic_max
        if riot_min is not None:
            params["riot_min"] = riot_min
        if riot_max is not None:
            params["riot_max"] = riot_max
        if email is not None:
            params["email"] = email
        if tel is not None:
            params["tel"] = tel
        if valorant_knife_min is not None:
            params["valorant_knife_min"] = valorant_knife_min
        if valorant_knife_max is not None:
            params["valorant_knife_max"] = valorant_knife_max
        if rp_min is not None:
            params["rp_min"] = rp_min
        if rp_max is not None:
            params["rp_max"] = rp_max
        if fa_min is not None:
            params["fa_min"] = fa_min
        if fa_max is not None:
            params["fa_max"] = fa_max
        if lol_rank is not None:
            params["lol_rank[]"] = lol_rank
        return self._request("GET", path, params=params)

    def category_telegram(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        spam: YesNoNoMatterScheme | None = None,
        password: YesNoNoMatterScheme | None = None,
        premium: str | None = None,
        premium_expiration: int | None = None,
        premium_expiration_period: str | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        min_channels: int | None = None,
        max_channels: int | None = None,
        min_chats: int | None = None,
        max_chats: int | None = None,
        min_conversations: int | None = None,
        max_conversations: int | None = None,
        min_admin: int | None = None,
        max_admin: int | None = None,
        min_admin_sub: int | None = None,
        max_admin_sub: int | None = None,
        dig_min: int | None = None,
        dig_max: int | None = None,
        min_contacts: int | None = None,
        max_contacts: int | None = None,
        min_stars: int | None = None,
        max_stars: int | None = None,
        birthday: int | None = None,
        birthday_period: str | None = None,
        birthday_after: int | None = None,
        birthday_after_period: str | None = None,
        min_id: int | None = None,
        max_id: int | None = None,
        allow_geo_spamblock: bool | None = None,
        min_gifts: int | None = None,
        max_gifts: int | None = None,
        min_nft_gifts: int | None = None,
        max_nft_gifts: int | None = None,
        min_gifts_stars: int | None = None,
        max_gifts_stars: int | None = None,
        min_gifts_convert_stars: int | None = None,
        max_gifts_convert_stars: int | None = None,
        dc_id: list[int] | None = None,
        not_dc_id: list[int] | None = None,
        email: str | None = None,
        min_bots: int | None = None,
        max_bots: int | None = None,
        min_bot_active_users: int | None = None,
        max_bot_active_users: int | None = None,
    ) -> dict[str, Any]:
        path = "/telegram"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if spam is not None:
            params["spam"] = spam
        if password is not None:
            params["password"] = password
        if premium is not None:
            params["premium"] = premium
        if premium_expiration is not None:
            params["premium_expiration"] = premium_expiration
        if premium_expiration_period is not None:
            params["premium_expiration_period"] = premium_expiration_period
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if min_channels is not None:
            params["min_channels"] = min_channels
        if max_channels is not None:
            params["max_channels"] = max_channels
        if min_chats is not None:
            params["min_chats"] = min_chats
        if max_chats is not None:
            params["max_chats"] = max_chats
        if min_conversations is not None:
            params["min_conversations"] = min_conversations
        if max_conversations is not None:
            params["max_conversations"] = max_conversations
        if min_admin is not None:
            params["min_admin"] = min_admin
        if max_admin is not None:
            params["max_admin"] = max_admin
        if min_admin_sub is not None:
            params["min_admin_sub"] = min_admin_sub
        if max_admin_sub is not None:
            params["max_admin_sub"] = max_admin_sub
        if dig_min is not None:
            params["dig_min"] = dig_min
        if dig_max is not None:
            params["dig_max"] = dig_max
        if min_contacts is not None:
            params["min_contacts"] = min_contacts
        if max_contacts is not None:
            params["max_contacts"] = max_contacts
        if min_stars is not None:
            params["min_stars"] = min_stars
        if max_stars is not None:
            params["max_stars"] = max_stars
        if birthday is not None:
            params["birthday"] = birthday
        if birthday_period is not None:
            params["birthday_period"] = birthday_period
        if birthday_after is not None:
            params["birthday_after"] = birthday_after
        if birthday_after_period is not None:
            params["birthday_after_period"] = birthday_after_period
        if min_id is not None:
            params["min_id"] = min_id
        if max_id is not None:
            params["max_id"] = max_id
        if allow_geo_spamblock is not None:
            params["allow_geo_spamblock"] = allow_geo_spamblock
        if min_gifts is not None:
            params["min_gifts"] = min_gifts
        if max_gifts is not None:
            params["max_gifts"] = max_gifts
        if min_nft_gifts is not None:
            params["min_nft_gifts"] = min_nft_gifts
        if max_nft_gifts is not None:
            params["max_nft_gifts"] = max_nft_gifts
        if min_gifts_stars is not None:
            params["min_gifts_stars"] = min_gifts_stars
        if max_gifts_stars is not None:
            params["max_gifts_stars"] = max_gifts_stars
        if min_gifts_convert_stars is not None:
            params["min_gifts_convert_stars"] = min_gifts_convert_stars
        if max_gifts_convert_stars is not None:
            params["max_gifts_convert_stars"] = max_gifts_convert_stars
        if dc_id is not None:
            params["dc_id[]"] = dc_id
        if not_dc_id is not None:
            params["not_dc_id[]"] = not_dc_id
        if email is not None:
            params["email"] = email
        if min_bots is not None:
            params["min_bots"] = min_bots
        if max_bots is not None:
            params["max_bots"] = max_bots
        if min_bot_active_users is not None:
            params["min_bot_active_users"] = min_bot_active_users
        if max_bot_active_users is not None:
            params["max_bot_active_users"] = max_bot_active_users
        return self._request("GET", path, params=params)

    def category_supercell(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        daybreak: int | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        tel: YesNoNoMatterScheme | None = None,
        brawl_level_min: int | None = None,
        brawl_level_max: int | None = None,
        brawl_cup_min: int | None = None,
        brawl_cup_max: int | None = None,
        brawl_wins_min: int | None = None,
        brawl_wins_max: int | None = None,
        brawl_pass: YesNoNoMatterScheme | None = None,
        brawler: list[str] | None = None,
        brawlers_min: int | None = None,
        brawlers_max: int | None = None,
        legendary_brawlers_min: int | None = None,
        legendary_brawlers_max: int | None = None,
        royale_level_min: int | None = None,
        royale_level_max: int | None = None,
        royale_cup_min: int | None = None,
        royale_cup_max: int | None = None,
        royale_wins_min: int | None = None,
        royale_wins_max: int | None = None,
        king_level_min: int | None = None,
        king_level_max: int | None = None,
        royale_pass: YesNoNoMatterScheme | None = None,
        clash_level_min: int | None = None,
        clash_level_max: int | None = None,
        clash_cup_min: int | None = None,
        clash_cup_max: int | None = None,
        clash_wins_min: int | None = None,
        clash_wins_max: int | None = None,
        clash_pass: YesNoNoMatterScheme | None = None,
        total_heroes_level_min: int | None = None,
        total_heroes_level_max: int | None = None,
        total_troops_level_min: int | None = None,
        total_troops_level_max: int | None = None,
        total_spells_level_min: int | None = None,
        total_spells_level_max: int | None = None,
        total_builder_heroes_level_min: int | None = None,
        total_builder_heroes_level_max: int | None = None,
        total_builder_troops_level_min: int | None = None,
        total_builder_troops_level_max: int | None = None,
        town_hall_level_min: int | None = None,
        town_hall_level_max: int | None = None,
        builder_hall_level_min: int | None = None,
        builder_hall_level_max: int | None = None,
        builder_hall_cup_min: int | None = None,
        builder_hall_cup_max: int | None = None,
        creation_year_min: int | None = None,
        creation_year_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/supercell"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if daybreak is not None:
            params["daybreak"] = daybreak
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if tel is not None:
            params["tel"] = tel
        if brawl_level_min is not None:
            params["brawl_level_min"] = brawl_level_min
        if brawl_level_max is not None:
            params["brawl_level_max"] = brawl_level_max
        if brawl_cup_min is not None:
            params["brawl_cup_min"] = brawl_cup_min
        if brawl_cup_max is not None:
            params["brawl_cup_max"] = brawl_cup_max
        if brawl_wins_min is not None:
            params["brawl_wins_min"] = brawl_wins_min
        if brawl_wins_max is not None:
            params["brawl_wins_max"] = brawl_wins_max
        if brawl_pass is not None:
            params["brawl_pass"] = brawl_pass
        if brawler is not None:
            params["brawler[]"] = brawler
        if brawlers_min is not None:
            params["brawlers_min"] = brawlers_min
        if brawlers_max is not None:
            params["brawlers_max"] = brawlers_max
        if legendary_brawlers_min is not None:
            params["legendary_brawlers_min"] = legendary_brawlers_min
        if legendary_brawlers_max is not None:
            params["legendary_brawlers_max"] = legendary_brawlers_max
        if royale_level_min is not None:
            params["royale_level_min"] = royale_level_min
        if royale_level_max is not None:
            params["royale_level_max"] = royale_level_max
        if royale_cup_min is not None:
            params["royale_cup_min"] = royale_cup_min
        if royale_cup_max is not None:
            params["royale_cup_max"] = royale_cup_max
        if royale_wins_min is not None:
            params["royale_wins_min"] = royale_wins_min
        if royale_wins_max is not None:
            params["royale_wins_max"] = royale_wins_max
        if king_level_min is not None:
            params["king_level_min"] = king_level_min
        if king_level_max is not None:
            params["king_level_max"] = king_level_max
        if royale_pass is not None:
            params["royale_pass"] = royale_pass
        if clash_level_min is not None:
            params["clash_level_min"] = clash_level_min
        if clash_level_max is not None:
            params["clash_level_max"] = clash_level_max
        if clash_cup_min is not None:
            params["clash_cup_min"] = clash_cup_min
        if clash_cup_max is not None:
            params["clash_cup_max"] = clash_cup_max
        if clash_wins_min is not None:
            params["clash_wins_min"] = clash_wins_min
        if clash_wins_max is not None:
            params["clash_wins_max"] = clash_wins_max
        if clash_pass is not None:
            params["clash_pass"] = clash_pass
        if total_heroes_level_min is not None:
            params["total_heroes_level_min"] = total_heroes_level_min
        if total_heroes_level_max is not None:
            params["total_heroes_level_max"] = total_heroes_level_max
        if total_troops_level_min is not None:
            params["total_troops_level_min"] = total_troops_level_min
        if total_troops_level_max is not None:
            params["total_troops_level_max"] = total_troops_level_max
        if total_spells_level_min is not None:
            params["total_spells_level_min"] = total_spells_level_min
        if total_spells_level_max is not None:
            params["total_spells_level_max"] = total_spells_level_max
        if total_builder_heroes_level_min is not None:
            params["total_builder_heroes_level_min"] = total_builder_heroes_level_min
        if total_builder_heroes_level_max is not None:
            params["total_builder_heroes_level_max"] = total_builder_heroes_level_max
        if total_builder_troops_level_min is not None:
            params["total_builder_troops_level_min"] = total_builder_troops_level_min
        if total_builder_troops_level_max is not None:
            params["total_builder_troops_level_max"] = total_builder_troops_level_max
        if town_hall_level_min is not None:
            params["town_hall_level_min"] = town_hall_level_min
        if town_hall_level_max is not None:
            params["town_hall_level_max"] = town_hall_level_max
        if builder_hall_level_min is not None:
            params["builder_hall_level_min"] = builder_hall_level_min
        if builder_hall_level_max is not None:
            params["builder_hall_level_max"] = builder_hall_level_max
        if builder_hall_cup_min is not None:
            params["builder_hall_cup_min"] = builder_hall_cup_min
        if builder_hall_cup_max is not None:
            params["builder_hall_cup_max"] = builder_hall_cup_max
        if creation_year_min is not None:
            params["creation_year_min"] = creation_year_min
        if creation_year_max is not None:
            params["creation_year_max"] = creation_year_max
        return self._request("GET", path, params=params)

    def category_ea(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        game: list[str] | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        al_rank_min: int | None = None,
        al_rank_max: int | None = None,
        al_level_min: int | None = None,
        al_level_max: int | None = None,
        has_ban: YesNoNoMatterScheme | None = None,
        xbox_connected: YesNoNoMatterScheme | None = None,
        steam_connected: YesNoNoMatterScheme | None = None,
        psn_connected: YesNoNoMatterScheme | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        hours_played: dict[str, Any] | None = None,
        hours_played_max: dict[str, Any] | None = None,
        transactions: YesNoNoMatterScheme | None = None,
    ) -> dict[str, Any]:
        path = "/ea"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if game is not None:
            params["game[]"] = game
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if al_rank_min is not None:
            params["al_rank_min"] = al_rank_min
        if al_rank_max is not None:
            params["al_rank_max"] = al_rank_max
        if al_level_min is not None:
            params["al_level_min"] = al_level_min
        if al_level_max is not None:
            params["al_level_max"] = al_level_max
        if has_ban is not None:
            params["has_ban"] = has_ban
        if xbox_connected is not None:
            params["xbox_connected"] = xbox_connected
        if steam_connected is not None:
            params["steam_connected"] = steam_connected
        if psn_connected is not None:
            params["psn_connected"] = psn_connected
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if hours_played is not None:
            params["hours_played"] = hours_played
        if hours_played_max is not None:
            params["hours_played_max"] = hours_played_max
        if transactions is not None:
            params["transactions"] = transactions
        return self._request("GET", path, params=params)

    def category_wot(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        daybreak: int | None = None,
        battles_min: int | None = None,
        battles_max: int | None = None,
        gold_min: int | None = None,
        gold_max: int | None = None,
        silver_min: int | None = None,
        silver_max: int | None = None,
        top_min: int | None = None,
        top_max: int | None = None,
        prem_min: int | None = None,
        prem_max: int | None = None,
        top_prem_min: int | None = None,
        top_prem_max: int | None = None,
        win_pmin: int | None = None,
        win_pmax: int | None = None,
        tank: list[int] | None = None,
        region: list[str] | None = None,
        not_region: list[str] | None = None,
        premium: str | None = None,
        premium_expiration: int | None = None,
        premium_expiration_period: str | None = None,
        clan: str | None = None,
        clan_role: list[str] | None = None,
        not_clan_role: list[str] | None = None,
        clan_gold_min: int | None = None,
        clan_gold_max: int | None = None,
        clan_credits_min: int | None = None,
        clan_credits_max: int | None = None,
        clan_crystal_min: int | None = None,
        clan_crystal_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/world-of-tanks"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if daybreak is not None:
            params["daybreak"] = daybreak
        if battles_min is not None:
            params["battles_min"] = battles_min
        if battles_max is not None:
            params["battles_max"] = battles_max
        if gold_min is not None:
            params["gold_min"] = gold_min
        if gold_max is not None:
            params["gold_max"] = gold_max
        if silver_min is not None:
            params["silver_min"] = silver_min
        if silver_max is not None:
            params["silver_max"] = silver_max
        if top_min is not None:
            params["top_min"] = top_min
        if top_max is not None:
            params["top_max"] = top_max
        if prem_min is not None:
            params["prem_min"] = prem_min
        if prem_max is not None:
            params["prem_max"] = prem_max
        if top_prem_min is not None:
            params["top_prem_min"] = top_prem_min
        if top_prem_max is not None:
            params["top_prem_max"] = top_prem_max
        if win_pmin is not None:
            params["win_pmin"] = win_pmin
        if win_pmax is not None:
            params["win_pmax"] = win_pmax
        if tank is not None:
            params["tank[]"] = tank
        if region is not None:
            params["region[]"] = region
        if not_region is not None:
            params["not_region[]"] = not_region
        if premium is not None:
            params["premium"] = premium
        if premium_expiration is not None:
            params["premium_expiration"] = premium_expiration
        if premium_expiration_period is not None:
            params["premium_expiration_period"] = premium_expiration_period
        if clan is not None:
            params["clan"] = clan
        if clan_role is not None:
            params["clan_role[]"] = clan_role
        if not_clan_role is not None:
            params["not_clan_role[]"] = not_clan_role
        if clan_gold_min is not None:
            params["clan_gold_min"] = clan_gold_min
        if clan_gold_max is not None:
            params["clan_gold_max"] = clan_gold_max
        if clan_credits_min is not None:
            params["clan_credits_min"] = clan_credits_min
        if clan_credits_max is not None:
            params["clan_credits_max"] = clan_credits_max
        if clan_crystal_min is not None:
            params["clan_crystal_min"] = clan_crystal_min
        if clan_crystal_max is not None:
            params["clan_crystal_max"] = clan_crystal_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        return self._request("GET", path, params=params)

    def category_wot_blitz(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        daybreak: int | None = None,
        battles_min: int | None = None,
        battles_max: int | None = None,
        gold_min: int | None = None,
        gold_max: int | None = None,
        silver_min: int | None = None,
        silver_max: int | None = None,
        top_min: int | None = None,
        top_max: int | None = None,
        prem_min: int | None = None,
        prem_max: int | None = None,
        top_prem_min: int | None = None,
        top_prem_max: int | None = None,
        win_pmin: int | None = None,
        win_pmax: int | None = None,
        tank: list[int] | None = None,
        region: list[str] | None = None,
        not_region: list[str] | None = None,
        premium: str | None = None,
        premium_expiration: int | None = None,
        premium_expiration_period: str | None = None,
        clan: str | None = None,
        clan_role: list[str] | None = None,
        not_clan_role: list[str] | None = None,
        clan_gold_min: int | None = None,
        clan_gold_max: int | None = None,
        clan_credits_min: int | None = None,
        clan_credits_max: int | None = None,
        clan_crystal_min: int | None = None,
        clan_crystal_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/wot-blitz"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if daybreak is not None:
            params["daybreak"] = daybreak
        if battles_min is not None:
            params["battles_min"] = battles_min
        if battles_max is not None:
            params["battles_max"] = battles_max
        if gold_min is not None:
            params["gold_min"] = gold_min
        if gold_max is not None:
            params["gold_max"] = gold_max
        if silver_min is not None:
            params["silver_min"] = silver_min
        if silver_max is not None:
            params["silver_max"] = silver_max
        if top_min is not None:
            params["top_min"] = top_min
        if top_max is not None:
            params["top_max"] = top_max
        if prem_min is not None:
            params["prem_min"] = prem_min
        if prem_max is not None:
            params["prem_max"] = prem_max
        if top_prem_min is not None:
            params["top_prem_min"] = top_prem_min
        if top_prem_max is not None:
            params["top_prem_max"] = top_prem_max
        if win_pmin is not None:
            params["win_pmin"] = win_pmin
        if win_pmax is not None:
            params["win_pmax"] = win_pmax
        if tank is not None:
            params["tank[]"] = tank
        if region is not None:
            params["region[]"] = region
        if not_region is not None:
            params["not_region[]"] = not_region
        if premium is not None:
            params["premium"] = premium
        if premium_expiration is not None:
            params["premium_expiration"] = premium_expiration
        if premium_expiration_period is not None:
            params["premium_expiration_period"] = premium_expiration_period
        if clan is not None:
            params["clan"] = clan
        if clan_role is not None:
            params["clan_role[]"] = clan_role
        if not_clan_role is not None:
            params["not_clan_role[]"] = not_clan_role
        if clan_gold_min is not None:
            params["clan_gold_min"] = clan_gold_min
        if clan_gold_max is not None:
            params["clan_gold_max"] = clan_gold_max
        if clan_credits_min is not None:
            params["clan_credits_min"] = clan_credits_min
        if clan_credits_max is not None:
            params["clan_credits_max"] = clan_credits_max
        if clan_crystal_min is not None:
            params["clan_crystal_min"] = clan_crystal_min
        if clan_crystal_max is not None:
            params["clan_crystal_max"] = clan_crystal_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        return self._request("GET", path, params=params)

    def category_gifts(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
    ) -> dict[str, Any]:
        path = "/gifts"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        return self._request("GET", path, params=params)

    def category_epic_games(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        game: list[str] | None = None,
        change_email: str | None = None,
        rl_purchases: bool | None = None,
        balance_min: float | None = None,
        balance_max: float | None = None,
        rewards_balance_min: float | None = None,
        rewards_balance_max: float | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        hours_played: dict[str, Any] | None = None,
        hours_played_max: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        path = "/epicgames"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if game is not None:
            params["game[]"] = game
        if change_email is not None:
            params["change_email"] = change_email
        if rl_purchases is not None:
            params["rl_purchases"] = rl_purchases
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        if rewards_balance_min is not None:
            params["rewards_balance_min"] = rewards_balance_min
        if rewards_balance_max is not None:
            params["rewards_balance_max"] = rewards_balance_max
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if hours_played is not None:
            params["hours_played"] = hours_played
        if hours_played_max is not None:
            params["hours_played_max"] = hours_played_max
        return self._request("GET", path, params=params)

    def category_escape_from_tarkov(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        region: str | None = None,
        version: list[str] | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        level_min: int | None = None,
        level_max: int | None = None,
        pve: YesNoNoMatterScheme | None = None,
        side: str | None = None,
    ) -> dict[str, Any]:
        path = "/escape-from-tarkov"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if region is not None:
            params["region"] = region
        if version is not None:
            params["version[]"] = version
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if level_min is not None:
            params["level_min"] = level_min
        if level_max is not None:
            params["level_max"] = level_max
        if pve is not None:
            params["pve"] = pve
        if side is not None:
            params["side"] = side
        return self._request("GET", path, params=params)

    def category_social_club(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        daybreak: int | None = None,
        level_min: int | None = None,
        level_max: int | None = None,
        cash_min: int | None = None,
        cash_max: int | None = None,
        bank_cash_min: int | None = None,
        bank_cash_max: int | None = None,
        game: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/socialclub"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if daybreak is not None:
            params["daybreak"] = daybreak
        if level_min is not None:
            params["level_min"] = level_min
        if level_max is not None:
            params["level_max"] = level_max
        if cash_min is not None:
            params["cash_min"] = cash_min
        if cash_max is not None:
            params["cash_max"] = cash_max
        if bank_cash_min is not None:
            params["bank_cash_min"] = bank_cash_min
        if bank_cash_max is not None:
            params["bank_cash_max"] = bank_cash_max
        if game is not None:
            params["game[]"] = game
        return self._request("GET", path, params=params)

    def category_uplay(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        game: list[str] | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        r6_level_min: int | None = None,
        r6_level_max: int | None = None,
        r6_rank_min: int | None = None,
        r6_rank_max: int | None = None,
        r6_operators_min: int | None = None,
        r6_operators_max: int | None = None,
        r6_ban: YesNoNoMatterScheme | None = None,
        r6_smin: int | None = None,
        r6_smax: int | None = None,
        r6_skin: list[str] | None = None,
        r6_operator: list[str] | None = None,
        xbox_connected: YesNoNoMatterScheme | None = None,
        psn_connected: YesNoNoMatterScheme | None = None,
        steam_connected: YesNoNoMatterScheme | None = None,
        balance_min: float | None = None,
        balance_max: float | None = None,
        transactions: YesNoNoMatterScheme | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
    ) -> dict[str, Any]:
        path = "/uplay"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if game is not None:
            params["game[]"] = game
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if r6_level_min is not None:
            params["r6_level_min"] = r6_level_min
        if r6_level_max is not None:
            params["r6_level_max"] = r6_level_max
        if r6_rank_min is not None:
            params["r6_rank_min"] = r6_rank_min
        if r6_rank_max is not None:
            params["r6_rank_max"] = r6_rank_max
        if r6_operators_min is not None:
            params["r6_operators_min"] = r6_operators_min
        if r6_operators_max is not None:
            params["r6_operators_max"] = r6_operators_max
        if r6_ban is not None:
            params["r6_ban"] = r6_ban
        if r6_smin is not None:
            params["r6_smin"] = r6_smin
        if r6_smax is not None:
            params["r6_smax"] = r6_smax
        if r6_skin is not None:
            params["r6_skin[]"] = r6_skin
        if r6_operator is not None:
            params["r6_operator[]"] = r6_operator
        if xbox_connected is not None:
            params["xbox_connected"] = xbox_connected
        if psn_connected is not None:
            params["psn_connected"] = psn_connected
        if steam_connected is not None:
            params["steam_connected"] = steam_connected
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        if transactions is not None:
            params["transactions"] = transactions
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        return self._request("GET", path, params=params)

    def category_discord(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        nitro: YesNoNoMatterScheme | None = None,
        nitro_type: list[str] | None = None,
        nitro_length: int | None = None,
        nitro_period: str | None = None,
        boosts_min: int | None = None,
        boosts_max: int | None = None,
        billing: YesNoNoMatterScheme | None = None,
        gifts: YesNoNoMatterScheme | None = None,
        transactions: YesNoNoMatterScheme | None = None,
        badge: list[str] | None = None,
        condition: list[str] | None = None,
        chat_min: int | None = None,
        chat_max: int | None = None,
        min_admin_members: int | None = None,
        max_admin_members: int | None = None,
        min_admin: int | None = None,
        max_admin: int | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        language: list[str] | None = None,
        not_language: list[str] | None = None,
        clans: YesNoNoMatterScheme | None = None,
        min_admin_clans: int | None = None,
        max_admin_clans: int | None = None,
        min_owner_clans: int | None = None,
        max_owner_clans: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        min_servers: int | None = None,
        max_servers: int | None = None,
        p_2fa: YesNoNoMatterScheme | None = None,
        min_full_credits: int | None = None,
        max_full_credits: int | None = None,
        min_basic_credits: int | None = None,
        max_basic_credits: int | None = None,
        min_orbs: int | None = None,
        max_orbs: int | None = None,
    ) -> dict[str, Any]:
        path = "/discord"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if nitro is not None:
            params["nitro"] = nitro
        if nitro_type is not None:
            params["nitro_type[]"] = nitro_type
        if nitro_length is not None:
            params["nitro_length"] = nitro_length
        if nitro_period is not None:
            params["nitro_period"] = nitro_period
        if boosts_min is not None:
            params["boosts_min"] = boosts_min
        if boosts_max is not None:
            params["boosts_max"] = boosts_max
        if billing is not None:
            params["billing"] = billing
        if gifts is not None:
            params["gifts"] = gifts
        if transactions is not None:
            params["transactions"] = transactions
        if badge is not None:
            params["badge[]"] = badge
        if condition is not None:
            params["condition[]"] = condition
        if chat_min is not None:
            params["chat_min"] = chat_min
        if chat_max is not None:
            params["chat_max"] = chat_max
        if min_admin_members is not None:
            params["min_admin_members"] = min_admin_members
        if max_admin_members is not None:
            params["max_admin_members"] = max_admin_members
        if min_admin is not None:
            params["min_admin"] = min_admin
        if max_admin is not None:
            params["max_admin"] = max_admin
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if language is not None:
            params["language[]"] = language
        if not_language is not None:
            params["not_language[]"] = not_language
        if clans is not None:
            params["clans"] = clans
        if min_admin_clans is not None:
            params["min_admin_clans"] = min_admin_clans
        if max_admin_clans is not None:
            params["max_admin_clans"] = max_admin_clans
        if min_owner_clans is not None:
            params["min_owner_clans"] = min_owner_clans
        if max_owner_clans is not None:
            params["max_owner_clans"] = max_owner_clans
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if min_servers is not None:
            params["min_servers"] = min_servers
        if max_servers is not None:
            params["max_servers"] = max_servers
        if p_2fa is not None:
            params["2fa"] = p_2fa
        if min_full_credits is not None:
            params["min_full_credits"] = min_full_credits
        if max_full_credits is not None:
            params["max_full_credits"] = max_full_credits
        if min_basic_credits is not None:
            params["min_basic_credits"] = min_basic_credits
        if max_basic_credits is not None:
            params["max_basic_credits"] = max_basic_credits
        if min_orbs is not None:
            params["min_orbs"] = min_orbs
        if max_orbs is not None:
            params["max_orbs"] = max_orbs
        return self._request("GET", path, params=params)

    def category_tik_tok(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        followers_min: int | None = None,
        followers_max: int | None = None,
        post_min: int | None = None,
        post_max: int | None = None,
        like_min: int | None = None,
        like_max: int | None = None,
        coins_min: int | None = None,
        coins_max: int | None = None,
        cookie_login: YesNoNoMatterScheme | None = None,
        verified: str | None = None,
        email: str | None = None,
    ) -> dict[str, Any]:
        path = "/tiktok"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if followers_min is not None:
            params["followers_min"] = followers_min
        if followers_max is not None:
            params["followers_max"] = followers_max
        if post_min is not None:
            params["post_min"] = post_min
        if post_max is not None:
            params["post_max"] = post_max
        if like_min is not None:
            params["like_min"] = like_min
        if like_max is not None:
            params["like_max"] = like_max
        if coins_min is not None:
            params["coins_min"] = coins_min
        if coins_max is not None:
            params["coins_max"] = coins_max
        if cookie_login is not None:
            params["cookie_login"] = cookie_login
        if verified is not None:
            params["verified"] = verified
        if email is not None:
            params["email"] = email
        return self._request("GET", path, params=params)

    def category_instagram(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        cookies: str | None = None,
        login_without_cookies: YesNoNoMatterScheme | None = None,
        followers_min: int | None = None,
        followers_max: int | None = None,
        post_min: int | None = None,
        post_max: int | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
    ) -> dict[str, Any]:
        path = "/instagram"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if cookies is not None:
            params["cookies"] = cookies
        if login_without_cookies is not None:
            params["login_without_cookies"] = login_without_cookies
        if followers_min is not None:
            params["followers_min"] = followers_min
        if followers_max is not None:
            params["followers_max"] = followers_max
        if post_min is not None:
            params["post_min"] = post_min
        if post_max is not None:
            params["post_max"] = post_max
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        return self._request("GET", path, params=params)

    def category_battle_net(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        game: list[int] | None = None,
        daybreak: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        tel: str | None = None,
        edit_btag: YesNoNoMatterScheme | None = None,
        changeable_fn: YesNoNoMatterScheme | None = None,
        real_id: YesNoNoMatterScheme | None = None,
        parent_control: YesNoNoMatterScheme | None = None,
        no_bans: YesNoNoMatterScheme | None = None,
        balance_min: int | None = None,
        balance_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/battlenet"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if game is not None:
            params["game[]"] = game
        if daybreak is not None:
            params["daybreak"] = daybreak
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if tel is not None:
            params["tel"] = tel
        if edit_btag is not None:
            params["edit_btag"] = edit_btag
        if changeable_fn is not None:
            params["changeable_fn"] = changeable_fn
        if real_id is not None:
            params["real_id"] = real_id
        if parent_control is not None:
            params["parent_control"] = parent_control
        if no_bans is not None:
            params["no_bans"] = no_bans
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        return self._request("GET", path, params=params)

    def category_chat_gpt(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        subscription: list[str] | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
        tel: str | None = None,
        transactions: YesNoNoMatterScheme | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        openai_tier: list[str] | None = None,
        openai_balance_min: int | None = None,
        openai_balance_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/chatgpt"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if subscription is not None:
            params["subscription[]"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        if tel is not None:
            params["tel"] = tel
        if transactions is not None:
            params["transactions"] = transactions
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if openai_tier is not None:
            params["openai_tier[]"] = openai_tier
        if openai_balance_min is not None:
            params["openai_balance_min"] = openai_balance_min
        if openai_balance_max is not None:
            params["openai_balance_max"] = openai_balance_max
        return self._request("GET", path, params=params)

    def category_vpn(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        service: list[str] | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
    ) -> dict[str, Any]:
        path = "/vpn"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if service is not None:
            params["service[]"] = service
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        return self._request("GET", path, params=params)

    def category_roblox(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email: YesNoNoMatterScheme | None = None,
        robux_min: int | None = None,
        robux_max: int | None = None,
        friends_min: int | None = None,
        friends_max: int | None = None,
        followers_min: int | None = None,
        followers_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
        xbox_connected: YesNoNoMatterScheme | None = None,
        psn_connected: YesNoNoMatterScheme | None = None,
        verified: str | None = None,
        age_verified: YesNoNoMatterScheme | None = None,
        incoming_robux_total_min: int | None = None,
        incoming_robux_total_max: int | None = None,
        limited_price_min: int | None = None,
        limited_price_max: int | None = None,
        gamepass_min: int | None = None,
        gamepass_max: int | None = None,
        game_donations: YesNoNoMatterScheme | None = None,
        inv_min: int | None = None,
        inv_max: int | None = None,
        ugc_limited_price_min: int | None = None,
        ugc_limited_price_max: int | None = None,
        credit_balance_min: int | None = None,
        credit_balance_max: int | None = None,
        offsale_min: int | None = None,
        offsale_max: int | None = None,
        voice: YesNoNoMatterScheme | None = None,
        age_group: list[str] | None = None,
        not_age_group: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/roblox"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email is not None:
            params["email"] = email
        if robux_min is not None:
            params["robux_min"] = robux_min
        if robux_max is not None:
            params["robux_max"] = robux_max
        if friends_min is not None:
            params["friends_min"] = friends_min
        if friends_max is not None:
            params["friends_max"] = friends_max
        if followers_min is not None:
            params["followers_min"] = followers_min
        if followers_max is not None:
            params["followers_max"] = followers_max
        if country is not None:
            params["country"] = country
        if not_country is not None:
            params["not_country"] = not_country
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        if xbox_connected is not None:
            params["xbox_connected"] = xbox_connected
        if psn_connected is not None:
            params["psn_connected"] = psn_connected
        if verified is not None:
            params["verified"] = verified
        if age_verified is not None:
            params["age_verified"] = age_verified
        if incoming_robux_total_min is not None:
            params["incoming_robux_total_min"] = incoming_robux_total_min
        if incoming_robux_total_max is not None:
            params["incoming_robux_total_max"] = incoming_robux_total_max
        if limited_price_min is not None:
            params["limited_price_min"] = limited_price_min
        if limited_price_max is not None:
            params["limited_price_max"] = limited_price_max
        if gamepass_min is not None:
            params["gamepass_min"] = gamepass_min
        if gamepass_max is not None:
            params["gamepass_max"] = gamepass_max
        if game_donations is not None:
            params["game_donations"] = game_donations
        if inv_min is not None:
            params["inv_min"] = inv_min
        if inv_max is not None:
            params["inv_max"] = inv_max
        if ugc_limited_price_min is not None:
            params["ugc_limited_price_min"] = ugc_limited_price_min
        if ugc_limited_price_max is not None:
            params["ugc_limited_price_max"] = ugc_limited_price_max
        if credit_balance_min is not None:
            params["credit_balance_min"] = credit_balance_min
        if credit_balance_max is not None:
            params["credit_balance_max"] = credit_balance_max
        if offsale_min is not None:
            params["offsale_min"] = offsale_min
        if offsale_max is not None:
            params["offsale_max"] = offsale_max
        if voice is not None:
            params["voice"] = voice
        if age_group is not None:
            params["age_group[]"] = age_group
        if not_age_group is not None:
            params["not_age_group[]"] = not_age_group
        return self._request("GET", path, params=params)

    def category_warface(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        rank_min: int | None = None,
        rank_max: int | None = None,
        bonus_rank_min: int | None = None,
        bonus_rank_max: int | None = None,
        tel: str | None = None,
        daybreak: int | None = None,
        kredits_min: int | None = None,
        kredits_max: int | None = None,
        total_kredits_min: int | None = None,
        total_kredits_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/warface"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if rank_min is not None:
            params["rank_min"] = rank_min
        if rank_max is not None:
            params["rank_max"] = rank_max
        if bonus_rank_min is not None:
            params["bonus_rank_min"] = bonus_rank_min
        if bonus_rank_max is not None:
            params["bonus_rank_max"] = bonus_rank_max
        if tel is not None:
            params["tel"] = tel
        if daybreak is not None:
            params["daybreak"] = daybreak
        if kredits_min is not None:
            params["kredits_min"] = kredits_min
        if kredits_max is not None:
            params["kredits_max"] = kredits_max
        if total_kredits_min is not None:
            params["total_kredits_min"] = total_kredits_min
        if total_kredits_max is not None:
            params["total_kredits_max"] = total_kredits_max
        return self._request("GET", path, params=params)

    def category_minecraft(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
        java: YesNoNoMatterScheme | None = None,
        bedrock: YesNoNoMatterScheme | None = None,
        dungeons: YesNoNoMatterScheme | None = None,
        legends: YesNoNoMatterScheme | None = None,
        change_nickname: YesNoNoMatterScheme | None = None,
        capes: list[str] | None = None,
        capes_min: int | None = None,
        capes_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        hypixel_ban: YesNoNoMatterScheme | None = None,
        hypixel_skyblock_api_enabled: YesNoNoMatterScheme | None = None,
        rank_hypixel: list[str] | None = None,
        level_hypixel_min: int | None = None,
        level_hypixel_max: int | None = None,
        achievement_hypixel_min: int | None = None,
        achievement_hypixel_max: int | None = None,
        level_hypixel_skyblock_min: int | None = None,
        level_hypixel_skyblock_max: int | None = None,
        net_worth_hypixel_skyblock_min: int | None = None,
        net_worth_hypixel_skyblock_max: int | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        last_login_hypixel: int | None = None,
        last_login_hypixel_period: str | None = None,
        can_change_details: YesNoNoMatterScheme | None = None,
        nickname_length_min: int | None = None,
        nickname_length_max: int | None = None,
        hypixel_ban_parsed: YesNoNoMatterScheme | None = None,
        minecoins_min: int | None = None,
        minecoins_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/minecraft"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        if java is not None:
            params["java"] = java
        if bedrock is not None:
            params["bedrock"] = bedrock
        if dungeons is not None:
            params["dungeons"] = dungeons
        if legends is not None:
            params["legends"] = legends
        if change_nickname is not None:
            params["change_nickname"] = change_nickname
        if capes is not None:
            params["capes[]"] = capes
        if capes_min is not None:
            params["capes_min"] = capes_min
        if capes_max is not None:
            params["capes_max"] = capes_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if hypixel_ban is not None:
            params["hypixel_ban"] = hypixel_ban
        if hypixel_skyblock_api_enabled is not None:
            params["hypixel_skyblock_api_enabled"] = hypixel_skyblock_api_enabled
        if rank_hypixel is not None:
            params["rank_hypixel[]"] = rank_hypixel
        if level_hypixel_min is not None:
            params["level_hypixel_min"] = level_hypixel_min
        if level_hypixel_max is not None:
            params["level_hypixel_max"] = level_hypixel_max
        if achievement_hypixel_min is not None:
            params["achievement_hypixel_min"] = achievement_hypixel_min
        if achievement_hypixel_max is not None:
            params["achievement_hypixel_max"] = achievement_hypixel_max
        if level_hypixel_skyblock_min is not None:
            params["level_hypixel_skyblock_min"] = level_hypixel_skyblock_min
        if level_hypixel_skyblock_max is not None:
            params["level_hypixel_skyblock_max"] = level_hypixel_skyblock_max
        if net_worth_hypixel_skyblock_min is not None:
            params["net_worth_hypixel_skyblock_min"] = net_worth_hypixel_skyblock_min
        if net_worth_hypixel_skyblock_max is not None:
            params["net_worth_hypixel_skyblock_max"] = net_worth_hypixel_skyblock_max
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if last_login_hypixel is not None:
            params["last_login_hypixel"] = last_login_hypixel
        if last_login_hypixel_period is not None:
            params["last_login_hypixel_period"] = last_login_hypixel_period
        if can_change_details is not None:
            params["can_change_details"] = can_change_details
        if nickname_length_min is not None:
            params["nickname_length_min"] = nickname_length_min
        if nickname_length_max is not None:
            params["nickname_length_max"] = nickname_length_max
        if hypixel_ban_parsed is not None:
            params["hypixel_ban_parsed"] = hypixel_ban_parsed
        if minecoins_min is not None:
            params["minecoins_min"] = minecoins_min
        if minecoins_max is not None:
            params["minecoins_max"] = minecoins_max
        return self._request("GET", path, params=params)

    def category_hytale(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        edition: list[str] | None = None,
        profiles_min: int | None = None,
        profiles_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/hytale"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if edition is not None:
            params["edition[]"] = edition
        if profiles_min is not None:
            params["profiles_min"] = profiles_min
        if profiles_max is not None:
            params["profiles_max"] = profiles_max
        return self._request("GET", path, params=params)

    def category_list(
        self,
        top_queries: bool | None = None,
    ) -> dict[str, Any]:
        path = "/category"
        params: dict[str, Any] = {}
        if top_queries is not None:
            params["top_queries"] = top_queries
        return self._request("GET", path, params=params)

    def category_params(
        self,
        categoryName: str,
    ) -> dict[str, Any]:
        path = "/{categoryName}/params"
        path = path.replace("{categoryName}", str(categoryName))
        return self._request("GET", path)

    def category_games(
        self,
        categoryName: str,
    ) -> dict[str, Any]:
        path = "/{categoryName}/games"
        path = path.replace("{categoryName}", str(categoryName))
        return self._request("GET", path)

    def list_user(
        self,
        user_id: int | None = None,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        show: str | None = None,
        delete_reason: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        login: str | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
        username: str | None = None,
        published_startDate: str | None = None,
        published_endDate: str | None = None,
        filter_by_published_date: bool | None = None,
        paid_startDate: str | None = None,
        paid_endDate: str | None = None,
        filter_by_buyer_operation_date: bool | None = None,
        delete_startDate: str | None = None,
        delete_endDate: str | None = None,
        filter_by_delete_date: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/items"
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if delete_reason is not None:
            params["delete_reason"] = delete_reason
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if login is not None:
            params["login"] = login
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if username is not None:
            params["username"] = username
        if published_startDate is not None:
            params["published_startDate"] = published_startDate
        if published_endDate is not None:
            params["published_endDate"] = published_endDate
        if filter_by_published_date is not None:
            params["filter_by_published_date"] = filter_by_published_date
        if paid_startDate is not None:
            params["paid_startDate"] = paid_startDate
        if paid_endDate is not None:
            params["paid_endDate"] = paid_endDate
        if filter_by_buyer_operation_date is not None:
            params["filter_by_buyer_operation_date"] = filter_by_buyer_operation_date
        if delete_startDate is not None:
            params["delete_startDate"] = delete_startDate
        if delete_endDate is not None:
            params["delete_endDate"] = delete_endDate
        if filter_by_delete_date is not None:
            params["filter_by_delete_date"] = filter_by_delete_date
        return self._request("GET", path, params=params)

    def list_orders(
        self,
        user_id: int | None = None,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        show: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        login: str | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/orders"
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if login is not None:
            params["login"] = login
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        return self._request("GET", path, params=params)

    def list_states(
        self,
        user_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/user/item-states"
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        return self._request("GET", path, params=params)

    def list_download(
        self,
        type_: str,
        format: str | None = None,
        custom_format: str | None = None,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        show: str | None = None,
        delete_reason: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
        username: str | None = None,
        published_startDate: str | None = None,
        published_endDate: str | None = None,
        filter_by_published_date: bool | None = None,
        paid_startDate: str | None = None,
        paid_endDate: str | None = None,
        filter_by_buyer_operation_date: bool | None = None,
        delete_startDate: str | None = None,
        delete_endDate: str | None = None,
        filter_by_delete_date: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/{type}/download"
        path = path.replace("{type}", str(type_))
        params: dict[str, Any] = {}
        if format is not None:
            params["format"] = format
        if custom_format is not None:
            params["custom_format"] = custom_format
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if delete_reason is not None:
            params["delete_reason"] = delete_reason
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if username is not None:
            params["username"] = username
        if published_startDate is not None:
            params["published_startDate"] = published_startDate
        if published_endDate is not None:
            params["published_endDate"] = published_endDate
        if filter_by_published_date is not None:
            params["filter_by_published_date"] = filter_by_published_date
        if paid_startDate is not None:
            params["paid_startDate"] = paid_startDate
        if paid_endDate is not None:
            params["paid_endDate"] = paid_endDate
        if filter_by_buyer_operation_date is not None:
            params["filter_by_buyer_operation_date"] = filter_by_buyer_operation_date
        if delete_startDate is not None:
            params["delete_startDate"] = delete_startDate
        if delete_endDate is not None:
            params["delete_endDate"] = delete_endDate
        if filter_by_delete_date is not None:
            params["filter_by_delete_date"] = filter_by_delete_date
        return self._request("GET", path, params=params)

    def list_favorites(
        self,
        page: int | None = None,
        show: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
    ) -> dict[str, Any]:
        path = "/fave"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        return self._request("GET", path, params=params)

    def list_viewed(
        self,
        page: int | None = None,
        show: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
    ) -> dict[str, Any]:
        path = "/viewed"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        return self._request("GET", path, params=params)

    def managing_get(
        self,
        item_id: int,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        return self._request("GET", path, params=params)

    def manging_delete(
        self,
        item_id: int,
        reason: str,
    ) -> dict[str, Any]:
        path = "/{item_id}"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if reason is not None:
            data["reason"] = reason
        return self._request("DELETE", path, json=data)

    def profile_claims(
        self,
        type_: str | None = None,
        claim_state: str | None = None,
    ) -> dict[str, Any]:
        path = "/claims"
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if claim_state is not None:
            params["claim_state"] = claim_state
        return self._request("GET", path, params=params)

    def managing_create_claim(
        self,
        item_id: ItemIDModel,
        post_body: str,
    ) -> dict[str, Any]:
        path = "/claims"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        if post_body is not None:
            data["post_body"] = post_body
        return self._request("POST", path, json=data)

    def managing_bulk_get(
        self,
        item_id: list[ItemIDModel] | None = None,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/bulk/items"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        if parse_same_item_ids is not None:
            data["parse_same_item_ids"] = parse_same_item_ids
        return self._request("POST", path, json=data)

    def managing_steam_inventory_value(
        self,
        item_id: int,
        app_id: int | None = None,
        currency: CurrencyModel | None = None,
        ignore_cache: bool | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/inventory-value"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if app_id is not None:
            params["app_id"] = app_id
        if currency is not None:
            params["currency"] = currency
        if ignore_cache is not None:
            params["ignore_cache"] = ignore_cache
        return self._request("GET", path, params=params)

    def managing_steam_value(
        self,
        link: str,
        app_id: int | None = None,
        currency: CurrencyModel | None = None,
        ignore_cache: bool | None = None,
    ) -> dict[str, Any]:
        path = "/steam-value"
        params: dict[str, Any] = {}
        if link is not None:
            params["link"] = link
        if app_id is not None:
            params["app_id"] = app_id
        if currency is not None:
            params["currency"] = currency
        if ignore_cache is not None:
            params["ignore_cache"] = ignore_cache
        return self._request("GET", path, params=params)

    def managing_steam_preview(
        self,
        item_id: int,
        type_: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/steam-preview"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        return self._request("GET", path, params=params)

    def managing_edit(
        self,
        item_id: int,
        title: str | None = None,
        title_en: str | None = None,
        price: int | None = None,
        currency: CurrencyModel | None = None,
        item_origin: str | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        allow_ask_discount: bool | None = None,
        proxy_id: int | None = None,
        description: str | None = None,
        information: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/edit"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if price is not None:
            data["price"] = price
        if currency is not None:
            data["currency"] = currency
        if item_origin is not None:
            data["item_origin"] = item_origin
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if allow_ask_discount is not None:
            data["allow_ask_discount"] = allow_ask_discount
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if description is not None:
            data["description"] = description
        if information is not None:
            data["information"] = information
        return self._request("PUT", path, json=data)

    def managing_ai_price(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/ai-price"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_auto_buy_price(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/auto-buy-price"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_note(
        self,
        item_id: int,
        text: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/note-save"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if text is not None:
            data["text"] = text
        return self._request("POST", path, json=data)

    def managing_steam_update_value(
        self,
        item_id: int,
        all: bool | None = None,
        app_id: int | None = None,
        authorize: bool | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/update-inventory"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if all is not None:
            data["all"] = all
        if app_id is not None:
            data["app_id"] = app_id
        if authorize is not None:
            data["authorize"] = authorize
        return self._request("POST", path, json=data)

    def managing_bump(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/bump"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_auto_bump(
        self,
        item_id: int,
        hour: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/auto-bump"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if hour is not None:
            data["hour"] = hour
        return self._request("POST", path, json=data)

    def managing_auto_bump_disable(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/auto-bump"
        path = path.replace("{item_id}", str(item_id))
        return self._request("DELETE", path)

    def managing_open(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/open"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_close(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/close"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_image(
        self,
        item_id: int,
        type_: str,
    ) -> dict[str, Any]:
        path = "/{item_id}/image"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        return self._request("GET", path, params=params)

    def cart_get(
        self,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/cart"
        params: dict[str, Any] = {}
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        return self._request("GET", path, params=params)

    def cart_add(
        self,
        item_id: ItemIDModel,
    ) -> dict[str, Any]:
        path = "/cart"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        return self._request("POST", path, json=data)

    def cart_delete(
        self,
        item_id: ItemIDModel | None = None,
    ) -> dict[str, Any]:
        path = "/cart"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        return self._request("DELETE", path, json=data)

    def purchasing_fast_buy(
        self,
        item_id: int,
        price: float | None = None,
        balance_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/fast-buy"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if price is not None:
            data["price"] = price
        if balance_id is not None:
            data["balance_id"] = balance_id
        return self._request("POST", path, json=data)

    def purchasing_check(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/check-account"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def purchasing_confirm(
        self,
        item_id: int,
        price: int | None = None,
        balance_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/confirm-buy"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if price is not None:
            data["price"] = price
        if balance_id is not None:
            data["balance_id"] = balance_id
        return self._request("POST", path, json=data)

    def purchasing_discount_request(
        self,
        item_id: int,
        discount_price: float,
        message: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/discount"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if discount_price is not None:
            data["discount_price"] = discount_price
        if message is not None:
            data["message"] = message
        return self._request("POST", path, json=data)

    def purchasing_discount_cancel(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/discount"
        path = path.replace("{item_id}", str(item_id))
        return self._request("DELETE", path)

    def custom_discounts_get(
        self,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        return self._request("GET", path)

    def custom_discounts_create(
        self,
        user_id: int,
        category_id: CategoryIDModel,
        discount_percent: float,
        min_price: float,
        max_price: float | None = None,
        currency: CurrencyModel | None = None,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        if category_id is not None:
            data["category_id"] = category_id
        if discount_percent is not None:
            data["discount_percent"] = discount_percent
        if min_price is not None:
            data["min_price"] = min_price
        if max_price is not None:
            data["max_price"] = max_price
        if currency is not None:
            data["currency"] = currency
        return self._request("POST", path, json=data)

    def custom_discounts_edit(
        self,
        discount_id: int,
        discount_percent: float | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if discount_id is not None:
            data["discount_id"] = discount_id
        if discount_percent is not None:
            data["discount_percent"] = discount_percent
        if min_price is not None:
            data["min_price"] = min_price
        if max_price is not None:
            data["max_price"] = max_price
        return self._request("PUT", path, json=data)

    def custom_discounts_delete(
        self,
        discount_id: int,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if discount_id is not None:
            data["discount_id"] = discount_id
        return self._request("DELETE", path, json=data)

    def publishing_fast_sell(
        self,
        price: float,
        category_id: int,
        currency: CurrencyModel,
        item_origin: str,
        title: str | None = None,
        title_en: str | None = None,
        extended_guarantee: int | None = None,
        allow_ask_discount: bool | None = None,
        proxy_id: int | None = None,
        random_proxy: schema | None = None,
        description: str | None = None,
        information: str | None = None,
        login: str | None = None,
        password: str | None = None,
        login_password: str | None = None,
        has_email_login_data: bool | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        extra: ExtraModel | None = None,
    ) -> dict[str, Any]:
        path = "/item/fast-sell"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if price is not None:
            data["price"] = price
        if category_id is not None:
            data["category_id"] = category_id
        if currency is not None:
            data["currency"] = currency
        if item_origin is not None:
            data["item_origin"] = item_origin
        if extended_guarantee is not None:
            data["extended_guarantee"] = extended_guarantee
        if allow_ask_discount is not None:
            data["allow_ask_discount"] = allow_ask_discount
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if random_proxy is not None:
            data["random_proxy"] = random_proxy
        if description is not None:
            data["description"] = description
        if information is not None:
            data["information"] = information
        if login is not None:
            data["login"] = login
        if password is not None:
            data["password"] = password
        if login_password is not None:
            data["login_password"] = login_password
        if has_email_login_data is not None:
            data["has_email_login_data"] = has_email_login_data
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if extra is not None:
            data["extra"] = extra
        return self._request("POST", path, json=data)

    def publishing_add(
        self,
        price: float,
        category_id: int,
        currency: CurrencyModel,
        item_origin: str,
        title: str | None = None,
        title_en: str | None = None,
        extended_guarantee: int | None = None,
        description: str | None = None,
        information: str | None = None,
        forceTempEmail: bool | None = None,
        resell_item_id: int | None = None,
        has_email_login_data: bool | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        allow_ask_discount: bool | None = None,
        proxy_id: int | None = None,
        random_proxy: schema | None = None,
    ) -> dict[str, Any]:
        path = "/item/add"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if price is not None:
            data["price"] = price
        if category_id is not None:
            data["category_id"] = category_id
        if currency is not None:
            data["currency"] = currency
        if item_origin is not None:
            data["item_origin"] = item_origin
        if extended_guarantee is not None:
            data["extended_guarantee"] = extended_guarantee
        if description is not None:
            data["description"] = description
        if information is not None:
            data["information"] = information
        if forceTempEmail is not None:
            data["forceTempEmail"] = forceTempEmail
        if resell_item_id is not None:
            data["resell_item_id"] = resell_item_id
        if has_email_login_data is not None:
            data["has_email_login_data"] = has_email_login_data
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if allow_ask_discount is not None:
            data["allow_ask_discount"] = allow_ask_discount
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if random_proxy is not None:
            data["random_proxy"] = random_proxy
        return self._request("POST", path, json=data)

    def publishing_check(
        self,
        item_id: int,
        resell_item_id: int | None = None,
        random_proxy: bool | None = None,
        login: str | None = None,
        password: str | None = None,
        login_password: str | None = None,
        has_email_login_data: bool | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        extra: ExtraModel | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/goods/check"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if resell_item_id is not None:
            data["resell_item_id"] = resell_item_id
        if random_proxy is not None:
            data["random_proxy"] = random_proxy
        if login is not None:
            data["login"] = login
        if password is not None:
            data["password"] = password
        if login_password is not None:
            data["login_password"] = login_password
        if has_email_login_data is not None:
            data["has_email_login_data"] = has_email_login_data
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if extra is not None:
            data["extra"] = extra
        return self._request("POST", path, json=data)

    def publishing_external(
        self,
        item_id: int,
        type_: str,
        login: str | None = None,
        email_login_data: str | None = None,
        cookies: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/external-account"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if type_ is not None:
            data["type"] = type_
        if login is not None:
            data["login"] = login
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if cookies is not None:
            data["cookies"] = cookies
        return self._request("POST", path, json=data)

    def managing_email_code(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/email-code"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_get_letters2(
        self,
        email_password: str | None = None,
        email: str | None = None,
        password: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        path = "/letters2"
        params: dict[str, Any] = {}
        if email_password is not None:
            params["email_password"] = email_password
        if email is not None:
            params["email"] = email
        if password is not None:
            params["password"] = password
        if limit is not None:
            params["limit"] = limit
        return self._request("GET", path, params=params)

    def managing_steam_get_mafile(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/mafile"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_steam_add_mafile(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/mafile"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_steam_remove_mafile(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/mafile"
        path = path.replace("{item_id}", str(item_id))
        return self._request("DELETE", path)

    def managing_steam_mafile_code(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/guard-code"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_steam_sda(
        self,
        item_id: int,
        id: int | None = None,
        nonce: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/confirm-sda"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if id is not None:
            data["id"] = id
        if nonce is not None:
            data["nonce"] = nonce
        return self._request("POST", path, json=data)

    def managing_telegram_code(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/telegram-login-code"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_telegram_reset_auth(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/telegram-reset-authorizations"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_refuse_guarantee(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/refuse-guarantee"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_decline_video_recording(
        self,
        item_id: int,
        i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item: bool,
    ) -> dict[str, Any]:
        path = "/{item_id}/decline-video-recording"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item is not None:
            data["i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item"] = i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item
        return self._request("POST", path, json=data)

    def managing_check_guarantee(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/check-guarantee"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_change_password(
        self,
        item_id: int,
        cancel: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/change-password"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if cancel is not None:
            data["_cancel"] = cancel
        return self._request("POST", path, json=data)

    def managing_temp_email_password(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/temp-email-password"
        path = path.replace("{item_id}", str(item_id))
        return self._request("GET", path)

    def managing_tag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return self._request("POST", path, json=data)

    def managing_untag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return self._request("DELETE", path, json=data)

    def managing_public_tag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/public-tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return self._request("POST", path, json=data)

    def managing_public_untag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/public-tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return self._request("DELETE", path, json=data)

    def managing_favorite(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/star"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_unfavorite(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/star"
        path = path.replace("{item_id}", str(item_id))
        return self._request("DELETE", path)

    def managing_stick(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/stick"
        path = path.replace("{item_id}", str(item_id))
        return self._request("POST", path)

    def managing_unstick(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/stick"
        path = path.replace("{item_id}", str(item_id))
        return self._request("DELETE", path)

    def managing_transfer(
        self,
        item_id: int,
        username: str,
        secret_answer: str,
    ) -> dict[str, Any]:
        path = "/{item_id}/change-owner"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if username is not None:
            data["username"] = username
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        return self._request("POST", path, json=data)

    def profile_get(
        self,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/me"
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._request("GET", path, params=params)

    def profile_edit(
        self,
        user: dict[str, Any] | None = None,
        option: dict[str, Any] | None = None,
        allow_accept_accounts: list[str] | None = None,
        telegram_api_id: str | None = None,
        telegram_api_hash: str | None = None,
        telegram_device_model: str | None = None,
        telegram_system_version: str | None = None,
        telegram_app_version: str | None = None,
        telegram_lang_pack: str | None = None,
        telegram_lang_code: str | None = None,
        telegram_system_lang_code: str | None = None,
        clear_telegram_client: bool | None = None,
    ) -> dict[str, Any]:
        path = "/me"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if user is not None:
            data["user"] = user
        if option is not None:
            data["option"] = option
        if allow_accept_accounts is not None:
            data["allow_accept_accounts"] = allow_accept_accounts
        if telegram_api_id is not None:
            data["telegram_api_id"] = telegram_api_id
        if telegram_api_hash is not None:
            data["telegram_api_hash"] = telegram_api_hash
        if telegram_device_model is not None:
            data["telegram_device_model"] = telegram_device_model
        if telegram_system_version is not None:
            data["telegram_system_version"] = telegram_system_version
        if telegram_app_version is not None:
            data["telegram_app_version"] = telegram_app_version
        if telegram_lang_pack is not None:
            data["telegram_lang_pack"] = telegram_lang_pack
        if telegram_lang_code is not None:
            data["telegram_lang_code"] = telegram_lang_code
        if telegram_system_lang_code is not None:
            data["telegram_system_lang_code"] = telegram_system_lang_code
        if clear_telegram_client is not None:
            data["clear_telegram_client"] = clear_telegram_client
        return self._request("PUT", path, json=data)

    def payments_invoice_get(
        self,
        invoice_id: int | None = None,
        payment_id: str | None = None,
    ) -> dict[str, Any]:
        path = "/invoice"
        params: dict[str, Any] = {}
        if invoice_id is not None:
            params["invoice_id"] = invoice_id
        if payment_id is not None:
            params["payment_id"] = payment_id
        return self._request("GET", path, params=params)

    def payments_invoice_create(
        self,
        currency: CurrencyModel,
        amount: float,
        payment_id: str,
        comment: str,
        url_success: str,
        merchant_id: int,
        url_callback: str | None = None,
        required_telegram_id: int | None = None,
        required_telegram_username: str | None = None,
        lifetime: float | None = 3600,
        additional_data: str | None = None,
        is_test: bool | None = None,
    ) -> dict[str, Any]:
        path = "/invoice"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if currency is not None:
            data["currency"] = currency
        if amount is not None:
            data["amount"] = amount
        if payment_id is not None:
            data["payment_id"] = payment_id
        if comment is not None:
            data["comment"] = comment
        if url_success is not None:
            data["url_success"] = url_success
        if url_callback is not None:
            data["url_callback"] = url_callback
        if merchant_id is not None:
            data["merchant_id"] = merchant_id
        if required_telegram_id is not None:
            data["required_telegram_id"] = required_telegram_id
        if required_telegram_username is not None:
            data["required_telegram_username"] = required_telegram_username
        if lifetime is not None:
            data["lifetime"] = lifetime
        if additional_data is not None:
            data["additional_data"] = additional_data
        if is_test is not None:
            data["is_test"] = is_test
        return self._request("POST", path, json=data)

    def payments_invoice_list(
        self,
        page: int | None = None,
        currency: CurrencyModel | None = None,
        status: str | None = None,
        amount: float | None = None,
        merchant_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/invoice/list"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if currency is not None:
            params["currency"] = currency
        if status is not None:
            params["status"] = status
        if amount is not None:
            params["amount"] = amount
        if merchant_id is not None:
            params["merchant_id"] = merchant_id
        return self._request("GET", path, params=params)

    def payments_currency(
        self,
    ) -> dict[str, Any]:
        path = "/currency"
        return self._request("GET", path)

    def payments_balance_list(
        self,
    ) -> dict[str, Any]:
        path = "/balance/exchange"
        return self._request("GET", path)

    def payments_balance_exchange(
        self,
        from_balance: str,
        to_balance: str,
        amount: int,
    ) -> dict[str, Any]:
        path = "/balance/exchange"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if from_balance is not None:
            data["from_balance"] = from_balance
        if to_balance is not None:
            data["to_balance"] = to_balance
        if amount is not None:
            data["amount"] = amount
        return self._request("POST", path, json=data)

    def payments_transfer(
        self,
        amount: int,
        currency: CurrencyModel,
        user_id: int | None = None,
        username: str | None = None,
        comment: str | None = None,
        telegram_deal: bool | None = None,
        telegram_username: str | None = None,
        transfer_hold: bool | None = None,
        hold_length_value: int | None = None,
        hold_length_option: str | None = None,
    ) -> dict[str, Any]:
        path = "/balance/transfer"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        if username is not None:
            data["username"] = username
        if amount is not None:
            data["amount"] = amount
        if currency is not None:
            data["currency"] = currency
        if comment is not None:
            data["comment"] = comment
        if telegram_deal is not None:
            data["telegram_deal"] = telegram_deal
        if telegram_username is not None:
            data["telegram_username"] = telegram_username
        if transfer_hold is not None:
            data["transfer_hold"] = transfer_hold
        if hold_length_value is not None:
            data["hold_length_value"] = hold_length_value
        if hold_length_option is not None:
            data["hold_length_option"] = hold_length_option
        return self._request("POST", path, json=data)

    def payments_fee(
        self,
        amount: float | None = None,
    ) -> dict[str, Any]:
        path = "/balance/transfer/fee"
        params: dict[str, Any] = {}
        if amount is not None:
            params["amount"] = amount
        return self._request("GET", path, params=params)

    def payments_cancel(
        self,
        payment_id: int,
    ) -> dict[str, Any]:
        path = "/balance/transfer/cancel"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if payment_id is not None:
            data["payment_id"] = payment_id
        return self._request("POST", path, json=data)

    def payments_history(
        self,
        type_: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        currency: CurrencyModel | None = None,
        page: int | None = None,
        operation_id_lt: int | None = None,
        receiver: str | None = None,
        sender: str | None = None,
        is_api: bool | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
        wallet: str | None = None,
        comment: str | None = None,
        is_hold: bool | None = None,
        show_payment_stats: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/payments"
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if currency is not None:
            params["currency"] = currency
        if page is not None:
            params["page"] = page
        if operation_id_lt is not None:
            params["operation_id_lt"] = operation_id_lt
        if receiver is not None:
            params["receiver"] = receiver
        if sender is not None:
            params["sender"] = sender
        if is_api is not None:
            params["is_api"] = is_api
        if startDate is not None:
            params["startDate"] = startDate
        if endDate is not None:
            params["endDate"] = endDate
        if wallet is not None:
            params["wallet"] = wallet
        if comment is not None:
            params["comment"] = comment
        if is_hold is not None:
            params["is_hold"] = is_hold
        if show_payment_stats is not None:
            params["show_payment_stats"] = show_payment_stats
        return self._request("GET", path, params=params)

    def auto_payments_list(
        self,
    ) -> dict[str, Any]:
        path = "/auto-payments"
        return self._request("GET", path)

    def auto_payments_create(
        self,
        username_receiver: str,
        day: int,
        amount: float,
        secret_answer: str | None = None,
        currency: CurrencyModel | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        path = "/auto-payment"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        if username_receiver is not None:
            data["username_receiver"] = username_receiver
        if day is not None:
            data["day"] = day
        if amount is not None:
            data["amount"] = amount
        if currency is not None:
            data["currency"] = currency
        if description is not None:
            data["description"] = description
        return self._request("POST", path, json=data)

    def auto_payments_delete(
        self,
        auto_payment_id: int,
    ) -> dict[str, Any]:
        path = "/auto-payment"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if auto_payment_id is not None:
            data["auto_payment_id"] = auto_payment_id
        return self._request("DELETE", path, json=data)

    def payments_payout_services(
        self,
    ) -> dict[str, Any]:
        path = "/balance/payout/services"
        return self._request("GET", path)

    def payments_payout(
        self,
        payment_system: str,
        wallet: str,
        amount: float,
        currency: CurrencyModel,
        include_fee: bool | None = None,
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        path = "/balance/payout"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if payment_system is not None:
            data["payment_system"] = payment_system
        if wallet is not None:
            data["wallet"] = wallet
        if amount is not None:
            data["amount"] = amount
        if currency is not None:
            data["currency"] = currency
        if include_fee is not None:
            data["include_fee"] = include_fee
        if extra is not None:
            data["extra"] = extra
        return self._request("POST", path, json=data)

    def proxy_get(
        self,
    ) -> dict[str, Any]:
        path = "/proxy"
        return self._request("GET", path)

    def proxy_add(
        self,
        proxy_ip: str | None = None,
        proxy_port: int | None = None,
        proxy_user: str | None = None,
        proxy_pass: str | None = None,
        proxy_row: str | None = None,
    ) -> dict[str, Any]:
        path = "/proxy"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if proxy_ip is not None:
            data["proxy_ip"] = proxy_ip
        if proxy_port is not None:
            data["proxy_port"] = proxy_port
        if proxy_user is not None:
            data["proxy_user"] = proxy_user
        if proxy_pass is not None:
            data["proxy_pass"] = proxy_pass
        if proxy_row is not None:
            data["proxy_row"] = proxy_row
        return self._request("POST", path, json=data)

    def proxy_delete(
        self,
        proxy_id: int | None = None,
        delete_all: bool | None = None,
    ) -> dict[str, Any]:
        path = "/proxy"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if delete_all is not None:
            data["delete_all"] = delete_all
        return self._request("DELETE", path, json=data)

    def imap_create(
        self,
        domain: str,
        imap_server: str,
        port: int,
        secure: bool,
    ) -> dict[str, Any]:
        path = "/imap"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if domain is not None:
            data["domain"] = domain
        if imap_server is not None:
            data["imap_server"] = imap_server
        if port is not None:
            data["port"] = port
        if secure is not None:
            data["secure"] = secure
        return self._request("POST", path, json=data)

    def imap_delete(
        self,
        domain: str,
    ) -> dict[str, Any]:
        path = "/imap"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if domain is not None:
            data["domain"] = domain
        return self._request("DELETE", path, json=data)

    def batch(
        self,
    ) -> dict[str, Any]:
        path = "/batch"
        return self._request("POST", path)


class AsyncMarketClient(AsyncBaseClient):
    def __init__(self, token: str, base_url: str = "https://prod-api.lzt.market", proxy: str | None = None, timeout: float = 30.0):
        super().__init__(token=token, base_url=base_url, proxy=proxy, timeout=timeout)

    async def category_all(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        return await self._request("GET", path, params=params)

    async def category_steam(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_type: list[str] | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        item_domain: str | None = None,
        game: list[int] | None = None,
        hours_played: dict[str, Any] | None = None,
        hours_played_max: dict[str, Any] | None = None,
        eg: int | None = None,
        vac: list[int] | None = None,
        vac_skip_game_check: bool | None = None,
        rt: str | None = "no",
        trade_ban: YesNoNoMatterScheme | None = None,
        trade_limit: YesNoNoMatterScheme | None = None,
        daybreak: int | None = None,
        limit: YesNoNoMatterScheme | None = None,
        mafile: YesNoNoMatterScheme | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        lmin: int | None = None,
        lmax: int | None = None,
        rmin: int | None = None,
        rmax: int | None = None,
        wingman_rmin: int | None = None,
        wingman_rmax: int | None = None,
        no_vac: bool | None = None,
        mm_ban: YesNoNoMatterScheme | None = None,
        balance_min: int | None = None,
        balance_max: int | None = None,
        inv_game: int | None = None,
        inv_min: float | None = None,
        inv_max: float | None = None,
        friends_min: int | None = None,
        friends_max: int | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        win_count_min: int | None = None,
        win_count_max: int | None = None,
        medal_id: list[int] | None = None,
        medal_operator_or: bool | None = None,
        medal_min: int | None = None,
        medal_max: int | None = None,
        gift: list[str] | None = None,
        gift_min: int | None = None,
        gift_max: int | None = None,
        recently_hours_min: int | None = None,
        recently_hours_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        cs2_profile_rank_min: int | None = None,
        cs2_profile_rank_max: int | None = None,
        solommr_min: int | None = None,
        solommr_max: int | None = None,
        d2_game_count_min: int | None = None,
        d2_game_count_max: int | None = None,
        d2_win_count_min: int | None = None,
        d2_win_count_max: int | None = None,
        d2_behavior_min: int | None = None,
        d2_behavior_max: int | None = None,
        faceit_lvl_min: int | None = None,
        faceit_lvl_max: int | None = None,
        points_min: int | None = None,
        points_max: int | None = None,
        relevant_gmin: int | None = None,
        relevant_gmax: int | None = None,
        last_trans_date: int | None = None,
        last_trans_date_period: str | None = None,
        last_trans_date_later: int | None = None,
        last_trans_date_period_later: DatePeriodModel | None = None,
        no_trans: bool | None = None,
        trans: bool | None = None,
        gifts_purchase_min: float | None = None,
        gifts_purchase_max: float | None = None,
        refunds_purchase_min: float | None = None,
        refunds_purchase_max: float | None = None,
        ingame_purchase_min: float | None = None,
        ingame_purchase_max: float | None = None,
        games_purchase_min: float | None = None,
        games_purchase_max: float | None = None,
        purchase_min: float | None = None,
        purchase_max: float | None = None,
        has_activated_keys: YesNoNoMatterScheme | None = None,
        elo_min: int | None = None,
        elo_max: int | None = None,
        cs2_map_rank: int | None = None,
        cs2_map_rmin: int | None = None,
        cs2_map_rmax: int | None = None,
        has_faceit: YesNoNoMatterScheme | None = None,
        faceit_csgo_lvl_min: int | None = None,
        faceit_csgo_lvl_max: int | None = None,
        rust_deaths_min: int | None = None,
        rust_deaths_max: int | None = None,
        rust_kills_min: int | None = None,
        rust_kills_max: int | None = None,
        d2_last_match_date: int | None = None,
        d2_last_match_date_period: str | None = None,
        cards_min: int | None = None,
        cards_max: int | None = None,
        cards_games_min: int | None = None,
        cards_games_max: int | None = None,
        skip_vac_inv: bool | None = None,
    ) -> dict[str, Any]:
        path = "/steam"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_type is not None:
            params["email_type[]"] = email_type
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if item_domain is not None:
            params["item_domain"] = item_domain
        if game is not None:
            params["game[]"] = game
        if hours_played is not None:
            params["hours_played"] = hours_played
        if hours_played_max is not None:
            params["hours_played_max"] = hours_played_max
        if eg is not None:
            params["eg"] = eg
        if vac is not None:
            params["vac[]"] = vac
        if vac_skip_game_check is not None:
            params["vac_skip_game_check"] = vac_skip_game_check
        if rt is not None:
            params["rt"] = rt
        if trade_ban is not None:
            params["trade_ban"] = trade_ban
        if trade_limit is not None:
            params["trade_limit"] = trade_limit
        if daybreak is not None:
            params["daybreak"] = daybreak
        if limit is not None:
            params["limit"] = limit
        if mafile is not None:
            params["mafile"] = mafile
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if lmin is not None:
            params["lmin"] = lmin
        if lmax is not None:
            params["lmax"] = lmax
        if rmin is not None:
            params["rmin"] = rmin
        if rmax is not None:
            params["rmax"] = rmax
        if wingman_rmin is not None:
            params["wingman_rmin"] = wingman_rmin
        if wingman_rmax is not None:
            params["wingman_rmax"] = wingman_rmax
        if no_vac is not None:
            params["no_vac"] = no_vac
        if mm_ban is not None:
            params["mm_ban"] = mm_ban
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        if inv_game is not None:
            params["inv_game"] = inv_game
        if inv_min is not None:
            params["inv_min"] = inv_min
        if inv_max is not None:
            params["inv_max"] = inv_max
        if friends_min is not None:
            params["friends_min"] = friends_min
        if friends_max is not None:
            params["friends_max"] = friends_max
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if win_count_min is not None:
            params["win_count_min"] = win_count_min
        if win_count_max is not None:
            params["win_count_max"] = win_count_max
        if medal_id is not None:
            params["medal_id[]"] = medal_id
        if medal_operator_or is not None:
            params["medal_operator_or"] = medal_operator_or
        if medal_min is not None:
            params["medal_min"] = medal_min
        if medal_max is not None:
            params["medal_max"] = medal_max
        if gift is not None:
            params["gift[]"] = gift
        if gift_min is not None:
            params["gift_min"] = gift_min
        if gift_max is not None:
            params["gift_max"] = gift_max
        if recently_hours_min is not None:
            params["recently_hours_min"] = recently_hours_min
        if recently_hours_max is not None:
            params["recently_hours_max"] = recently_hours_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if cs2_profile_rank_min is not None:
            params["cs2_profile_rank_min"] = cs2_profile_rank_min
        if cs2_profile_rank_max is not None:
            params["cs2_profile_rank_max"] = cs2_profile_rank_max
        if solommr_min is not None:
            params["solommr_min"] = solommr_min
        if solommr_max is not None:
            params["solommr_max"] = solommr_max
        if d2_game_count_min is not None:
            params["d2_game_count_min"] = d2_game_count_min
        if d2_game_count_max is not None:
            params["d2_game_count_max"] = d2_game_count_max
        if d2_win_count_min is not None:
            params["d2_win_count_min"] = d2_win_count_min
        if d2_win_count_max is not None:
            params["d2_win_count_max"] = d2_win_count_max
        if d2_behavior_min is not None:
            params["d2_behavior_min"] = d2_behavior_min
        if d2_behavior_max is not None:
            params["d2_behavior_max"] = d2_behavior_max
        if faceit_lvl_min is not None:
            params["faceit_lvl_min"] = faceit_lvl_min
        if faceit_lvl_max is not None:
            params["faceit_lvl_max"] = faceit_lvl_max
        if points_min is not None:
            params["points_min"] = points_min
        if points_max is not None:
            params["points_max"] = points_max
        if relevant_gmin is not None:
            params["relevant_gmin"] = relevant_gmin
        if relevant_gmax is not None:
            params["relevant_gmax"] = relevant_gmax
        if last_trans_date is not None:
            params["last_trans_date"] = last_trans_date
        if last_trans_date_period is not None:
            params["last_trans_date_period"] = last_trans_date_period
        if last_trans_date_later is not None:
            params["last_trans_date_later"] = last_trans_date_later
        if last_trans_date_period_later is not None:
            params["last_trans_date_period_later"] = last_trans_date_period_later
        if no_trans is not None:
            params["no_trans"] = no_trans
        if trans is not None:
            params["trans"] = trans
        if gifts_purchase_min is not None:
            params["gifts_purchase_min"] = gifts_purchase_min
        if gifts_purchase_max is not None:
            params["gifts_purchase_max"] = gifts_purchase_max
        if refunds_purchase_min is not None:
            params["refunds_purchase_min"] = refunds_purchase_min
        if refunds_purchase_max is not None:
            params["refunds_purchase_max"] = refunds_purchase_max
        if ingame_purchase_min is not None:
            params["ingame_purchase_min"] = ingame_purchase_min
        if ingame_purchase_max is not None:
            params["ingame_purchase_max"] = ingame_purchase_max
        if games_purchase_min is not None:
            params["games_purchase_min"] = games_purchase_min
        if games_purchase_max is not None:
            params["games_purchase_max"] = games_purchase_max
        if purchase_min is not None:
            params["purchase_min"] = purchase_min
        if purchase_max is not None:
            params["purchase_max"] = purchase_max
        if has_activated_keys is not None:
            params["has_activated_keys"] = has_activated_keys
        if elo_min is not None:
            params["elo_min"] = elo_min
        if elo_max is not None:
            params["elo_max"] = elo_max
        if cs2_map_rank is not None:
            params["cs2_map_rank"] = cs2_map_rank
        if cs2_map_rmin is not None:
            params["cs2_map_rmin"] = cs2_map_rmin
        if cs2_map_rmax is not None:
            params["cs2_map_rmax"] = cs2_map_rmax
        if has_faceit is not None:
            params["has_faceit"] = has_faceit
        if faceit_csgo_lvl_min is not None:
            params["faceit_csgo_lvl_min"] = faceit_csgo_lvl_min
        if faceit_csgo_lvl_max is not None:
            params["faceit_csgo_lvl_max"] = faceit_csgo_lvl_max
        if rust_deaths_min is not None:
            params["rust_deaths_min"] = rust_deaths_min
        if rust_deaths_max is not None:
            params["rust_deaths_max"] = rust_deaths_max
        if rust_kills_min is not None:
            params["rust_kills_min"] = rust_kills_min
        if rust_kills_max is not None:
            params["rust_kills_max"] = rust_kills_max
        if d2_last_match_date is not None:
            params["d2_last_match_date"] = d2_last_match_date
        if d2_last_match_date_period is not None:
            params["d2_last_match_date_period"] = d2_last_match_date_period
        if cards_min is not None:
            params["cards_min"] = cards_min
        if cards_max is not None:
            params["cards_max"] = cards_max
        if cards_games_min is not None:
            params["cards_games_min"] = cards_games_min
        if cards_games_max is not None:
            params["cards_games_max"] = cards_games_max
        if skip_vac_inv is not None:
            params["skip_vac_inv"] = skip_vac_inv
        return await self._request("GET", path, params=params)

    async def category_fortnite(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        email_type: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        temp_email: str | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        smin: int | None = None,
        smax: int | None = None,
        vbmin: int | None = None,
        vbmax: int | None = None,
        skin: list[str] | None = None,
        pickaxe: list[str] | None = None,
        glider: list[str] | None = None,
        dance: list[str] | None = None,
        change_email: str | None = None,
        platform: list[str] | None = None,
        skins_shop_min: int | None = None,
        skins_shop_max: int | None = None,
        pickaxes_shop_min: int | None = None,
        pickaxes_shop_max: int | None = None,
        dances_shop_min: int | None = None,
        dances_shop_max: int | None = None,
        gliders_shop_min: int | None = None,
        gliders_shop_max: int | None = None,
        skins_shop_vbmin: int | None = None,
        skins_shop_vbmax: int | None = None,
        pickaxes_shop_vbmin: int | None = None,
        pickaxes_shop_vbmax: int | None = None,
        dances_shop_vbmin: int | None = None,
        dances_shop_vbmax: int | None = None,
        gliders_shop_vbmin: int | None = None,
        gliders_shop_vbmax: int | None = None,
        bp: YesNoNoMatterScheme | None = None,
        lmin: int | None = None,
        lmax: int | None = None,
        bp_lmin: int | None = None,
        bp_lmax: int | None = None,
        last_trans_date: int | None = None,
        last_trans_date_period: str | None = None,
        no_trans: bool | None = None,
        xbox_linkable: YesNoNoMatterScheme | None = None,
        psn_linkable: YesNoNoMatterScheme | None = None,
        daybreak: int | None = None,
        rl_purchases: bool | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        refund_credits_min: int | None = None,
        refund_credits_max: int | None = None,
        pickaxe_min: int | None = None,
        pickaxe_max: int | None = None,
        dmin: int | None = None,
        dmax: int | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/fortnite"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if email_type is not None:
            params["email_type[]"] = email_type
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if temp_email is not None:
            params["temp_email"] = temp_email
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if smin is not None:
            params["smin"] = smin
        if smax is not None:
            params["smax"] = smax
        if vbmin is not None:
            params["vbmin"] = vbmin
        if vbmax is not None:
            params["vbmax"] = vbmax
        if skin is not None:
            params["skin[]"] = skin
        if pickaxe is not None:
            params["pickaxe[]"] = pickaxe
        if glider is not None:
            params["glider[]"] = glider
        if dance is not None:
            params["dance[]"] = dance
        if change_email is not None:
            params["change_email"] = change_email
        if platform is not None:
            params["platform[]"] = platform
        if skins_shop_min is not None:
            params["skins_shop_min"] = skins_shop_min
        if skins_shop_max is not None:
            params["skins_shop_max"] = skins_shop_max
        if pickaxes_shop_min is not None:
            params["pickaxes_shop_min"] = pickaxes_shop_min
        if pickaxes_shop_max is not None:
            params["pickaxes_shop_max"] = pickaxes_shop_max
        if dances_shop_min is not None:
            params["dances_shop_min"] = dances_shop_min
        if dances_shop_max is not None:
            params["dances_shop_max"] = dances_shop_max
        if gliders_shop_min is not None:
            params["gliders_shop_min"] = gliders_shop_min
        if gliders_shop_max is not None:
            params["gliders_shop_max"] = gliders_shop_max
        if skins_shop_vbmin is not None:
            params["skins_shop_vbmin"] = skins_shop_vbmin
        if skins_shop_vbmax is not None:
            params["skins_shop_vbmax"] = skins_shop_vbmax
        if pickaxes_shop_vbmin is not None:
            params["pickaxes_shop_vbmin"] = pickaxes_shop_vbmin
        if pickaxes_shop_vbmax is not None:
            params["pickaxes_shop_vbmax"] = pickaxes_shop_vbmax
        if dances_shop_vbmin is not None:
            params["dances_shop_vbmin"] = dances_shop_vbmin
        if dances_shop_vbmax is not None:
            params["dances_shop_vbmax"] = dances_shop_vbmax
        if gliders_shop_vbmin is not None:
            params["gliders_shop_vbmin"] = gliders_shop_vbmin
        if gliders_shop_vbmax is not None:
            params["gliders_shop_vbmax"] = gliders_shop_vbmax
        if bp is not None:
            params["bp"] = bp
        if lmin is not None:
            params["lmin"] = lmin
        if lmax is not None:
            params["lmax"] = lmax
        if bp_lmin is not None:
            params["bp_lmin"] = bp_lmin
        if bp_lmax is not None:
            params["bp_lmax"] = bp_lmax
        if last_trans_date is not None:
            params["last_trans_date"] = last_trans_date
        if last_trans_date_period is not None:
            params["last_trans_date_period"] = last_trans_date_period
        if no_trans is not None:
            params["no_trans"] = no_trans
        if xbox_linkable is not None:
            params["xbox_linkable"] = xbox_linkable
        if psn_linkable is not None:
            params["psn_linkable"] = psn_linkable
        if daybreak is not None:
            params["daybreak"] = daybreak
        if rl_purchases is not None:
            params["rl_purchases"] = rl_purchases
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if refund_credits_min is not None:
            params["refund_credits_min"] = refund_credits_min
        if refund_credits_max is not None:
            params["refund_credits_max"] = refund_credits_max
        if pickaxe_min is not None:
            params["pickaxe_min"] = pickaxe_min
        if pickaxe_max is not None:
            params["pickaxe_max"] = pickaxe_max
        if dmin is not None:
            params["dmin"] = dmin
        if dmax is not None:
            params["dmax"] = dmax
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        return await self._request("GET", path, params=params)

    async def category_mihoyo(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        email_type: list[str] | None = None,
        parse_same_item_ids: bool | None = None,
        item_domain: str | None = None,
        email: str | None = None,
        ea: YesNoNoMatterScheme | None = None,
        region: list[str] | None = None,
        not_region: list[str] | None = None,
        genshin_character: list[int] | None = None,
        genshin_character_constellations: dict[str, Any] | None = None,
        genshin_character_constellations_max: dict[str, Any] | None = None,
        genshin_weapon: list[int] | None = None,
        genshin_char_min: int | None = None,
        genshin_char_max: int | None = None,
        genshin_legendary_min: int | None = None,
        genshin_legendary_max: int | None = None,
        genshin_level_min: int | None = None,
        genshin_level_max: int | None = None,
        genshin_legendary_weapon_min: int | None = None,
        genshin_legendary_weapon_max: int | None = None,
        constellations_min: int | None = None,
        constellations_max: int | None = None,
        genshin_achievement_min: int | None = None,
        genshin_achievement_max: int | None = None,
        genshin_currency_min: int | None = None,
        genshin_currency_max: int | None = None,
        honkai_character: list[int] | None = None,
        honkai_character_eidolons: dict[str, Any] | None = None,
        honkai_character_eidolons_max: dict[str, Any] | None = None,
        honkai_weapon: list[int] | None = None,
        honkai_char_min: int | None = None,
        honkai_char_max: int | None = None,
        honkai_legendary_min: int | None = None,
        honkai_legendary_max: int | None = None,
        honkai_level_min: int | None = None,
        honkai_level_max: int | None = None,
        honkai_legendary_weapon_min: int | None = None,
        honkai_legendary_weapon_max: int | None = None,
        eidolons_min: int | None = None,
        eidolons_max: int | None = None,
        honkai_achievement_min: int | None = None,
        honkai_achievement_max: int | None = None,
        honkai_currency_min: int | None = None,
        honkai_currency_max: int | None = None,
        zenless_character: list[int] | None = None,
        zenless_character_cinemas: dict[str, Any] | None = None,
        zenless_character_cinemas_max: dict[str, Any] | None = None,
        zenless_weapon: list[int] | None = None,
        zenless_legendary_min: int | None = None,
        zenless_legendary_max: int | None = None,
        cinemas_min: int | None = None,
        cinemas_max: int | None = None,
        zenless_legendary_weapon_min: int | None = None,
        zenless_legendary_weapon_max: int | None = None,
        zenless_char_min: int | None = None,
        zenless_char_max: int | None = None,
        zenless_level_min: int | None = None,
        zenless_level_max: int | None = None,
        zenless_achievement_min: int | None = None,
        zenless_achievement_max: int | None = None,
        zenless_currency_min: int | None = None,
        zenless_currency_max: int | None = None,
        daybreak: int | None = None,
    ) -> dict[str, Any]:
        path = "/mihoyo"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if email_type is not None:
            params["email_type[]"] = email_type
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if item_domain is not None:
            params["item_domain"] = item_domain
        if email is not None:
            params["email"] = email
        if ea is not None:
            params["ea"] = ea
        if region is not None:
            params["region"] = region
        if not_region is not None:
            params["not_region"] = not_region
        if genshin_character is not None:
            params["genshin_character[]"] = genshin_character
        if genshin_character_constellations is not None:
            params["genshin_character_constellations"] = genshin_character_constellations
        if genshin_character_constellations_max is not None:
            params["genshin_character_constellations_max"] = genshin_character_constellations_max
        if genshin_weapon is not None:
            params["genshin_weapon[]"] = genshin_weapon
        if genshin_char_min is not None:
            params["genshin_char_min"] = genshin_char_min
        if genshin_char_max is not None:
            params["genshin_char_max"] = genshin_char_max
        if genshin_legendary_min is not None:
            params["genshin_legendary_min"] = genshin_legendary_min
        if genshin_legendary_max is not None:
            params["genshin_legendary_max"] = genshin_legendary_max
        if genshin_level_min is not None:
            params["genshin_level_min"] = genshin_level_min
        if genshin_level_max is not None:
            params["genshin_level_max"] = genshin_level_max
        if genshin_legendary_weapon_min is not None:
            params["genshin_legendary_weapon_min"] = genshin_legendary_weapon_min
        if genshin_legendary_weapon_max is not None:
            params["genshin_legendary_weapon_max"] = genshin_legendary_weapon_max
        if constellations_min is not None:
            params["constellations_min"] = constellations_min
        if constellations_max is not None:
            params["constellations_max"] = constellations_max
        if genshin_achievement_min is not None:
            params["genshin_achievement_min"] = genshin_achievement_min
        if genshin_achievement_max is not None:
            params["genshin_achievement_max"] = genshin_achievement_max
        if genshin_currency_min is not None:
            params["genshin_currency_min"] = genshin_currency_min
        if genshin_currency_max is not None:
            params["genshin_currency_max"] = genshin_currency_max
        if honkai_character is not None:
            params["honkai_character[]"] = honkai_character
        if honkai_character_eidolons is not None:
            params["honkai_character_eidolons"] = honkai_character_eidolons
        if honkai_character_eidolons_max is not None:
            params["honkai_character_eidolons_max"] = honkai_character_eidolons_max
        if honkai_weapon is not None:
            params["honkai_weapon[]"] = honkai_weapon
        if honkai_char_min is not None:
            params["honkai_char_min"] = honkai_char_min
        if honkai_char_max is not None:
            params["honkai_char_max"] = honkai_char_max
        if honkai_legendary_min is not None:
            params["honkai_legendary_min"] = honkai_legendary_min
        if honkai_legendary_max is not None:
            params["honkai_legendary_max"] = honkai_legendary_max
        if honkai_level_min is not None:
            params["honkai_level_min"] = honkai_level_min
        if honkai_level_max is not None:
            params["honkai_level_max"] = honkai_level_max
        if honkai_legendary_weapon_min is not None:
            params["honkai_legendary_weapon_min"] = honkai_legendary_weapon_min
        if honkai_legendary_weapon_max is not None:
            params["honkai_legendary_weapon_max"] = honkai_legendary_weapon_max
        if eidolons_min is not None:
            params["eidolons_min"] = eidolons_min
        if eidolons_max is not None:
            params["eidolons_max"] = eidolons_max
        if honkai_achievement_min is not None:
            params["honkai_achievement_min"] = honkai_achievement_min
        if honkai_achievement_max is not None:
            params["honkai_achievement_max"] = honkai_achievement_max
        if honkai_currency_min is not None:
            params["honkai_currency_min"] = honkai_currency_min
        if honkai_currency_max is not None:
            params["honkai_currency_max"] = honkai_currency_max
        if zenless_character is not None:
            params["zenless_character[]"] = zenless_character
        if zenless_character_cinemas is not None:
            params["zenless_character_cinemas"] = zenless_character_cinemas
        if zenless_character_cinemas_max is not None:
            params["zenless_character_cinemas_max"] = zenless_character_cinemas_max
        if zenless_weapon is not None:
            params["zenless_weapon[]"] = zenless_weapon
        if zenless_legendary_min is not None:
            params["zenless_legendary_min"] = zenless_legendary_min
        if zenless_legendary_max is not None:
            params["zenless_legendary_max"] = zenless_legendary_max
        if cinemas_min is not None:
            params["cinemas_min"] = cinemas_min
        if cinemas_max is not None:
            params["cinemas_max"] = cinemas_max
        if zenless_legendary_weapon_min is not None:
            params["zenless_legendary_weapon_min"] = zenless_legendary_weapon_min
        if zenless_legendary_weapon_max is not None:
            params["zenless_legendary_weapon_max"] = zenless_legendary_weapon_max
        if zenless_char_min is not None:
            params["zenless_char_min"] = zenless_char_min
        if zenless_char_max is not None:
            params["zenless_char_max"] = zenless_char_max
        if zenless_level_min is not None:
            params["zenless_level_min"] = zenless_level_min
        if zenless_level_max is not None:
            params["zenless_level_max"] = zenless_level_max
        if zenless_achievement_min is not None:
            params["zenless_achievement_min"] = zenless_achievement_min
        if zenless_achievement_max is not None:
            params["zenless_achievement_max"] = zenless_achievement_max
        if zenless_currency_min is not None:
            params["zenless_currency_min"] = zenless_currency_min
        if zenless_currency_max is not None:
            params["zenless_currency_max"] = zenless_currency_max
        if daybreak is not None:
            params["daybreak"] = daybreak
        return await self._request("GET", path, params=params)

    async def category_riot(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        rmin: int | None = None,
        rmax: int | None = None,
        last_rmin: int | None = None,
        last_rmax: int | None = None,
        previous_rmin: int | None = None,
        previous_rmax: int | None = None,
        weaponSkin: list[str] | None = None,
        buddy: list[str] | None = None,
        agent: list[str] | None = None,
        champion: list[str] | None = None,
        skin: list[str] | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        valorant_level_min: int | None = None,
        valorant_level_max: int | None = None,
        lol_level_min: int | None = None,
        lol_level_max: int | None = None,
        inv_min: int | None = None,
        inv_max: int | None = None,
        vp_min: int | None = None,
        vp_max: int | None = None,
        valorant_smin: int | None = None,
        valorant_smax: int | None = None,
        valorant_rank_type: list[str] | None = None,
        amin: int | None = None,
        amax: int | None = None,
        valorant_region: list[str] | None = None,
        valorant_not_region: list[str] | None = None,
        lol_region: list[str] | None = None,
        lol_not_region: list[str] | None = None,
        knife: bool | None = None,
        lol_smin: int | None = None,
        lol_smax: int | None = None,
        champion_min: int | None = None,
        champion_max: int | None = None,
        win_rate_min: int | None = None,
        win_rate_max: int | None = None,
        blue_min: int | None = None,
        blue_max: int | None = None,
        orange_min: int | None = None,
        orange_max: int | None = None,
        mythic_min: int | None = None,
        mythic_max: int | None = None,
        riot_min: int | None = None,
        riot_max: int | None = None,
        email: str | None = None,
        tel: str | None = None,
        valorant_knife_min: int | None = None,
        valorant_knife_max: int | None = None,
        rp_min: int | None = None,
        rp_max: int | None = None,
        fa_min: int | None = None,
        fa_max: int | None = None,
        lol_rank: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/riot"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if rmin is not None:
            params["rmin"] = rmin
        if rmax is not None:
            params["rmax"] = rmax
        if last_rmin is not None:
            params["last_rmin"] = last_rmin
        if last_rmax is not None:
            params["last_rmax"] = last_rmax
        if previous_rmin is not None:
            params["previous_rmin"] = previous_rmin
        if previous_rmax is not None:
            params["previous_rmax"] = previous_rmax
        if weaponSkin is not None:
            params["weaponSkin[]"] = weaponSkin
        if buddy is not None:
            params["buddy[]"] = buddy
        if agent is not None:
            params["agent[]"] = agent
        if champion is not None:
            params["champion[]"] = champion
        if skin is not None:
            params["skin[]"] = skin
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if valorant_level_min is not None:
            params["valorant_level_min"] = valorant_level_min
        if valorant_level_max is not None:
            params["valorant_level_max"] = valorant_level_max
        if lol_level_min is not None:
            params["lol_level_min"] = lol_level_min
        if lol_level_max is not None:
            params["lol_level_max"] = lol_level_max
        if inv_min is not None:
            params["inv_min"] = inv_min
        if inv_max is not None:
            params["inv_max"] = inv_max
        if vp_min is not None:
            params["vp_min"] = vp_min
        if vp_max is not None:
            params["vp_max"] = vp_max
        if valorant_smin is not None:
            params["valorant_smin"] = valorant_smin
        if valorant_smax is not None:
            params["valorant_smax"] = valorant_smax
        if valorant_rank_type is not None:
            params["valorant_rank_type[]"] = valorant_rank_type
        if amin is not None:
            params["amin"] = amin
        if amax is not None:
            params["amax"] = amax
        if valorant_region is not None:
            params["valorant_region[]"] = valorant_region
        if valorant_not_region is not None:
            params["valorant_not_region[]"] = valorant_not_region
        if lol_region is not None:
            params["lol_region[]"] = lol_region
        if lol_not_region is not None:
            params["lol_not_region[]"] = lol_not_region
        if knife is not None:
            params["knife"] = knife
        if lol_smin is not None:
            params["lol_smin"] = lol_smin
        if lol_smax is not None:
            params["lol_smax"] = lol_smax
        if champion_min is not None:
            params["champion_min"] = champion_min
        if champion_max is not None:
            params["champion_max"] = champion_max
        if win_rate_min is not None:
            params["win_rate_min"] = win_rate_min
        if win_rate_max is not None:
            params["win_rate_max"] = win_rate_max
        if blue_min is not None:
            params["blue_min"] = blue_min
        if blue_max is not None:
            params["blue_max"] = blue_max
        if orange_min is not None:
            params["orange_min"] = orange_min
        if orange_max is not None:
            params["orange_max"] = orange_max
        if mythic_min is not None:
            params["mythic_min"] = mythic_min
        if mythic_max is not None:
            params["mythic_max"] = mythic_max
        if riot_min is not None:
            params["riot_min"] = riot_min
        if riot_max is not None:
            params["riot_max"] = riot_max
        if email is not None:
            params["email"] = email
        if tel is not None:
            params["tel"] = tel
        if valorant_knife_min is not None:
            params["valorant_knife_min"] = valorant_knife_min
        if valorant_knife_max is not None:
            params["valorant_knife_max"] = valorant_knife_max
        if rp_min is not None:
            params["rp_min"] = rp_min
        if rp_max is not None:
            params["rp_max"] = rp_max
        if fa_min is not None:
            params["fa_min"] = fa_min
        if fa_max is not None:
            params["fa_max"] = fa_max
        if lol_rank is not None:
            params["lol_rank[]"] = lol_rank
        return await self._request("GET", path, params=params)

    async def category_telegram(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        spam: YesNoNoMatterScheme | None = None,
        password: YesNoNoMatterScheme | None = None,
        premium: str | None = None,
        premium_expiration: int | None = None,
        premium_expiration_period: str | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        min_channels: int | None = None,
        max_channels: int | None = None,
        min_chats: int | None = None,
        max_chats: int | None = None,
        min_conversations: int | None = None,
        max_conversations: int | None = None,
        min_admin: int | None = None,
        max_admin: int | None = None,
        min_admin_sub: int | None = None,
        max_admin_sub: int | None = None,
        dig_min: int | None = None,
        dig_max: int | None = None,
        min_contacts: int | None = None,
        max_contacts: int | None = None,
        min_stars: int | None = None,
        max_stars: int | None = None,
        birthday: int | None = None,
        birthday_period: str | None = None,
        birthday_after: int | None = None,
        birthday_after_period: str | None = None,
        min_id: int | None = None,
        max_id: int | None = None,
        allow_geo_spamblock: bool | None = None,
        min_gifts: int | None = None,
        max_gifts: int | None = None,
        min_nft_gifts: int | None = None,
        max_nft_gifts: int | None = None,
        min_gifts_stars: int | None = None,
        max_gifts_stars: int | None = None,
        min_gifts_convert_stars: int | None = None,
        max_gifts_convert_stars: int | None = None,
        dc_id: list[int] | None = None,
        not_dc_id: list[int] | None = None,
        email: str | None = None,
        min_bots: int | None = None,
        max_bots: int | None = None,
        min_bot_active_users: int | None = None,
        max_bot_active_users: int | None = None,
    ) -> dict[str, Any]:
        path = "/telegram"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if spam is not None:
            params["spam"] = spam
        if password is not None:
            params["password"] = password
        if premium is not None:
            params["premium"] = premium
        if premium_expiration is not None:
            params["premium_expiration"] = premium_expiration
        if premium_expiration_period is not None:
            params["premium_expiration_period"] = premium_expiration_period
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if min_channels is not None:
            params["min_channels"] = min_channels
        if max_channels is not None:
            params["max_channels"] = max_channels
        if min_chats is not None:
            params["min_chats"] = min_chats
        if max_chats is not None:
            params["max_chats"] = max_chats
        if min_conversations is not None:
            params["min_conversations"] = min_conversations
        if max_conversations is not None:
            params["max_conversations"] = max_conversations
        if min_admin is not None:
            params["min_admin"] = min_admin
        if max_admin is not None:
            params["max_admin"] = max_admin
        if min_admin_sub is not None:
            params["min_admin_sub"] = min_admin_sub
        if max_admin_sub is not None:
            params["max_admin_sub"] = max_admin_sub
        if dig_min is not None:
            params["dig_min"] = dig_min
        if dig_max is not None:
            params["dig_max"] = dig_max
        if min_contacts is not None:
            params["min_contacts"] = min_contacts
        if max_contacts is not None:
            params["max_contacts"] = max_contacts
        if min_stars is not None:
            params["min_stars"] = min_stars
        if max_stars is not None:
            params["max_stars"] = max_stars
        if birthday is not None:
            params["birthday"] = birthday
        if birthday_period is not None:
            params["birthday_period"] = birthday_period
        if birthday_after is not None:
            params["birthday_after"] = birthday_after
        if birthday_after_period is not None:
            params["birthday_after_period"] = birthday_after_period
        if min_id is not None:
            params["min_id"] = min_id
        if max_id is not None:
            params["max_id"] = max_id
        if allow_geo_spamblock is not None:
            params["allow_geo_spamblock"] = allow_geo_spamblock
        if min_gifts is not None:
            params["min_gifts"] = min_gifts
        if max_gifts is not None:
            params["max_gifts"] = max_gifts
        if min_nft_gifts is not None:
            params["min_nft_gifts"] = min_nft_gifts
        if max_nft_gifts is not None:
            params["max_nft_gifts"] = max_nft_gifts
        if min_gifts_stars is not None:
            params["min_gifts_stars"] = min_gifts_stars
        if max_gifts_stars is not None:
            params["max_gifts_stars"] = max_gifts_stars
        if min_gifts_convert_stars is not None:
            params["min_gifts_convert_stars"] = min_gifts_convert_stars
        if max_gifts_convert_stars is not None:
            params["max_gifts_convert_stars"] = max_gifts_convert_stars
        if dc_id is not None:
            params["dc_id[]"] = dc_id
        if not_dc_id is not None:
            params["not_dc_id[]"] = not_dc_id
        if email is not None:
            params["email"] = email
        if min_bots is not None:
            params["min_bots"] = min_bots
        if max_bots is not None:
            params["max_bots"] = max_bots
        if min_bot_active_users is not None:
            params["min_bot_active_users"] = min_bot_active_users
        if max_bot_active_users is not None:
            params["max_bot_active_users"] = max_bot_active_users
        return await self._request("GET", path, params=params)

    async def category_supercell(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        daybreak: int | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        tel: YesNoNoMatterScheme | None = None,
        brawl_level_min: int | None = None,
        brawl_level_max: int | None = None,
        brawl_cup_min: int | None = None,
        brawl_cup_max: int | None = None,
        brawl_wins_min: int | None = None,
        brawl_wins_max: int | None = None,
        brawl_pass: YesNoNoMatterScheme | None = None,
        brawler: list[str] | None = None,
        brawlers_min: int | None = None,
        brawlers_max: int | None = None,
        legendary_brawlers_min: int | None = None,
        legendary_brawlers_max: int | None = None,
        royale_level_min: int | None = None,
        royale_level_max: int | None = None,
        royale_cup_min: int | None = None,
        royale_cup_max: int | None = None,
        royale_wins_min: int | None = None,
        royale_wins_max: int | None = None,
        king_level_min: int | None = None,
        king_level_max: int | None = None,
        royale_pass: YesNoNoMatterScheme | None = None,
        clash_level_min: int | None = None,
        clash_level_max: int | None = None,
        clash_cup_min: int | None = None,
        clash_cup_max: int | None = None,
        clash_wins_min: int | None = None,
        clash_wins_max: int | None = None,
        clash_pass: YesNoNoMatterScheme | None = None,
        total_heroes_level_min: int | None = None,
        total_heroes_level_max: int | None = None,
        total_troops_level_min: int | None = None,
        total_troops_level_max: int | None = None,
        total_spells_level_min: int | None = None,
        total_spells_level_max: int | None = None,
        total_builder_heroes_level_min: int | None = None,
        total_builder_heroes_level_max: int | None = None,
        total_builder_troops_level_min: int | None = None,
        total_builder_troops_level_max: int | None = None,
        town_hall_level_min: int | None = None,
        town_hall_level_max: int | None = None,
        builder_hall_level_min: int | None = None,
        builder_hall_level_max: int | None = None,
        builder_hall_cup_min: int | None = None,
        builder_hall_cup_max: int | None = None,
        creation_year_min: int | None = None,
        creation_year_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/supercell"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if daybreak is not None:
            params["daybreak"] = daybreak
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if tel is not None:
            params["tel"] = tel
        if brawl_level_min is not None:
            params["brawl_level_min"] = brawl_level_min
        if brawl_level_max is not None:
            params["brawl_level_max"] = brawl_level_max
        if brawl_cup_min is not None:
            params["brawl_cup_min"] = brawl_cup_min
        if brawl_cup_max is not None:
            params["brawl_cup_max"] = brawl_cup_max
        if brawl_wins_min is not None:
            params["brawl_wins_min"] = brawl_wins_min
        if brawl_wins_max is not None:
            params["brawl_wins_max"] = brawl_wins_max
        if brawl_pass is not None:
            params["brawl_pass"] = brawl_pass
        if brawler is not None:
            params["brawler[]"] = brawler
        if brawlers_min is not None:
            params["brawlers_min"] = brawlers_min
        if brawlers_max is not None:
            params["brawlers_max"] = brawlers_max
        if legendary_brawlers_min is not None:
            params["legendary_brawlers_min"] = legendary_brawlers_min
        if legendary_brawlers_max is not None:
            params["legendary_brawlers_max"] = legendary_brawlers_max
        if royale_level_min is not None:
            params["royale_level_min"] = royale_level_min
        if royale_level_max is not None:
            params["royale_level_max"] = royale_level_max
        if royale_cup_min is not None:
            params["royale_cup_min"] = royale_cup_min
        if royale_cup_max is not None:
            params["royale_cup_max"] = royale_cup_max
        if royale_wins_min is not None:
            params["royale_wins_min"] = royale_wins_min
        if royale_wins_max is not None:
            params["royale_wins_max"] = royale_wins_max
        if king_level_min is not None:
            params["king_level_min"] = king_level_min
        if king_level_max is not None:
            params["king_level_max"] = king_level_max
        if royale_pass is not None:
            params["royale_pass"] = royale_pass
        if clash_level_min is not None:
            params["clash_level_min"] = clash_level_min
        if clash_level_max is not None:
            params["clash_level_max"] = clash_level_max
        if clash_cup_min is not None:
            params["clash_cup_min"] = clash_cup_min
        if clash_cup_max is not None:
            params["clash_cup_max"] = clash_cup_max
        if clash_wins_min is not None:
            params["clash_wins_min"] = clash_wins_min
        if clash_wins_max is not None:
            params["clash_wins_max"] = clash_wins_max
        if clash_pass is not None:
            params["clash_pass"] = clash_pass
        if total_heroes_level_min is not None:
            params["total_heroes_level_min"] = total_heroes_level_min
        if total_heroes_level_max is not None:
            params["total_heroes_level_max"] = total_heroes_level_max
        if total_troops_level_min is not None:
            params["total_troops_level_min"] = total_troops_level_min
        if total_troops_level_max is not None:
            params["total_troops_level_max"] = total_troops_level_max
        if total_spells_level_min is not None:
            params["total_spells_level_min"] = total_spells_level_min
        if total_spells_level_max is not None:
            params["total_spells_level_max"] = total_spells_level_max
        if total_builder_heroes_level_min is not None:
            params["total_builder_heroes_level_min"] = total_builder_heroes_level_min
        if total_builder_heroes_level_max is not None:
            params["total_builder_heroes_level_max"] = total_builder_heroes_level_max
        if total_builder_troops_level_min is not None:
            params["total_builder_troops_level_min"] = total_builder_troops_level_min
        if total_builder_troops_level_max is not None:
            params["total_builder_troops_level_max"] = total_builder_troops_level_max
        if town_hall_level_min is not None:
            params["town_hall_level_min"] = town_hall_level_min
        if town_hall_level_max is not None:
            params["town_hall_level_max"] = town_hall_level_max
        if builder_hall_level_min is not None:
            params["builder_hall_level_min"] = builder_hall_level_min
        if builder_hall_level_max is not None:
            params["builder_hall_level_max"] = builder_hall_level_max
        if builder_hall_cup_min is not None:
            params["builder_hall_cup_min"] = builder_hall_cup_min
        if builder_hall_cup_max is not None:
            params["builder_hall_cup_max"] = builder_hall_cup_max
        if creation_year_min is not None:
            params["creation_year_min"] = creation_year_min
        if creation_year_max is not None:
            params["creation_year_max"] = creation_year_max
        return await self._request("GET", path, params=params)

    async def category_ea(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        game: list[str] | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        al_rank_min: int | None = None,
        al_rank_max: int | None = None,
        al_level_min: int | None = None,
        al_level_max: int | None = None,
        has_ban: YesNoNoMatterScheme | None = None,
        xbox_connected: YesNoNoMatterScheme | None = None,
        steam_connected: YesNoNoMatterScheme | None = None,
        psn_connected: YesNoNoMatterScheme | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        hours_played: dict[str, Any] | None = None,
        hours_played_max: dict[str, Any] | None = None,
        transactions: YesNoNoMatterScheme | None = None,
    ) -> dict[str, Any]:
        path = "/ea"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if game is not None:
            params["game[]"] = game
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if al_rank_min is not None:
            params["al_rank_min"] = al_rank_min
        if al_rank_max is not None:
            params["al_rank_max"] = al_rank_max
        if al_level_min is not None:
            params["al_level_min"] = al_level_min
        if al_level_max is not None:
            params["al_level_max"] = al_level_max
        if has_ban is not None:
            params["has_ban"] = has_ban
        if xbox_connected is not None:
            params["xbox_connected"] = xbox_connected
        if steam_connected is not None:
            params["steam_connected"] = steam_connected
        if psn_connected is not None:
            params["psn_connected"] = psn_connected
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if hours_played is not None:
            params["hours_played"] = hours_played
        if hours_played_max is not None:
            params["hours_played_max"] = hours_played_max
        if transactions is not None:
            params["transactions"] = transactions
        return await self._request("GET", path, params=params)

    async def category_wot(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        daybreak: int | None = None,
        battles_min: int | None = None,
        battles_max: int | None = None,
        gold_min: int | None = None,
        gold_max: int | None = None,
        silver_min: int | None = None,
        silver_max: int | None = None,
        top_min: int | None = None,
        top_max: int | None = None,
        prem_min: int | None = None,
        prem_max: int | None = None,
        top_prem_min: int | None = None,
        top_prem_max: int | None = None,
        win_pmin: int | None = None,
        win_pmax: int | None = None,
        tank: list[int] | None = None,
        region: list[str] | None = None,
        not_region: list[str] | None = None,
        premium: str | None = None,
        premium_expiration: int | None = None,
        premium_expiration_period: str | None = None,
        clan: str | None = None,
        clan_role: list[str] | None = None,
        not_clan_role: list[str] | None = None,
        clan_gold_min: int | None = None,
        clan_gold_max: int | None = None,
        clan_credits_min: int | None = None,
        clan_credits_max: int | None = None,
        clan_crystal_min: int | None = None,
        clan_crystal_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/world-of-tanks"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if daybreak is not None:
            params["daybreak"] = daybreak
        if battles_min is not None:
            params["battles_min"] = battles_min
        if battles_max is not None:
            params["battles_max"] = battles_max
        if gold_min is not None:
            params["gold_min"] = gold_min
        if gold_max is not None:
            params["gold_max"] = gold_max
        if silver_min is not None:
            params["silver_min"] = silver_min
        if silver_max is not None:
            params["silver_max"] = silver_max
        if top_min is not None:
            params["top_min"] = top_min
        if top_max is not None:
            params["top_max"] = top_max
        if prem_min is not None:
            params["prem_min"] = prem_min
        if prem_max is not None:
            params["prem_max"] = prem_max
        if top_prem_min is not None:
            params["top_prem_min"] = top_prem_min
        if top_prem_max is not None:
            params["top_prem_max"] = top_prem_max
        if win_pmin is not None:
            params["win_pmin"] = win_pmin
        if win_pmax is not None:
            params["win_pmax"] = win_pmax
        if tank is not None:
            params["tank[]"] = tank
        if region is not None:
            params["region[]"] = region
        if not_region is not None:
            params["not_region[]"] = not_region
        if premium is not None:
            params["premium"] = premium
        if premium_expiration is not None:
            params["premium_expiration"] = premium_expiration
        if premium_expiration_period is not None:
            params["premium_expiration_period"] = premium_expiration_period
        if clan is not None:
            params["clan"] = clan
        if clan_role is not None:
            params["clan_role[]"] = clan_role
        if not_clan_role is not None:
            params["not_clan_role[]"] = not_clan_role
        if clan_gold_min is not None:
            params["clan_gold_min"] = clan_gold_min
        if clan_gold_max is not None:
            params["clan_gold_max"] = clan_gold_max
        if clan_credits_min is not None:
            params["clan_credits_min"] = clan_credits_min
        if clan_credits_max is not None:
            params["clan_credits_max"] = clan_credits_max
        if clan_crystal_min is not None:
            params["clan_crystal_min"] = clan_crystal_min
        if clan_crystal_max is not None:
            params["clan_crystal_max"] = clan_crystal_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        return await self._request("GET", path, params=params)

    async def category_wot_blitz(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        daybreak: int | None = None,
        battles_min: int | None = None,
        battles_max: int | None = None,
        gold_min: int | None = None,
        gold_max: int | None = None,
        silver_min: int | None = None,
        silver_max: int | None = None,
        top_min: int | None = None,
        top_max: int | None = None,
        prem_min: int | None = None,
        prem_max: int | None = None,
        top_prem_min: int | None = None,
        top_prem_max: int | None = None,
        win_pmin: int | None = None,
        win_pmax: int | None = None,
        tank: list[int] | None = None,
        region: list[str] | None = None,
        not_region: list[str] | None = None,
        premium: str | None = None,
        premium_expiration: int | None = None,
        premium_expiration_period: str | None = None,
        clan: str | None = None,
        clan_role: list[str] | None = None,
        not_clan_role: list[str] | None = None,
        clan_gold_min: int | None = None,
        clan_gold_max: int | None = None,
        clan_credits_min: int | None = None,
        clan_credits_max: int | None = None,
        clan_crystal_min: int | None = None,
        clan_crystal_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/wot-blitz"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if daybreak is not None:
            params["daybreak"] = daybreak
        if battles_min is not None:
            params["battles_min"] = battles_min
        if battles_max is not None:
            params["battles_max"] = battles_max
        if gold_min is not None:
            params["gold_min"] = gold_min
        if gold_max is not None:
            params["gold_max"] = gold_max
        if silver_min is not None:
            params["silver_min"] = silver_min
        if silver_max is not None:
            params["silver_max"] = silver_max
        if top_min is not None:
            params["top_min"] = top_min
        if top_max is not None:
            params["top_max"] = top_max
        if prem_min is not None:
            params["prem_min"] = prem_min
        if prem_max is not None:
            params["prem_max"] = prem_max
        if top_prem_min is not None:
            params["top_prem_min"] = top_prem_min
        if top_prem_max is not None:
            params["top_prem_max"] = top_prem_max
        if win_pmin is not None:
            params["win_pmin"] = win_pmin
        if win_pmax is not None:
            params["win_pmax"] = win_pmax
        if tank is not None:
            params["tank[]"] = tank
        if region is not None:
            params["region[]"] = region
        if not_region is not None:
            params["not_region[]"] = not_region
        if premium is not None:
            params["premium"] = premium
        if premium_expiration is not None:
            params["premium_expiration"] = premium_expiration
        if premium_expiration_period is not None:
            params["premium_expiration_period"] = premium_expiration_period
        if clan is not None:
            params["clan"] = clan
        if clan_role is not None:
            params["clan_role[]"] = clan_role
        if not_clan_role is not None:
            params["not_clan_role[]"] = not_clan_role
        if clan_gold_min is not None:
            params["clan_gold_min"] = clan_gold_min
        if clan_gold_max is not None:
            params["clan_gold_max"] = clan_gold_max
        if clan_credits_min is not None:
            params["clan_credits_min"] = clan_credits_min
        if clan_credits_max is not None:
            params["clan_credits_max"] = clan_credits_max
        if clan_crystal_min is not None:
            params["clan_crystal_min"] = clan_crystal_min
        if clan_crystal_max is not None:
            params["clan_crystal_max"] = clan_crystal_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        return await self._request("GET", path, params=params)

    async def category_gifts(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
    ) -> dict[str, Any]:
        path = "/gifts"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        return await self._request("GET", path, params=params)

    async def category_epic_games(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        game: list[str] | None = None,
        change_email: str | None = None,
        rl_purchases: bool | None = None,
        balance_min: float | None = None,
        balance_max: float | None = None,
        rewards_balance_min: float | None = None,
        rewards_balance_max: float | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        hours_played: dict[str, Any] | None = None,
        hours_played_max: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        path = "/epicgames"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if game is not None:
            params["game[]"] = game
        if change_email is not None:
            params["change_email"] = change_email
        if rl_purchases is not None:
            params["rl_purchases"] = rl_purchases
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        if rewards_balance_min is not None:
            params["rewards_balance_min"] = rewards_balance_min
        if rewards_balance_max is not None:
            params["rewards_balance_max"] = rewards_balance_max
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if hours_played is not None:
            params["hours_played"] = hours_played
        if hours_played_max is not None:
            params["hours_played_max"] = hours_played_max
        return await self._request("GET", path, params=params)

    async def category_escape_from_tarkov(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        region: str | None = None,
        version: list[str] | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        level_min: int | None = None,
        level_max: int | None = None,
        pve: YesNoNoMatterScheme | None = None,
        side: str | None = None,
    ) -> dict[str, Any]:
        path = "/escape-from-tarkov"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if region is not None:
            params["region"] = region
        if version is not None:
            params["version[]"] = version
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if level_min is not None:
            params["level_min"] = level_min
        if level_max is not None:
            params["level_max"] = level_max
        if pve is not None:
            params["pve"] = pve
        if side is not None:
            params["side"] = side
        return await self._request("GET", path, params=params)

    async def category_social_club(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        daybreak: int | None = None,
        level_min: int | None = None,
        level_max: int | None = None,
        cash_min: int | None = None,
        cash_max: int | None = None,
        bank_cash_min: int | None = None,
        bank_cash_max: int | None = None,
        game: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/socialclub"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if daybreak is not None:
            params["daybreak"] = daybreak
        if level_min is not None:
            params["level_min"] = level_min
        if level_max is not None:
            params["level_max"] = level_max
        if cash_min is not None:
            params["cash_min"] = cash_min
        if cash_max is not None:
            params["cash_max"] = cash_max
        if bank_cash_min is not None:
            params["bank_cash_min"] = bank_cash_min
        if bank_cash_max is not None:
            params["bank_cash_max"] = bank_cash_max
        if game is not None:
            params["game[]"] = game
        return await self._request("GET", path, params=params)

    async def category_uplay(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        game: list[str] | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        daybreak: int | None = None,
        gmin: int | None = None,
        gmax: int | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        r6_level_min: int | None = None,
        r6_level_max: int | None = None,
        r6_rank_min: int | None = None,
        r6_rank_max: int | None = None,
        r6_operators_min: int | None = None,
        r6_operators_max: int | None = None,
        r6_ban: YesNoNoMatterScheme | None = None,
        r6_smin: int | None = None,
        r6_smax: int | None = None,
        r6_skin: list[str] | None = None,
        r6_operator: list[str] | None = None,
        xbox_connected: YesNoNoMatterScheme | None = None,
        psn_connected: YesNoNoMatterScheme | None = None,
        steam_connected: YesNoNoMatterScheme | None = None,
        balance_min: float | None = None,
        balance_max: float | None = None,
        transactions: YesNoNoMatterScheme | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
    ) -> dict[str, Any]:
        path = "/uplay"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if game is not None:
            params["game[]"] = game
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if daybreak is not None:
            params["daybreak"] = daybreak
        if gmin is not None:
            params["gmin"] = gmin
        if gmax is not None:
            params["gmax"] = gmax
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if r6_level_min is not None:
            params["r6_level_min"] = r6_level_min
        if r6_level_max is not None:
            params["r6_level_max"] = r6_level_max
        if r6_rank_min is not None:
            params["r6_rank_min"] = r6_rank_min
        if r6_rank_max is not None:
            params["r6_rank_max"] = r6_rank_max
        if r6_operators_min is not None:
            params["r6_operators_min"] = r6_operators_min
        if r6_operators_max is not None:
            params["r6_operators_max"] = r6_operators_max
        if r6_ban is not None:
            params["r6_ban"] = r6_ban
        if r6_smin is not None:
            params["r6_smin"] = r6_smin
        if r6_smax is not None:
            params["r6_smax"] = r6_smax
        if r6_skin is not None:
            params["r6_skin[]"] = r6_skin
        if r6_operator is not None:
            params["r6_operator[]"] = r6_operator
        if xbox_connected is not None:
            params["xbox_connected"] = xbox_connected
        if psn_connected is not None:
            params["psn_connected"] = psn_connected
        if steam_connected is not None:
            params["steam_connected"] = steam_connected
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        if transactions is not None:
            params["transactions"] = transactions
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        return await self._request("GET", path, params=params)

    async def category_discord(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        nitro: YesNoNoMatterScheme | None = None,
        nitro_type: list[str] | None = None,
        nitro_length: int | None = None,
        nitro_period: str | None = None,
        boosts_min: int | None = None,
        boosts_max: int | None = None,
        billing: YesNoNoMatterScheme | None = None,
        gifts: YesNoNoMatterScheme | None = None,
        transactions: YesNoNoMatterScheme | None = None,
        badge: list[str] | None = None,
        condition: list[str] | None = None,
        chat_min: int | None = None,
        chat_max: int | None = None,
        min_admin_members: int | None = None,
        max_admin_members: int | None = None,
        min_admin: int | None = None,
        max_admin: int | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        language: list[str] | None = None,
        not_language: list[str] | None = None,
        clans: YesNoNoMatterScheme | None = None,
        min_admin_clans: int | None = None,
        max_admin_clans: int | None = None,
        min_owner_clans: int | None = None,
        max_owner_clans: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        min_servers: int | None = None,
        max_servers: int | None = None,
        p_2fa: YesNoNoMatterScheme | None = None,
        min_full_credits: int | None = None,
        max_full_credits: int | None = None,
        min_basic_credits: int | None = None,
        max_basic_credits: int | None = None,
        min_orbs: int | None = None,
        max_orbs: int | None = None,
    ) -> dict[str, Any]:
        path = "/discord"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if nitro is not None:
            params["nitro"] = nitro
        if nitro_type is not None:
            params["nitro_type[]"] = nitro_type
        if nitro_length is not None:
            params["nitro_length"] = nitro_length
        if nitro_period is not None:
            params["nitro_period"] = nitro_period
        if boosts_min is not None:
            params["boosts_min"] = boosts_min
        if boosts_max is not None:
            params["boosts_max"] = boosts_max
        if billing is not None:
            params["billing"] = billing
        if gifts is not None:
            params["gifts"] = gifts
        if transactions is not None:
            params["transactions"] = transactions
        if badge is not None:
            params["badge[]"] = badge
        if condition is not None:
            params["condition[]"] = condition
        if chat_min is not None:
            params["chat_min"] = chat_min
        if chat_max is not None:
            params["chat_max"] = chat_max
        if min_admin_members is not None:
            params["min_admin_members"] = min_admin_members
        if max_admin_members is not None:
            params["max_admin_members"] = max_admin_members
        if min_admin is not None:
            params["min_admin"] = min_admin
        if max_admin is not None:
            params["max_admin"] = max_admin
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if language is not None:
            params["language[]"] = language
        if not_language is not None:
            params["not_language[]"] = not_language
        if clans is not None:
            params["clans"] = clans
        if min_admin_clans is not None:
            params["min_admin_clans"] = min_admin_clans
        if max_admin_clans is not None:
            params["max_admin_clans"] = max_admin_clans
        if min_owner_clans is not None:
            params["min_owner_clans"] = min_owner_clans
        if max_owner_clans is not None:
            params["max_owner_clans"] = max_owner_clans
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if min_servers is not None:
            params["min_servers"] = min_servers
        if max_servers is not None:
            params["max_servers"] = max_servers
        if p_2fa is not None:
            params["2fa"] = p_2fa
        if min_full_credits is not None:
            params["min_full_credits"] = min_full_credits
        if max_full_credits is not None:
            params["max_full_credits"] = max_full_credits
        if min_basic_credits is not None:
            params["min_basic_credits"] = min_basic_credits
        if max_basic_credits is not None:
            params["max_basic_credits"] = max_basic_credits
        if min_orbs is not None:
            params["min_orbs"] = min_orbs
        if max_orbs is not None:
            params["max_orbs"] = max_orbs
        return await self._request("GET", path, params=params)

    async def category_tik_tok(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        followers_min: int | None = None,
        followers_max: int | None = None,
        post_min: int | None = None,
        post_max: int | None = None,
        like_min: int | None = None,
        like_max: int | None = None,
        coins_min: int | None = None,
        coins_max: int | None = None,
        cookie_login: YesNoNoMatterScheme | None = None,
        verified: str | None = None,
        email: str | None = None,
    ) -> dict[str, Any]:
        path = "/tiktok"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if followers_min is not None:
            params["followers_min"] = followers_min
        if followers_max is not None:
            params["followers_max"] = followers_max
        if post_min is not None:
            params["post_min"] = post_min
        if post_max is not None:
            params["post_max"] = post_max
        if like_min is not None:
            params["like_min"] = like_min
        if like_max is not None:
            params["like_max"] = like_max
        if coins_min is not None:
            params["coins_min"] = coins_min
        if coins_max is not None:
            params["coins_max"] = coins_max
        if cookie_login is not None:
            params["cookie_login"] = cookie_login
        if verified is not None:
            params["verified"] = verified
        if email is not None:
            params["email"] = email
        return await self._request("GET", path, params=params)

    async def category_instagram(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        tel: str | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        cookies: str | None = None,
        login_without_cookies: YesNoNoMatterScheme | None = None,
        followers_min: int | None = None,
        followers_max: int | None = None,
        post_min: int | None = None,
        post_max: int | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
    ) -> dict[str, Any]:
        path = "/instagram"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if tel is not None:
            params["tel"] = tel
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if cookies is not None:
            params["cookies"] = cookies
        if login_without_cookies is not None:
            params["login_without_cookies"] = login_without_cookies
        if followers_min is not None:
            params["followers_min"] = followers_min
        if followers_max is not None:
            params["followers_max"] = followers_max
        if post_min is not None:
            params["post_min"] = post_min
        if post_max is not None:
            params["post_max"] = post_max
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        return await self._request("GET", path, params=params)

    async def category_battle_net(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        eg: int | None = None,
        game: list[int] | None = None,
        daybreak: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        tel: str | None = None,
        edit_btag: YesNoNoMatterScheme | None = None,
        changeable_fn: YesNoNoMatterScheme | None = None,
        real_id: YesNoNoMatterScheme | None = None,
        parent_control: YesNoNoMatterScheme | None = None,
        no_bans: YesNoNoMatterScheme | None = None,
        balance_min: int | None = None,
        balance_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/battlenet"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if eg is not None:
            params["eg"] = eg
        if game is not None:
            params["game[]"] = game
        if daybreak is not None:
            params["daybreak"] = daybreak
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if tel is not None:
            params["tel"] = tel
        if edit_btag is not None:
            params["edit_btag"] = edit_btag
        if changeable_fn is not None:
            params["changeable_fn"] = changeable_fn
        if real_id is not None:
            params["real_id"] = real_id
        if parent_control is not None:
            params["parent_control"] = parent_control
        if no_bans is not None:
            params["no_bans"] = no_bans
        if balance_min is not None:
            params["balance_min"] = balance_min
        if balance_max is not None:
            params["balance_max"] = balance_max
        return await self._request("GET", path, params=params)

    async def category_chat_gpt(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email_type: list[str] | None = None,
        item_domain: str | None = None,
        subscription: list[str] | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
        tel: str | None = None,
        transactions: YesNoNoMatterScheme | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        openai_tier: list[str] | None = None,
        openai_balance_min: int | None = None,
        openai_balance_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/chatgpt"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email_type is not None:
            params["email_type[]"] = email_type
        if item_domain is not None:
            params["item_domain"] = item_domain
        if subscription is not None:
            params["subscription[]"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        if tel is not None:
            params["tel"] = tel
        if transactions is not None:
            params["transactions"] = transactions
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if openai_tier is not None:
            params["openai_tier[]"] = openai_tier
        if openai_balance_min is not None:
            params["openai_balance_min"] = openai_balance_min
        if openai_balance_max is not None:
            params["openai_balance_max"] = openai_balance_max
        return await self._request("GET", path, params=params)

    async def category_vpn(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        service: list[str] | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
    ) -> dict[str, Any]:
        path = "/vpn"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if service is not None:
            params["service[]"] = service
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        return await self._request("GET", path, params=params)

    async def category_roblox(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        email: YesNoNoMatterScheme | None = None,
        robux_min: int | None = None,
        robux_max: int | None = None,
        friends_min: int | None = None,
        friends_max: int | None = None,
        followers_min: int | None = None,
        followers_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
        xbox_connected: YesNoNoMatterScheme | None = None,
        psn_connected: YesNoNoMatterScheme | None = None,
        verified: str | None = None,
        age_verified: YesNoNoMatterScheme | None = None,
        incoming_robux_total_min: int | None = None,
        incoming_robux_total_max: int | None = None,
        limited_price_min: int | None = None,
        limited_price_max: int | None = None,
        gamepass_min: int | None = None,
        gamepass_max: int | None = None,
        game_donations: YesNoNoMatterScheme | None = None,
        inv_min: int | None = None,
        inv_max: int | None = None,
        ugc_limited_price_min: int | None = None,
        ugc_limited_price_max: int | None = None,
        credit_balance_min: int | None = None,
        credit_balance_max: int | None = None,
        offsale_min: int | None = None,
        offsale_max: int | None = None,
        voice: YesNoNoMatterScheme | None = None,
        age_group: list[str] | None = None,
        not_age_group: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/roblox"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if email is not None:
            params["email"] = email
        if robux_min is not None:
            params["robux_min"] = robux_min
        if robux_max is not None:
            params["robux_max"] = robux_max
        if friends_min is not None:
            params["friends_min"] = friends_min
        if friends_max is not None:
            params["friends_max"] = friends_max
        if followers_min is not None:
            params["followers_min"] = followers_min
        if followers_max is not None:
            params["followers_max"] = followers_max
        if country is not None:
            params["country"] = country
        if not_country is not None:
            params["not_country"] = not_country
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        if xbox_connected is not None:
            params["xbox_connected"] = xbox_connected
        if psn_connected is not None:
            params["psn_connected"] = psn_connected
        if verified is not None:
            params["verified"] = verified
        if age_verified is not None:
            params["age_verified"] = age_verified
        if incoming_robux_total_min is not None:
            params["incoming_robux_total_min"] = incoming_robux_total_min
        if incoming_robux_total_max is not None:
            params["incoming_robux_total_max"] = incoming_robux_total_max
        if limited_price_min is not None:
            params["limited_price_min"] = limited_price_min
        if limited_price_max is not None:
            params["limited_price_max"] = limited_price_max
        if gamepass_min is not None:
            params["gamepass_min"] = gamepass_min
        if gamepass_max is not None:
            params["gamepass_max"] = gamepass_max
        if game_donations is not None:
            params["game_donations"] = game_donations
        if inv_min is not None:
            params["inv_min"] = inv_min
        if inv_max is not None:
            params["inv_max"] = inv_max
        if ugc_limited_price_min is not None:
            params["ugc_limited_price_min"] = ugc_limited_price_min
        if ugc_limited_price_max is not None:
            params["ugc_limited_price_max"] = ugc_limited_price_max
        if credit_balance_min is not None:
            params["credit_balance_min"] = credit_balance_min
        if credit_balance_max is not None:
            params["credit_balance_max"] = credit_balance_max
        if offsale_min is not None:
            params["offsale_min"] = offsale_min
        if offsale_max is not None:
            params["offsale_max"] = offsale_max
        if voice is not None:
            params["voice"] = voice
        if age_group is not None:
            params["age_group[]"] = age_group
        if not_age_group is not None:
            params["not_age_group[]"] = not_age_group
        return await self._request("GET", path, params=params)

    async def category_warface(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        rank_min: int | None = None,
        rank_max: int | None = None,
        bonus_rank_min: int | None = None,
        bonus_rank_max: int | None = None,
        tel: str | None = None,
        daybreak: int | None = None,
        kredits_min: int | None = None,
        kredits_max: int | None = None,
        total_kredits_min: int | None = None,
        total_kredits_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/warface"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if rank_min is not None:
            params["rank_min"] = rank_min
        if rank_max is not None:
            params["rank_max"] = rank_max
        if bonus_rank_min is not None:
            params["bonus_rank_min"] = bonus_rank_min
        if bonus_rank_max is not None:
            params["bonus_rank_max"] = bonus_rank_max
        if tel is not None:
            params["tel"] = tel
        if daybreak is not None:
            params["daybreak"] = daybreak
        if kredits_min is not None:
            params["kredits_min"] = kredits_min
        if kredits_max is not None:
            params["kredits_max"] = kredits_max
        if total_kredits_min is not None:
            params["total_kredits_min"] = total_kredits_min
        if total_kredits_max is not None:
            params["total_kredits_max"] = total_kredits_max
        return await self._request("GET", path, params=params)

    async def category_minecraft(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        subscription: str | None = None,
        subscription_length: int | None = None,
        subscription_period: str | None = None,
        autorenewal: str | None = None,
        java: YesNoNoMatterScheme | None = None,
        bedrock: YesNoNoMatterScheme | None = None,
        dungeons: YesNoNoMatterScheme | None = None,
        legends: YesNoNoMatterScheme | None = None,
        change_nickname: YesNoNoMatterScheme | None = None,
        capes: list[str] | None = None,
        capes_min: int | None = None,
        capes_max: int | None = None,
        country: list[str] | None = None,
        not_country: list[str] | None = None,
        hypixel_ban: YesNoNoMatterScheme | None = None,
        hypixel_skyblock_api_enabled: YesNoNoMatterScheme | None = None,
        rank_hypixel: list[str] | None = None,
        level_hypixel_min: int | None = None,
        level_hypixel_max: int | None = None,
        achievement_hypixel_min: int | None = None,
        achievement_hypixel_max: int | None = None,
        level_hypixel_skyblock_min: int | None = None,
        level_hypixel_skyblock_max: int | None = None,
        net_worth_hypixel_skyblock_min: int | None = None,
        net_worth_hypixel_skyblock_max: int | None = None,
        reg: int | None = None,
        reg_period: str | None = None,
        last_login_hypixel: int | None = None,
        last_login_hypixel_period: str | None = None,
        can_change_details: YesNoNoMatterScheme | None = None,
        nickname_length_min: int | None = None,
        nickname_length_max: int | None = None,
        hypixel_ban_parsed: YesNoNoMatterScheme | None = None,
        minecoins_min: int | None = None,
        minecoins_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/minecraft"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if subscription is not None:
            params["subscription"] = subscription
        if subscription_length is not None:
            params["subscription_length"] = subscription_length
        if subscription_period is not None:
            params["subscription_period"] = subscription_period
        if autorenewal is not None:
            params["autorenewal"] = autorenewal
        if java is not None:
            params["java"] = java
        if bedrock is not None:
            params["bedrock"] = bedrock
        if dungeons is not None:
            params["dungeons"] = dungeons
        if legends is not None:
            params["legends"] = legends
        if change_nickname is not None:
            params["change_nickname"] = change_nickname
        if capes is not None:
            params["capes[]"] = capes
        if capes_min is not None:
            params["capes_min"] = capes_min
        if capes_max is not None:
            params["capes_max"] = capes_max
        if country is not None:
            params["country[]"] = country
        if not_country is not None:
            params["not_country[]"] = not_country
        if hypixel_ban is not None:
            params["hypixel_ban"] = hypixel_ban
        if hypixel_skyblock_api_enabled is not None:
            params["hypixel_skyblock_api_enabled"] = hypixel_skyblock_api_enabled
        if rank_hypixel is not None:
            params["rank_hypixel[]"] = rank_hypixel
        if level_hypixel_min is not None:
            params["level_hypixel_min"] = level_hypixel_min
        if level_hypixel_max is not None:
            params["level_hypixel_max"] = level_hypixel_max
        if achievement_hypixel_min is not None:
            params["achievement_hypixel_min"] = achievement_hypixel_min
        if achievement_hypixel_max is not None:
            params["achievement_hypixel_max"] = achievement_hypixel_max
        if level_hypixel_skyblock_min is not None:
            params["level_hypixel_skyblock_min"] = level_hypixel_skyblock_min
        if level_hypixel_skyblock_max is not None:
            params["level_hypixel_skyblock_max"] = level_hypixel_skyblock_max
        if net_worth_hypixel_skyblock_min is not None:
            params["net_worth_hypixel_skyblock_min"] = net_worth_hypixel_skyblock_min
        if net_worth_hypixel_skyblock_max is not None:
            params["net_worth_hypixel_skyblock_max"] = net_worth_hypixel_skyblock_max
        if reg is not None:
            params["reg"] = reg
        if reg_period is not None:
            params["reg_period"] = reg_period
        if last_login_hypixel is not None:
            params["last_login_hypixel"] = last_login_hypixel
        if last_login_hypixel_period is not None:
            params["last_login_hypixel_period"] = last_login_hypixel_period
        if can_change_details is not None:
            params["can_change_details"] = can_change_details
        if nickname_length_min is not None:
            params["nickname_length_min"] = nickname_length_min
        if nickname_length_max is not None:
            params["nickname_length_max"] = nickname_length_max
        if hypixel_ban_parsed is not None:
            params["hypixel_ban_parsed"] = hypixel_ban_parsed
        if minecoins_min is not None:
            params["minecoins_min"] = minecoins_min
        if minecoins_max is not None:
            params["minecoins_max"] = minecoins_max
        return await self._request("GET", path, params=params)

    async def category_hytale(
        self,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
        edition: list[str] | None = None,
        profiles_min: int | None = None,
        profiles_max: int | None = None,
    ) -> dict[str, Any]:
        path = "/hytale"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        if edition is not None:
            params["edition[]"] = edition
        if profiles_min is not None:
            params["profiles_min"] = profiles_min
        if profiles_max is not None:
            params["profiles_max"] = profiles_max
        return await self._request("GET", path, params=params)

    async def category_list(
        self,
        top_queries: bool | None = None,
    ) -> dict[str, Any]:
        path = "/category"
        params: dict[str, Any] = {}
        if top_queries is not None:
            params["top_queries"] = top_queries
        return await self._request("GET", path, params=params)

    async def category_params(
        self,
        categoryName: str,
    ) -> dict[str, Any]:
        path = "/{categoryName}/params"
        path = path.replace("{categoryName}", str(categoryName))
        return await self._request("GET", path)

    async def category_games(
        self,
        categoryName: str,
    ) -> dict[str, Any]:
        path = "/{categoryName}/games"
        path = path.replace("{categoryName}", str(categoryName))
        return await self._request("GET", path)

    async def list_user(
        self,
        user_id: int | None = None,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        show: str | None = None,
        delete_reason: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        login: str | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
        username: str | None = None,
        published_startDate: str | None = None,
        published_endDate: str | None = None,
        filter_by_published_date: bool | None = None,
        paid_startDate: str | None = None,
        paid_endDate: str | None = None,
        filter_by_buyer_operation_date: bool | None = None,
        delete_startDate: str | None = None,
        delete_endDate: str | None = None,
        filter_by_delete_date: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/items"
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if delete_reason is not None:
            params["delete_reason"] = delete_reason
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if login is not None:
            params["login"] = login
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if username is not None:
            params["username"] = username
        if published_startDate is not None:
            params["published_startDate"] = published_startDate
        if published_endDate is not None:
            params["published_endDate"] = published_endDate
        if filter_by_published_date is not None:
            params["filter_by_published_date"] = filter_by_published_date
        if paid_startDate is not None:
            params["paid_startDate"] = paid_startDate
        if paid_endDate is not None:
            params["paid_endDate"] = paid_endDate
        if filter_by_buyer_operation_date is not None:
            params["filter_by_buyer_operation_date"] = filter_by_buyer_operation_date
        if delete_startDate is not None:
            params["delete_startDate"] = delete_startDate
        if delete_endDate is not None:
            params["delete_endDate"] = delete_endDate
        if filter_by_delete_date is not None:
            params["filter_by_delete_date"] = filter_by_delete_date
        return await self._request("GET", path, params=params)

    async def list_orders(
        self,
        user_id: int | None = None,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        show: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        login: str | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/orders"
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if login is not None:
            params["login"] = login
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        return await self._request("GET", path, params=params)

    async def list_states(
        self,
        user_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/user/item-states"
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        return await self._request("GET", path, params=params)

    async def list_download(
        self,
        type_: str,
        format: str | None = None,
        custom_format: str | None = None,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        show: str | None = None,
        delete_reason: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
        username: str | None = None,
        published_startDate: str | None = None,
        published_endDate: str | None = None,
        filter_by_published_date: bool | None = None,
        paid_startDate: str | None = None,
        paid_endDate: str | None = None,
        filter_by_buyer_operation_date: bool | None = None,
        delete_startDate: str | None = None,
        delete_endDate: str | None = None,
        filter_by_delete_date: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/{type}/download"
        path = path.replace("{type}", str(type_))
        params: dict[str, Any] = {}
        if format is not None:
            params["format"] = format
        if custom_format is not None:
            params["custom_format"] = custom_format
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if delete_reason is not None:
            params["delete_reason"] = delete_reason
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if username is not None:
            params["username"] = username
        if published_startDate is not None:
            params["published_startDate"] = published_startDate
        if published_endDate is not None:
            params["published_endDate"] = published_endDate
        if filter_by_published_date is not None:
            params["filter_by_published_date"] = filter_by_published_date
        if paid_startDate is not None:
            params["paid_startDate"] = paid_startDate
        if paid_endDate is not None:
            params["paid_endDate"] = paid_endDate
        if filter_by_buyer_operation_date is not None:
            params["filter_by_buyer_operation_date"] = filter_by_buyer_operation_date
        if delete_startDate is not None:
            params["delete_startDate"] = delete_startDate
        if delete_endDate is not None:
            params["delete_endDate"] = delete_endDate
        if filter_by_delete_date is not None:
            params["filter_by_delete_date"] = filter_by_delete_date
        return await self._request("GET", path, params=params)

    async def list_favorites(
        self,
        page: int | None = None,
        show: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
    ) -> dict[str, Any]:
        path = "/fave"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        return await self._request("GET", path, params=params)

    async def list_viewed(
        self,
        page: int | None = None,
        show: str | None = None,
        title: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        order_by: str | None = None,
        sb: bool | None = None,
        sb_by_me: bool | None = None,
        nsb: bool | None = None,
        nsb_by_me: bool | None = None,
    ) -> dict[str, Any]:
        path = "/viewed"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if show is not None:
            params["show"] = show
        if title is not None:
            params["title"] = title
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if order_by is not None:
            params["order_by"] = order_by
        if sb is not None:
            params["sb"] = sb
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if nsb is not None:
            params["nsb"] = nsb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        return await self._request("GET", path, params=params)

    async def managing_get(
        self,
        item_id: int,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        return await self._request("GET", path, params=params)

    async def manging_delete(
        self,
        item_id: int,
        reason: str,
    ) -> dict[str, Any]:
        path = "/{item_id}"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if reason is not None:
            data["reason"] = reason
        return await self._request("DELETE", path, json=data)

    async def profile_claims(
        self,
        type_: str | None = None,
        claim_state: str | None = None,
    ) -> dict[str, Any]:
        path = "/claims"
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if claim_state is not None:
            params["claim_state"] = claim_state
        return await self._request("GET", path, params=params)

    async def managing_create_claim(
        self,
        item_id: ItemIDModel,
        post_body: str,
    ) -> dict[str, Any]:
        path = "/claims"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        if post_body is not None:
            data["post_body"] = post_body
        return await self._request("POST", path, json=data)

    async def managing_bulk_get(
        self,
        item_id: list[ItemIDModel] | None = None,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/bulk/items"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        if parse_same_item_ids is not None:
            data["parse_same_item_ids"] = parse_same_item_ids
        return await self._request("POST", path, json=data)

    async def managing_steam_inventory_value(
        self,
        item_id: int,
        app_id: int | None = None,
        currency: CurrencyModel | None = None,
        ignore_cache: bool | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/inventory-value"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if app_id is not None:
            params["app_id"] = app_id
        if currency is not None:
            params["currency"] = currency
        if ignore_cache is not None:
            params["ignore_cache"] = ignore_cache
        return await self._request("GET", path, params=params)

    async def managing_steam_value(
        self,
        link: str,
        app_id: int | None = None,
        currency: CurrencyModel | None = None,
        ignore_cache: bool | None = None,
    ) -> dict[str, Any]:
        path = "/steam-value"
        params: dict[str, Any] = {}
        if link is not None:
            params["link"] = link
        if app_id is not None:
            params["app_id"] = app_id
        if currency is not None:
            params["currency"] = currency
        if ignore_cache is not None:
            params["ignore_cache"] = ignore_cache
        return await self._request("GET", path, params=params)

    async def managing_steam_preview(
        self,
        item_id: int,
        type_: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/steam-preview"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        return await self._request("GET", path, params=params)

    async def managing_edit(
        self,
        item_id: int,
        title: str | None = None,
        title_en: str | None = None,
        price: int | None = None,
        currency: CurrencyModel | None = None,
        item_origin: str | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        allow_ask_discount: bool | None = None,
        proxy_id: int | None = None,
        description: str | None = None,
        information: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/edit"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if price is not None:
            data["price"] = price
        if currency is not None:
            data["currency"] = currency
        if item_origin is not None:
            data["item_origin"] = item_origin
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if allow_ask_discount is not None:
            data["allow_ask_discount"] = allow_ask_discount
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if description is not None:
            data["description"] = description
        if information is not None:
            data["information"] = information
        return await self._request("PUT", path, json=data)

    async def managing_ai_price(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/ai-price"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_auto_buy_price(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/auto-buy-price"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_note(
        self,
        item_id: int,
        text: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/note-save"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if text is not None:
            data["text"] = text
        return await self._request("POST", path, json=data)

    async def managing_steam_update_value(
        self,
        item_id: int,
        all: bool | None = None,
        app_id: int | None = None,
        authorize: bool | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/update-inventory"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if all is not None:
            data["all"] = all
        if app_id is not None:
            data["app_id"] = app_id
        if authorize is not None:
            data["authorize"] = authorize
        return await self._request("POST", path, json=data)

    async def managing_bump(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/bump"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_auto_bump(
        self,
        item_id: int,
        hour: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/auto-bump"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if hour is not None:
            data["hour"] = hour
        return await self._request("POST", path, json=data)

    async def managing_auto_bump_disable(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/auto-bump"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("DELETE", path)

    async def managing_open(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/open"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_close(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/close"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_image(
        self,
        item_id: int,
        type_: str,
    ) -> dict[str, Any]:
        path = "/{item_id}/image"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        return await self._request("GET", path, params=params)

    async def cart_get(
        self,
        category_id: CategoryIDModel | None = None,
        page: int | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        title: str | None = None,
        order_by: str | None = None,
        tag_id: list[int] | None = None,
        not_tag_id: list[int] | None = None,
        public_tag_id: list[int] | None = None,
        not_public_tag_id: list[int] | None = None,
        origin: list[str] | None = None,
        not_origin: list[str] | None = None,
        user_id: int | None = None,
        nsb: bool | None = None,
        sb: bool | None = None,
        nsb_by_me: bool | None = None,
        sb_by_me: bool | None = None,
        currency: str | None = None,
        email_login_data: bool | None = None,
        email_provider: list[str] | None = None,
        not_email_provider: str | None = None,
        parse_same_item_ids: bool | None = None,
    ) -> dict[str, Any]:
        path = "/cart"
        params: dict[str, Any] = {}
        if category_id is not None:
            params["category_id"] = category_id
        if page is not None:
            params["page"] = page
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if title is not None:
            params["title"] = title
        if order_by is not None:
            params["order_by"] = order_by
        if tag_id is not None:
            params["tag_id[]"] = tag_id
        if not_tag_id is not None:
            params["not_tag_id[]"] = not_tag_id
        if public_tag_id is not None:
            params["public_tag_id[]"] = public_tag_id
        if not_public_tag_id is not None:
            params["not_public_tag_id[]"] = not_public_tag_id
        if origin is not None:
            params["origin[]"] = origin
        if not_origin is not None:
            params["not_origin[]"] = not_origin
        if user_id is not None:
            params["user_id"] = user_id
        if nsb is not None:
            params["nsb"] = nsb
        if sb is not None:
            params["sb"] = sb
        if nsb_by_me is not None:
            params["nsb_by_me"] = nsb_by_me
        if sb_by_me is not None:
            params["sb_by_me"] = sb_by_me
        if currency is not None:
            params["currency"] = currency
        if email_login_data is not None:
            params["email_login_data"] = email_login_data
        if email_provider is not None:
            params["email_provider[]"] = email_provider
        if not_email_provider is not None:
            params["not_email_provider[]"] = not_email_provider
        if parse_same_item_ids is not None:
            params["parse_same_item_ids"] = parse_same_item_ids
        return await self._request("GET", path, params=params)

    async def cart_add(
        self,
        item_id: ItemIDModel,
    ) -> dict[str, Any]:
        path = "/cart"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        return await self._request("POST", path, json=data)

    async def cart_delete(
        self,
        item_id: ItemIDModel | None = None,
    ) -> dict[str, Any]:
        path = "/cart"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if item_id is not None:
            data["item_id"] = item_id
        return await self._request("DELETE", path, json=data)

    async def purchasing_fast_buy(
        self,
        item_id: int,
        price: float | None = None,
        balance_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/fast-buy"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if price is not None:
            data["price"] = price
        if balance_id is not None:
            data["balance_id"] = balance_id
        return await self._request("POST", path, json=data)

    async def purchasing_check(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/check-account"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def purchasing_confirm(
        self,
        item_id: int,
        price: int | None = None,
        balance_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/confirm-buy"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if price is not None:
            data["price"] = price
        if balance_id is not None:
            data["balance_id"] = balance_id
        return await self._request("POST", path, json=data)

    async def purchasing_discount_request(
        self,
        item_id: int,
        discount_price: float,
        message: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/discount"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if discount_price is not None:
            data["discount_price"] = discount_price
        if message is not None:
            data["message"] = message
        return await self._request("POST", path, json=data)

    async def purchasing_discount_cancel(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/discount"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("DELETE", path)

    async def custom_discounts_get(
        self,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        return await self._request("GET", path)

    async def custom_discounts_create(
        self,
        user_id: int,
        category_id: CategoryIDModel,
        discount_percent: float,
        min_price: float,
        max_price: float | None = None,
        currency: CurrencyModel | None = None,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        if category_id is not None:
            data["category_id"] = category_id
        if discount_percent is not None:
            data["discount_percent"] = discount_percent
        if min_price is not None:
            data["min_price"] = min_price
        if max_price is not None:
            data["max_price"] = max_price
        if currency is not None:
            data["currency"] = currency
        return await self._request("POST", path, json=data)

    async def custom_discounts_edit(
        self,
        discount_id: int,
        discount_percent: float | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if discount_id is not None:
            data["discount_id"] = discount_id
        if discount_percent is not None:
            data["discount_percent"] = discount_percent
        if min_price is not None:
            data["min_price"] = min_price
        if max_price is not None:
            data["max_price"] = max_price
        return await self._request("PUT", path, json=data)

    async def custom_discounts_delete(
        self,
        discount_id: int,
    ) -> dict[str, Any]:
        path = "/custom-discounts"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if discount_id is not None:
            data["discount_id"] = discount_id
        return await self._request("DELETE", path, json=data)

    async def publishing_fast_sell(
        self,
        price: float,
        category_id: int,
        currency: CurrencyModel,
        item_origin: str,
        title: str | None = None,
        title_en: str | None = None,
        extended_guarantee: int | None = None,
        allow_ask_discount: bool | None = None,
        proxy_id: int | None = None,
        random_proxy: schema | None = None,
        description: str | None = None,
        information: str | None = None,
        login: str | None = None,
        password: str | None = None,
        login_password: str | None = None,
        has_email_login_data: bool | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        extra: ExtraModel | None = None,
    ) -> dict[str, Any]:
        path = "/item/fast-sell"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if price is not None:
            data["price"] = price
        if category_id is not None:
            data["category_id"] = category_id
        if currency is not None:
            data["currency"] = currency
        if item_origin is not None:
            data["item_origin"] = item_origin
        if extended_guarantee is not None:
            data["extended_guarantee"] = extended_guarantee
        if allow_ask_discount is not None:
            data["allow_ask_discount"] = allow_ask_discount
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if random_proxy is not None:
            data["random_proxy"] = random_proxy
        if description is not None:
            data["description"] = description
        if information is not None:
            data["information"] = information
        if login is not None:
            data["login"] = login
        if password is not None:
            data["password"] = password
        if login_password is not None:
            data["login_password"] = login_password
        if has_email_login_data is not None:
            data["has_email_login_data"] = has_email_login_data
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if extra is not None:
            data["extra"] = extra
        return await self._request("POST", path, json=data)

    async def publishing_add(
        self,
        price: float,
        category_id: int,
        currency: CurrencyModel,
        item_origin: str,
        title: str | None = None,
        title_en: str | None = None,
        extended_guarantee: int | None = None,
        description: str | None = None,
        information: str | None = None,
        forceTempEmail: bool | None = None,
        resell_item_id: int | None = None,
        has_email_login_data: bool | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        allow_ask_discount: bool | None = None,
        proxy_id: int | None = None,
        random_proxy: schema | None = None,
    ) -> dict[str, Any]:
        path = "/item/add"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if title is not None:
            data["title"] = title
        if title_en is not None:
            data["title_en"] = title_en
        if price is not None:
            data["price"] = price
        if category_id is not None:
            data["category_id"] = category_id
        if currency is not None:
            data["currency"] = currency
        if item_origin is not None:
            data["item_origin"] = item_origin
        if extended_guarantee is not None:
            data["extended_guarantee"] = extended_guarantee
        if description is not None:
            data["description"] = description
        if information is not None:
            data["information"] = information
        if forceTempEmail is not None:
            data["forceTempEmail"] = forceTempEmail
        if resell_item_id is not None:
            data["resell_item_id"] = resell_item_id
        if has_email_login_data is not None:
            data["has_email_login_data"] = has_email_login_data
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if allow_ask_discount is not None:
            data["allow_ask_discount"] = allow_ask_discount
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if random_proxy is not None:
            data["random_proxy"] = random_proxy
        return await self._request("POST", path, json=data)

    async def publishing_check(
        self,
        item_id: int,
        resell_item_id: int | None = None,
        random_proxy: bool | None = None,
        login: str | None = None,
        password: str | None = None,
        login_password: str | None = None,
        has_email_login_data: bool | None = None,
        email_login_data: str | None = None,
        email_type: str | None = None,
        extra: ExtraModel | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/goods/check"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if resell_item_id is not None:
            data["resell_item_id"] = resell_item_id
        if random_proxy is not None:
            data["random_proxy"] = random_proxy
        if login is not None:
            data["login"] = login
        if password is not None:
            data["password"] = password
        if login_password is not None:
            data["login_password"] = login_password
        if has_email_login_data is not None:
            data["has_email_login_data"] = has_email_login_data
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if email_type is not None:
            data["email_type"] = email_type
        if extra is not None:
            data["extra"] = extra
        return await self._request("POST", path, json=data)

    async def publishing_external(
        self,
        item_id: int,
        type_: str,
        login: str | None = None,
        email_login_data: str | None = None,
        cookies: str | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/external-account"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if type_ is not None:
            data["type"] = type_
        if login is not None:
            data["login"] = login
        if email_login_data is not None:
            data["email_login_data"] = email_login_data
        if cookies is not None:
            data["cookies"] = cookies
        return await self._request("POST", path, json=data)

    async def managing_email_code(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/email-code"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_get_letters2(
        self,
        email_password: str | None = None,
        email: str | None = None,
        password: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        path = "/letters2"
        params: dict[str, Any] = {}
        if email_password is not None:
            params["email_password"] = email_password
        if email is not None:
            params["email"] = email
        if password is not None:
            params["password"] = password
        if limit is not None:
            params["limit"] = limit
        return await self._request("GET", path, params=params)

    async def managing_steam_get_mafile(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/mafile"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_steam_add_mafile(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/mafile"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_steam_remove_mafile(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/mafile"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("DELETE", path)

    async def managing_steam_mafile_code(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/guard-code"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_steam_sda(
        self,
        item_id: int,
        id: int | None = None,
        nonce: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/confirm-sda"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if id is not None:
            data["id"] = id
        if nonce is not None:
            data["nonce"] = nonce
        return await self._request("POST", path, json=data)

    async def managing_telegram_code(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/telegram-login-code"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_telegram_reset_auth(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/telegram-reset-authorizations"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_refuse_guarantee(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/refuse-guarantee"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_decline_video_recording(
        self,
        item_id: int,
        i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item: bool,
    ) -> dict[str, Any]:
        path = "/{item_id}/decline-video-recording"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item is not None:
            data["i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item"] = i_voluntarily_and_with_full_awareness_of_my_actions_waive_any_claims_regarding_this_item
        return await self._request("POST", path, json=data)

    async def managing_check_guarantee(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/check-guarantee"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_change_password(
        self,
        item_id: int,
        cancel: int | None = None,
    ) -> dict[str, Any]:
        path = "/{item_id}/change-password"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if cancel is not None:
            data["_cancel"] = cancel
        return await self._request("POST", path, json=data)

    async def managing_temp_email_password(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/temp-email-password"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("GET", path)

    async def managing_tag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return await self._request("POST", path, json=data)

    async def managing_untag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return await self._request("DELETE", path, json=data)

    async def managing_public_tag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/public-tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return await self._request("POST", path, json=data)

    async def managing_public_untag(
        self,
        item_id: int,
        tag_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/public-tag"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if tag_id is not None:
            data["tag_id"] = tag_id
        return await self._request("DELETE", path, json=data)

    async def managing_favorite(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/star"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_unfavorite(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/star"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("DELETE", path)

    async def managing_stick(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/stick"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("POST", path)

    async def managing_unstick(
        self,
        item_id: int,
    ) -> dict[str, Any]:
        path = "/{item_id}/stick"
        path = path.replace("{item_id}", str(item_id))
        return await self._request("DELETE", path)

    async def managing_transfer(
        self,
        item_id: int,
        username: str,
        secret_answer: str,
    ) -> dict[str, Any]:
        path = "/{item_id}/change-owner"
        path = path.replace("{item_id}", str(item_id))
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if username is not None:
            data["username"] = username
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        return await self._request("POST", path, json=data)

    async def profile_get(
        self,
        fields_include: list[str] | None = None,
    ) -> dict[str, Any]:
        path = "/me"
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._request("GET", path, params=params)

    async def profile_edit(
        self,
        user: dict[str, Any] | None = None,
        option: dict[str, Any] | None = None,
        allow_accept_accounts: list[str] | None = None,
        telegram_api_id: str | None = None,
        telegram_api_hash: str | None = None,
        telegram_device_model: str | None = None,
        telegram_system_version: str | None = None,
        telegram_app_version: str | None = None,
        telegram_lang_pack: str | None = None,
        telegram_lang_code: str | None = None,
        telegram_system_lang_code: str | None = None,
        clear_telegram_client: bool | None = None,
    ) -> dict[str, Any]:
        path = "/me"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if user is not None:
            data["user"] = user
        if option is not None:
            data["option"] = option
        if allow_accept_accounts is not None:
            data["allow_accept_accounts"] = allow_accept_accounts
        if telegram_api_id is not None:
            data["telegram_api_id"] = telegram_api_id
        if telegram_api_hash is not None:
            data["telegram_api_hash"] = telegram_api_hash
        if telegram_device_model is not None:
            data["telegram_device_model"] = telegram_device_model
        if telegram_system_version is not None:
            data["telegram_system_version"] = telegram_system_version
        if telegram_app_version is not None:
            data["telegram_app_version"] = telegram_app_version
        if telegram_lang_pack is not None:
            data["telegram_lang_pack"] = telegram_lang_pack
        if telegram_lang_code is not None:
            data["telegram_lang_code"] = telegram_lang_code
        if telegram_system_lang_code is not None:
            data["telegram_system_lang_code"] = telegram_system_lang_code
        if clear_telegram_client is not None:
            data["clear_telegram_client"] = clear_telegram_client
        return await self._request("PUT", path, json=data)

    async def payments_invoice_get(
        self,
        invoice_id: int | None = None,
        payment_id: str | None = None,
    ) -> dict[str, Any]:
        path = "/invoice"
        params: dict[str, Any] = {}
        if invoice_id is not None:
            params["invoice_id"] = invoice_id
        if payment_id is not None:
            params["payment_id"] = payment_id
        return await self._request("GET", path, params=params)

    async def payments_invoice_create(
        self,
        currency: CurrencyModel,
        amount: float,
        payment_id: str,
        comment: str,
        url_success: str,
        merchant_id: int,
        url_callback: str | None = None,
        required_telegram_id: int | None = None,
        required_telegram_username: str | None = None,
        lifetime: float | None = 3600,
        additional_data: str | None = None,
        is_test: bool | None = None,
    ) -> dict[str, Any]:
        path = "/invoice"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if currency is not None:
            data["currency"] = currency
        if amount is not None:
            data["amount"] = amount
        if payment_id is not None:
            data["payment_id"] = payment_id
        if comment is not None:
            data["comment"] = comment
        if url_success is not None:
            data["url_success"] = url_success
        if url_callback is not None:
            data["url_callback"] = url_callback
        if merchant_id is not None:
            data["merchant_id"] = merchant_id
        if required_telegram_id is not None:
            data["required_telegram_id"] = required_telegram_id
        if required_telegram_username is not None:
            data["required_telegram_username"] = required_telegram_username
        if lifetime is not None:
            data["lifetime"] = lifetime
        if additional_data is not None:
            data["additional_data"] = additional_data
        if is_test is not None:
            data["is_test"] = is_test
        return await self._request("POST", path, json=data)

    async def payments_invoice_list(
        self,
        page: int | None = None,
        currency: CurrencyModel | None = None,
        status: str | None = None,
        amount: float | None = None,
        merchant_id: int | None = None,
    ) -> dict[str, Any]:
        path = "/invoice/list"
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if currency is not None:
            params["currency"] = currency
        if status is not None:
            params["status"] = status
        if amount is not None:
            params["amount"] = amount
        if merchant_id is not None:
            params["merchant_id"] = merchant_id
        return await self._request("GET", path, params=params)

    async def payments_currency(
        self,
    ) -> dict[str, Any]:
        path = "/currency"
        return await self._request("GET", path)

    async def payments_balance_list(
        self,
    ) -> dict[str, Any]:
        path = "/balance/exchange"
        return await self._request("GET", path)

    async def payments_balance_exchange(
        self,
        from_balance: str,
        to_balance: str,
        amount: int,
    ) -> dict[str, Any]:
        path = "/balance/exchange"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if from_balance is not None:
            data["from_balance"] = from_balance
        if to_balance is not None:
            data["to_balance"] = to_balance
        if amount is not None:
            data["amount"] = amount
        return await self._request("POST", path, json=data)

    async def payments_transfer(
        self,
        amount: int,
        currency: CurrencyModel,
        user_id: int | None = None,
        username: str | None = None,
        comment: str | None = None,
        telegram_deal: bool | None = None,
        telegram_username: str | None = None,
        transfer_hold: bool | None = None,
        hold_length_value: int | None = None,
        hold_length_option: str | None = None,
    ) -> dict[str, Any]:
        path = "/balance/transfer"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if user_id is not None:
            data["user_id"] = user_id
        if username is not None:
            data["username"] = username
        if amount is not None:
            data["amount"] = amount
        if currency is not None:
            data["currency"] = currency
        if comment is not None:
            data["comment"] = comment
        if telegram_deal is not None:
            data["telegram_deal"] = telegram_deal
        if telegram_username is not None:
            data["telegram_username"] = telegram_username
        if transfer_hold is not None:
            data["transfer_hold"] = transfer_hold
        if hold_length_value is not None:
            data["hold_length_value"] = hold_length_value
        if hold_length_option is not None:
            data["hold_length_option"] = hold_length_option
        return await self._request("POST", path, json=data)

    async def payments_fee(
        self,
        amount: float | None = None,
    ) -> dict[str, Any]:
        path = "/balance/transfer/fee"
        params: dict[str, Any] = {}
        if amount is not None:
            params["amount"] = amount
        return await self._request("GET", path, params=params)

    async def payments_cancel(
        self,
        payment_id: int,
    ) -> dict[str, Any]:
        path = "/balance/transfer/cancel"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if payment_id is not None:
            data["payment_id"] = payment_id
        return await self._request("POST", path, json=data)

    async def payments_history(
        self,
        type_: str | None = None,
        pmin: int | None = None,
        pmax: int | None = None,
        currency: CurrencyModel | None = None,
        page: int | None = None,
        operation_id_lt: int | None = None,
        receiver: str | None = None,
        sender: str | None = None,
        is_api: bool | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
        wallet: str | None = None,
        comment: str | None = None,
        is_hold: bool | None = None,
        show_payment_stats: bool | None = None,
    ) -> dict[str, Any]:
        path = "/user/payments"
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if pmin is not None:
            params["pmin"] = pmin
        if pmax is not None:
            params["pmax"] = pmax
        if currency is not None:
            params["currency"] = currency
        if page is not None:
            params["page"] = page
        if operation_id_lt is not None:
            params["operation_id_lt"] = operation_id_lt
        if receiver is not None:
            params["receiver"] = receiver
        if sender is not None:
            params["sender"] = sender
        if is_api is not None:
            params["is_api"] = is_api
        if startDate is not None:
            params["startDate"] = startDate
        if endDate is not None:
            params["endDate"] = endDate
        if wallet is not None:
            params["wallet"] = wallet
        if comment is not None:
            params["comment"] = comment
        if is_hold is not None:
            params["is_hold"] = is_hold
        if show_payment_stats is not None:
            params["show_payment_stats"] = show_payment_stats
        return await self._request("GET", path, params=params)

    async def auto_payments_list(
        self,
    ) -> dict[str, Any]:
        path = "/auto-payments"
        return await self._request("GET", path)

    async def auto_payments_create(
        self,
        username_receiver: str,
        day: int,
        amount: float,
        secret_answer: str | None = None,
        currency: CurrencyModel | None = None,
        description: str | None = None,
    ) -> dict[str, Any]:
        path = "/auto-payment"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if secret_answer is not None:
            data["secret_answer"] = secret_answer
        if username_receiver is not None:
            data["username_receiver"] = username_receiver
        if day is not None:
            data["day"] = day
        if amount is not None:
            data["amount"] = amount
        if currency is not None:
            data["currency"] = currency
        if description is not None:
            data["description"] = description
        return await self._request("POST", path, json=data)

    async def auto_payments_delete(
        self,
        auto_payment_id: int,
    ) -> dict[str, Any]:
        path = "/auto-payment"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if auto_payment_id is not None:
            data["auto_payment_id"] = auto_payment_id
        return await self._request("DELETE", path, json=data)

    async def payments_payout_services(
        self,
    ) -> dict[str, Any]:
        path = "/balance/payout/services"
        return await self._request("GET", path)

    async def payments_payout(
        self,
        payment_system: str,
        wallet: str,
        amount: float,
        currency: CurrencyModel,
        include_fee: bool | None = None,
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        path = "/balance/payout"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if payment_system is not None:
            data["payment_system"] = payment_system
        if wallet is not None:
            data["wallet"] = wallet
        if amount is not None:
            data["amount"] = amount
        if currency is not None:
            data["currency"] = currency
        if include_fee is not None:
            data["include_fee"] = include_fee
        if extra is not None:
            data["extra"] = extra
        return await self._request("POST", path, json=data)

    async def proxy_get(
        self,
    ) -> dict[str, Any]:
        path = "/proxy"
        return await self._request("GET", path)

    async def proxy_add(
        self,
        proxy_ip: str | None = None,
        proxy_port: int | None = None,
        proxy_user: str | None = None,
        proxy_pass: str | None = None,
        proxy_row: str | None = None,
    ) -> dict[str, Any]:
        path = "/proxy"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if proxy_ip is not None:
            data["proxy_ip"] = proxy_ip
        if proxy_port is not None:
            data["proxy_port"] = proxy_port
        if proxy_user is not None:
            data["proxy_user"] = proxy_user
        if proxy_pass is not None:
            data["proxy_pass"] = proxy_pass
        if proxy_row is not None:
            data["proxy_row"] = proxy_row
        return await self._request("POST", path, json=data)

    async def proxy_delete(
        self,
        proxy_id: int | None = None,
        delete_all: bool | None = None,
    ) -> dict[str, Any]:
        path = "/proxy"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if proxy_id is not None:
            data["proxy_id"] = proxy_id
        if delete_all is not None:
            data["delete_all"] = delete_all
        return await self._request("DELETE", path, json=data)

    async def imap_create(
        self,
        domain: str,
        imap_server: str,
        port: int,
        secure: bool,
    ) -> dict[str, Any]:
        path = "/imap"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if domain is not None:
            data["domain"] = domain
        if imap_server is not None:
            data["imap_server"] = imap_server
        if port is not None:
            data["port"] = port
        if secure is not None:
            data["secure"] = secure
        return await self._request("POST", path, json=data)

    async def imap_delete(
        self,
        domain: str,
    ) -> dict[str, Any]:
        path = "/imap"
        params: dict[str, Any] = {}
        data: dict[str, Any] = {}
        if domain is not None:
            data["domain"] = domain
        return await self._request("DELETE", path, json=data)

    async def batch(
        self,
    ) -> dict[str, Any]:
        path = "/batch"
        return await self._request("POST", path)

