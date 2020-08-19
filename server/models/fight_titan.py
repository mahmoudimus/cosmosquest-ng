

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel


class Equip(BaseModel):
    eid: str
    rank: int
    id: str


class Equip1(BaseModel):
    eid: str
    rank: int
    id: str


class Equip2(BaseModel):
    eid: str
    rank: int
    id: str


class Equip3(BaseModel):
    eid: str
    rank: int
    id: str


class Equip4(BaseModel):
    eid: str
    rank: int
    id: str


class Equip5(BaseModel):
    eid: str
    rank: int
    id: str


class Equip6(BaseModel):
    eid: str
    rank: int
    id: str


class Equip7(BaseModel):
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
    is_titan: bool


class Action(BaseModel):
    type: str
    animation: Optional[str] = None
    sourceFriendly: Optional[bool] = None
    sourceIndex: Optional[int] = None
    targetFriendly: Optional[bool] = None
    targetIndexes: Optional[List[int]] = None
    damage: Optional[Union[int, List[int]]] = None
    superEffectiveIndexes: Optional[List[bool]] = None
    icon: Optional[str] = None
    duration: Optional[int] = None
    friendly: Optional[bool] = None
    index: Optional[int] = None
    damagedFriendly: Optional[bool] = None
    damagedIndex: Optional[int] = None
    attackingFriendly: Optional[bool] = None
    attackingIndex: Optional[int] = None
    superEffective: Optional[bool] = None
    result: Optional[str] = None


class Simulation(BaseModel):
    player1Name: str
    player1Avatar: str
    player2Name: str
    friendUnits: List[FriendUnit]
    enemyUnits: List[EnemyUnit]
    actions: List[Action]
    dmga: int
    dmgb: int
    dmgt: int
    rounds: int
    result: int


class Member(BaseModel):
    contribution: int
    last_week_contribution_update: int
    rank: int
    uid: str
    week_contribution: int


class DefenseTeam3Item(BaseModel):
    hid: str
    equip: Equip4
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


class DefenseTeam1Item(BaseModel):
    hid: str
    equip: Equip5
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


class DefenseTeam2Item(BaseModel):
    hid: str
    equip: Equip6
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


class TitanFight(BaseModel):
    id: str
    level: int
    promotion: int
    ascension: int
    current_hp: int
    max_hp: int
    version: int


class TitanTank(BaseModel):
    ascension: int
    id: str
    level: int
    promotion: int


class Titans(BaseModel):
    titan_tank: TitanTank


class TitanFight1(BaseModel):
    ascension: int
    current_hp: int
    id: str
    level: int
    max_hp: int
    promotion: int
    version: int


class TitanTank1(BaseModel):
    ascension: int
    id: str
    level: int
    promotion: int


class Titans1(BaseModel):
    titan_tank: TitanTank1


class ItemRequest(BaseModel):
    id: str
    expire: int
    quantity: int
    type: int
    uid: str
    item_class: str
    playername: str
    heroportrait: str
    eraportrait: str


class InvasionTeamItem(BaseModel):
    hid: str
    equip: Optional[Equip7] = None
    ascension: int
    level: int
    busy: bool
    id: str
    promotion: int
    item_class: Optional[str] = None
    key: Optional[str] = None


class MembersInfoItem(BaseModel):
    laston: int
    playerportrait: int
    playername: str
    maxera: int
    uid: str
    invasion_team: List[InvasionTeamItem]
    message: str
    eraportrait: str
    heroportrait: str


class EnemyInfo(BaseModel):
    war_battle_status: int
    elo: int
    shards_al: int
    defense_members: List[str]
    enemy: str
    motd: str
    selected_titan: str
    requests: List
    members: List[Member]
    defense_team3: List[DefenseTeam3Item]
    aid: str
    defense_team1: List[DefenseTeam1Item]
    defense_team2: List[DefenseTeam2Item]
    shards: Dict[str, Any]
    policy: int
    titan_fight: TitanFight1
    facilities: List[int]
    alname: str
    investigations: List[int]
    titan_damage: int
    logo_small: str
    logo: str
    registered: bool
    onium_al: int
    titan_set_timestamp: int
    res: int
    titans: Titans1
    war_status: str
    position: int
    item_requests: List[ItemRequest]
    level: str
    member_count: int
    max_member_count: int
    members_info: List[MembersInfoItem]
    requests_info: List


class Alliance(BaseModel):
    war_battle_status: int
    elo: int
    shards_al: int
    defense_members: List[str]
    enemy: str
    motd: str
    selected_titan: str
    requests: List[str]
    members: List[Member]
    defense_team3: List[DefenseTeam3Item]
    aid: str
    defense_team1: List[DefenseTeam1Item]
    defense_team2: List[DefenseTeam2Item]
    shards: Dict[str, Any]
    policy: int
    titan_fight: TitanFight
    facilities: List[int]
    apera: int
    alname: str
    investigations: List[int]
    titan_damage: int
    logo_small: str
    logo: str
    registered: bool
    onium_al: int
    titan_lvl_cooldown: int
    titan_set_timestamp: int
    res: int
    titans: Titans
    war_status: str
    position: int
    item_requests: List
    enemy_info: EnemyInfo


class Donation(BaseModel):
    blueprints: int
    last_day: int
    population: int


class Social(BaseModel):
    war_attacks_performed: int
    rank: int
    donation: Donation
    last_titan_attack: int
    defense_setup: int
    aid: str
    status: int


class InventoryItem(BaseModel):
    id: str
    quantity: int


class CurrencyItem(BaseModel):
    id: str
    quantity: int


class Items(BaseModel):
    inventory: List[InventoryItem]
    currency: List[CurrencyItem]
    heroes: List


class Result(BaseModel):
    simulation: Simulation
    alliance: Alliance
    social: Social
    items: Items
    titan_damage: int
    defeated: bool
    onium: int
    shards: int
    showRewards: bool


class Model(BaseModel):
    result: Result
    log: List[str]
