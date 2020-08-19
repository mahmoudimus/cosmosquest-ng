

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Items(BaseModel):
    inventory: List
    heroes: List
    currency: List[CurrencyItem]


class Result(BaseModel):
    quantity: int
    items: Items
    um_earned: int
    next_greet: int


class Model(BaseModel):
    result: Result
    log: List[str]
