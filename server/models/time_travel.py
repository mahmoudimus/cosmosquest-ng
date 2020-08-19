

from __future__ import annotations

from datetime import datetime
from typing import List, Dict

from pydantic import BaseModel


class Expedition(BaseModel):
    begintime: datetime
    hero: str
    used: bool
    exptype: int
    unlocked: bool


class Result(BaseModel):
    expeditions: Dict[str, Expedition]
    population: int
    projects: Dict[str, datetime]


class Model(BaseModel):
    result: Result
    log: List[str]
