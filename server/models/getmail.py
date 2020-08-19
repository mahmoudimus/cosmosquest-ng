

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class CurrencyItem(BaseModel):
    id: str
    quantity: int


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


class Loot(BaseModel):
    currency: List[CurrencyItem]
    inventory: List[InventoryItem]
    heroes: List[Hero]
    lid: str


class L000Item(Loot):
    pass


class L001Item(Loot):
    pass


class L002Item(Loot):
    pass


class L003Item(Loot):
    pass


class L004Item(Loot):
    pass


class L005Item(Loot):
    pass


class LWEKItem(Loot):
    pass


class Lootboxes(BaseModel):
    L_001_FT: List
    L_WEK: List[LWEKItem]
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


class Model(BaseModel):
    mail: Mail
    log: List[str]
