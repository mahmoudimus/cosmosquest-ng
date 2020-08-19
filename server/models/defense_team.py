

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Member(BaseModel):
    contribution: int
    last_week_contribution_update: int
    rank: int
    uid: str
    week_contribution: int


class TitanFight(BaseModel):
    ascension: int
    current_hp: int
    id: str
    level: int
    max_hp: int
    promotion: int
    version: int


class TitanTank(BaseModel):
    ascension: int
    id: str
    level: int
    promotion: int


class Titans(BaseModel):
    titan_tank: TitanTank


class Equip(BaseModel):
    eid: str
    rank: int
    id: str


class DefenseTeam3Item(BaseModel):
    hid: str
    equip: Equip
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


class Equip1(BaseModel):
    eid: str
    rank: int
    id: str


class DefenseTeam1Item(BaseModel):
    hid: str
    equip: Equip1
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


class Equip2(BaseModel):
    eid: str
    rank: int
    id: str


class DefenseTeam2Item(BaseModel):
    hid: str
    equip: Equip2
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


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


class Equip3(BaseModel):
    eid: str
    rank: int
    id: str


class InvasionTeamItem(BaseModel):
    hid: str
    equip: Optional[Equip3] = None
    ascension: int
    level: int
    busy: bool
    id: str
    item_class: Optional[str] = None
    key: Optional[str] = None
    promotion: int


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
    defense_team3: List
    aid: str
    defense_team1: List
    defense_team2: List
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


class Result(BaseModel):
    alliance: Alliance
    social: Social


class Model(BaseModel):
    result: Result
    log: List[str]
