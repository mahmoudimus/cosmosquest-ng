

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel


class Stats(BaseModel):
    attack: int
    health: int


class Enemy(BaseModel):
    ascension: int
    id: str
    level: int
    promotion: int
    stats: Stats


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Hero(BaseModel):
    ascension: int
    busy: bool
    hid: str
    id: str
    level: int
    promotion: int
    quantity: int
    rare: bool
    type: int


class InventoryItem(BaseModel):
    id: str
    quantity: int


class Rewards(BaseModel):
    currency: List[CurrencyItem]
    heroes: List[Hero]
    inventory: List[InventoryItem]


class ExtraItem(BaseModel):
    enemies: List[Enemy]
    lasttimestamp: int
    next: int
    rewards: Rewards
    warps: int


class Items(BaseModel):
    currency: List[CurrencyItem]
    heroes: List
    inventory: List[InventoryItem]


class Action(BaseModel):
    animation: Optional[str] = None
    duration: Optional[int] = None
    icon: Optional[str] = None
    sourceFriendly: Optional[bool] = None
    sourceIndex: Optional[int] = None
    targetFriendly: Optional[bool] = None
    targetIndexes: Optional[List[int]] = None
    type: str
    attackingFriendly: Optional[bool] = None
    attackingIndex: Optional[int] = None
    damage: Optional[Union[int, List[int]]] = None
    damagedFriendly: Optional[bool] = None
    damagedIndex: Optional[int] = None
    superEffective: Optional[bool] = None
    friendly: Optional[bool] = None
    index: Optional[int] = None
    superEffectiveIndexes: Optional[List[bool]] = None
    result: Optional[str] = None


class EnemyUnit(BaseModel):
    ascension: int
    atk: int
    hp: int
    id: str
    level: int
    rank: int


class Equip(BaseModel):
    eid: str
    id: str
    rank: int


class FriendUnit(BaseModel):
    ascension: int
    atk: int
    equip: Equip
    hp: int
    id: str
    level: int
    rank: int


class Simulation(BaseModel):
    actions: List[Action]
    dmga: int
    dmgb: int
    dmgt: int
    enemyUnits: List[EnemyUnit]
    friendUnits: List[FriendUnit]
    player1Avatar: str
    player1Name: str
    player2Avatar: str
    player2Name: str
    result: int
    rounds: int


class Model(BaseModel):
    extra: Union[ExtraItem, List[ExtraItem]]
    items: Items
    log: List[str]
    simulation: Simulation
    win: bool
