

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class L001Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List
    heroes: List
    lid: str


class InventoryItem(BaseModel):
    id: str
    quantity: int


class L002Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List
    lid: str


class Hero(BaseModel):
    hid: str
    quantity: int
    ascension: int
    level: int
    busy: bool
    id: str
    type: int
    promotion: int


class L000Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List[Hero]
    lid: str


class L005Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List[Hero]
    lid: str


class L003Item(BaseModel):
    currency: List
    inventory: List[InventoryItem]
    heroes: List
    lid: str


class L004Item(BaseModel):
    currency: List
    inventory: List[InventoryItem]
    heroes: List[Hero]
    lid: str


class Lootboxes(BaseModel):
    L_001_FT: List
    L_WEK: List
    L_001: List[L001Item]
    L_002: List[L002Item]
    L_000: List[L000Item]
    L_005: List[L005Item]
    L_003: List[L003Item]
    L_004: List[L004Item]


class Mail(BaseModel):
    lootboxes: Lootboxes
    mail: Dict[str, Any]
    systemclaim: List[str]
    uid: str


class Rewards(BaseModel):
    inventory: List
    currency: List[CurrencyItem]
    heroes: List
    mail: Mail


class DailyQuests(BaseModel):
    next_timestamp: int
    quests: List[bool]


class Lootboxes1(BaseModel):
    L_001_FT: List
    L_WEK: List
    L_001: List[L001Item]
    L_002: List[L002Item]
    L_000: List[L000Item]
    L_005: List[L005Item]
    L_003: List[L003Item]
    L_004: List[L004Item]


class Mail1(BaseModel):
    lootboxes: Lootboxes1
    mail: Dict[str, Any]
    systemclaim: List[str]
    uid: str


class Model(BaseModel):
    rewards: Rewards
    daily_quests: DailyQuests
    mail: Mail1
    log: List[str]
