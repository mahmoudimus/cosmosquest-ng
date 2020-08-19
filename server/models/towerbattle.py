

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel


class Equip(BaseModel):
    eid: str
    rank: int
    id: str


class FriendUnit(BaseModel):
    id: str
    rank: int
    ascension: int
    atk: int
    hp: int
    level: int
    equip: Equip


class EnemyUnit(BaseModel):
    id: str
    rank: int
    ascension: int
    atk: int
    hp: int
    level: int


class Action(BaseModel):
    type: str
    animation: Optional[str] = None
    sourceFriendly: Optional[bool] = None
    sourceIndex: Optional[int] = None
    targetFriendly: Optional[bool] = None
    targetIndexes: Optional[List[int]] = None
    icon: Optional[str] = None
    duration: Optional[int] = None
    damage: Optional[Union[int, List[int]]] = None
    damagedFriendly: Optional[bool] = None
    damagedIndex: Optional[int] = None
    attackingFriendly: Optional[bool] = None
    attackingIndex: Optional[int] = None
    superEffective: Optional[bool] = None
    friendly: Optional[bool] = None
    index: Optional[int] = None
    superEffectiveIndexes: Optional[List[bool]] = None
    result: Optional[str] = None


class Battle(BaseModel):
    player1Name: str
    player1Avatar: str
    player2Name: str
    player2Avatar: str
    friendUnits: List[FriendUnit]
    enemyUnits: List[EnemyUnit]
    actions: List[Action]
    dmga: int
    dmgb: int
    dmgt: int
    rounds: int
    result: int


class InventoryItem(BaseModel):
    id: str
    quantity: int


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class L001Item(BaseModel):
    currency: List[CurrencyItem]
    inventory: List
    heroes: List
    lid: str


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
    inventory: List[InventoryItem]
    currency: List[CurrencyItem]
    heroes: List
    mail: Mail


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


class Rewards1(BaseModel):
    reward: Any
    reward_ft: Any


class Stats(BaseModel):
    attack: int
    health: int


class Team(BaseModel):
    id: str
    level: int
    ascension: int
    promotion: int
    stats: Stats


class Equip1(BaseModel):
    eid: str
    rank: int
    id: str


class InvasionTeamItem(BaseModel):
    hid: str
    equip: Optional[Equip1] = None
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


class RankingItem(BaseModel):
    uid: str
    score: str
    position: int
    name: str
    heroportrait: str
    invasion_team: List[InvasionTeamItem]


class InfinityData(BaseModel):
    floor: int
    max_floor: int
    rewards: Rewards1
    teams: List[Team]
    ranking: List[RankingItem]
    resettime: int


class Model(BaseModel):
    battle: Battle
    rewards: Rewards
    mail: Mail1
    infinity_data: InfinityData
    log: List[str]
