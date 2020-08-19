

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Items(BaseModel):
    inventory: List
    currency: List[CurrencyItem]
    heroes: List


class InventoryItem(BaseModel):
    rank: Optional[int] = None
    eid: Optional[str] = None
    id: str
    quantity: int
    type: Optional[int] = None


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


class L00TItem(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List[Hero]
    lid: str


class Lootboxes(BaseModel):
    L_001_FT: List
    L_WEK: List
    L_001: List[L00TItem]
    L_002: List[L00TItem]
    L_000: List[L00TItem]
    L_005: List[L00TItem]
    L_003: List[L00TItem]
    L_004: List[L00TItem]


class Mail(BaseModel):
    lootboxes: Lootboxes
    mail: Dict[str, Any]
    systemclaim: List[str]
    uid: str


class AdData(BaseModel):
    next: int
    reward: int


class Result(BaseModel):
    items: Items
    mail: Mail
    ad_data: AdData


class Model(BaseModel):
    result: Result
    log: List[str]
