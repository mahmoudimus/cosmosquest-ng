

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Rewards(BaseModel):
    inventory: List
    currency: List[CurrencyItem]
    heroes: List


class Rewards1Item(BaseModel):
    item_class: str
    id: str
    quantity: Optional[int] = None
    rarity: Optional[int] = None


class Daily(BaseModel):
    next_timestamp: int
    next: int
    rewards: List[Rewards1Item]


class Model(BaseModel):
    rewards: Rewards
    daily: Daily
    log: List[str]
