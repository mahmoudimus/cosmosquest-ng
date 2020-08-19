

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class InventoryItem(BaseModel):
    rank: int
    eid: str
    id: str
    quantity: int
    type: int


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Items(BaseModel):
    inventory: List[InventoryItem]
    heroes: List
    currency: List[CurrencyItem]


class Hero(BaseModel):
    hid: str
    quantity: int
    ascension: int
    level: int
    rare: bool
    busy: bool
    id: str
    type: int
    promotion: int


class L000Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List[Hero]
    lid: str


class L003Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List
    lid: str


class Lootboxes(BaseModel):
    L_001_FT: List
    L_WEK: List
    L_001: List
    L_002: List
    L_000: List[L000Item]
    L_005: List
    L_003: List[L003Item]
    L_004: List


class Mail(BaseModel):
    lootboxes: Lootboxes
    mail: Dict[str, Any]
    systemclaim: List[str]
    uid: str


class Model(BaseModel):
    items: Items
    price: int
    success: List[int]
    rushes: List[int]
    mail: Mail
    log: List[str]
