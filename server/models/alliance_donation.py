

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class TitanFight(BaseModel):
    id: str
    level: int
    promotion: int
    ascension: int
    current_hp: int
    max_hp: int
    version: int


class Member(BaseModel):
    contribution: int
    rank: int
    uid: str


class Alliance(BaseModel):
    policy: int
    titan_fight: TitanFight
    facilities: List[int]
    apera: int
    alname: str
    elo: int
    investigations: List[int]
    logo_small: str
    logo: str
    onium_al: int
    motd: str
    titan_lvl_cooldown: int
    requests: List[str]
    members: List[Member]
    aid: str
    shards: Dict[str, Any]
    titans: Dict[str, Any]
    war_status: str
    position: Any
    item_requests: List
    titan_fight_update: bool
    res: int
    enemy: str
    war_battle_status: int


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Items(BaseModel):
    inventory: List
    currency: List[CurrencyItem]
    heroes: List


class Donation(BaseModel):
    last_day: int
    population: int
    blueprints: int


class Social(BaseModel):
    rank: int
    donation: Donation
    aid: str
    status: int


class Model(BaseModel):
    alliance: Alliance
    blueprints: int
    items: Items
    social: Social
