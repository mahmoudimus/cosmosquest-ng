

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel


class H0(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H1(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H2(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H3(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H4(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H5(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H6(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H7(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H8(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H9(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H10(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H11(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H12(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H13(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H14(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H15(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H16(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H17(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H18(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class H19(BaseModel):
    hid: str
    id: str
    ascension: int
    promotion: int
    level: int


class Pool(BaseModel):
    h0: H0
    h1: H1
    h2: H2
    h3: H3
    h4: H4
    h5: H5
    h6: H6
    h7: H7
    h8: H8
    h9: H9
    h10: H10
    h11: H11
    h12: H12
    h13: H13
    h14: H14
    h15: H15
    h16: H16
    h17: H17
    h18: H18
    h19: H19


class TeamItem(BaseModel):
    id: str
    ascension: int
    level: int
    promotion: int


class Equip(BaseModel):
    eid: str
    rank: int
    id: str


class InvasionTeamItem(BaseModel):
    hid: str
    equip: Optional[Equip] = None
    ascension: int
    level: int
    busy: bool
    id: str
    promotion: int
    item_class: Optional[str] = None
    key: Optional[str] = None


class RankingbestItem(BaseModel):
    uid: str
    score: str
    position: int
    name: str
    heroportrait: str
    invasion_team: List[InvasionTeamItem]


class ModelItem(BaseModel):
    type: int
    tid: str
    finishat: Optional[str] = None
    status: Union[int, str]
    next: str
    registered: bool
    pool: Optional[Pool] = None
    team: Optional[List[TeamItem]] = None
    rankingbest: Optional[List[RankingbestItem]] = None
    count: Optional[int] = None


class Model(BaseModel):
    __root__: List[ModelItem]
