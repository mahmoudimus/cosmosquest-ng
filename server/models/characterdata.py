

from __future__ import annotations
from datetime import datetime

from typing import List, Optional

from pydantic import BaseModel


class AdInfoItem(BaseModel):
    adName: str
    next: datetime
    times: int


class Ads(BaseModel):
    lastCrate: datetime
    lastBoost: datetime
    lastReturn: int
    adInfo: List[AdInfoItem]


class ShopManager(BaseModel):
    cratesBought: int


class Energy(BaseModel):
    m: float
    e: int


class TotalEnergy(BaseModel):
    m: float
    e: int


class UM(BaseModel):
    m: float
    e: int


class Prana(BaseModel):
    m: int
    e: int


class BonusEnergy(BaseModel):
    m: int
    e: int


class Multiplier(BaseModel):
    m: int
    e: int


class Total(BaseModel):
    m: float
    e: int


class BigCrunchMul(BaseModel):
    m: float
    e: int


class OmegaMul(BaseModel):
    m: float
    e: int


class Contribution(BaseModel):
    m: float
    e: int


class PopulationMultiplier(BaseModel):
    m: int
    e: int


class PermanentBonuses(BaseModel):
    bonusEnergy: BonusEnergy
    multiplier: Multiplier
    exponent: int
    total: Total
    bigCrunchMul: BigCrunchMul
    omegaMul: OmegaMul
    contribution: Contribution
    populationMultiplier: PopulationMultiplier


class Omegacount(BaseModel):
    m: float
    e: int


class Omegagained(BaseModel):
    m: float
    e: int


class GameData(BaseModel):
    energy: Energy
    totalEnergy: TotalEnergy
    UM: UM
    prana: Prana
    permanentBonuses: PermanentBonuses
    lastBigCrunch: datetime
    maxSpecie: int
    currentPortrait: int
    buildings: List[int]
    researchers: int
    research: str
    discoveredHeroes: List[str]
    discoveredResearches: str
    pausedResearches: List
    currentresearches: List
    houses: List[datetime]
    omegas: List[int]
    omegacount: Omegacount
    omegagained: Omegagained
    species: List[int]
    boughtUM: bool
    oneTimeOffers: List[str]
    shopPurchases: List


class OmegaGain(BaseModel):
    m: float
    e: int


class ProductionMul(BaseModel):
    m: float
    e: int


class BigCrunch(BaseModel):
    omegaGain: OmegaGain
    productionMul: ProductionMul
    speciesTimer: int
    bonusRotation: int


class Actionlist(BaseModel):
    list: List


class AchItem(BaseModel):
    key: str
    level: int


class Achievements(BaseModel):
    ach: List[AchItem]


class SystemSettings(BaseModel):
    formatMode: int
    language: str
    buildingMode: str
    showClicks: bool
    tapSound: bool
    effectSound: bool
    musicSound: bool


class Antiparticles(BaseModel):
    board: List


class Heroes(BaseModel):
    favoriteHeroes: List[str]


class Setup(BaseModel):
    key: str
    Expedition0: Optional[List[str]] = None
    Expedition1: Optional[List[str]] = None
    Expedition2: Optional[List[str]] = None
    Expedition3: Optional[List[str]] = None
    infinityTeam: Optional[List[str]] = None
    ExtraConquest: Optional[List[str]] = None
    allianceadefense: Optional[List[str]] = None
    titan_fight: Optional[List[str]] = None
    Invasion: Optional[List[str]] = None


class TeamSetups(BaseModel):
    Setups: List[Setup]


class MailData(BaseModel):
    readMails: List[str]


class BoostManager(BaseModel):
    list: List


class DailyQuests(BaseModel):
    QuestProgress: List[int]
    timestamp: datetime


class DiscardedOffers(BaseModel):
    discardedOffers: List[str]


class Tutorial(BaseModel):
    step: int


class Value(BaseModel):
    m: float
    e: int


class CurrentStat(BaseModel):
    """
    [
      "TotalHousesClaimed",
      "TotalHousesClaimed0",
      "PopulationWonByHouses",
      "PopulationWon",
      "MaxPopulation",
      "TotalHousesClaimed1",
      "TotalHousesClaimed2",
      "TotalHousesClaimed3",
      "TotalHousesClaimed4",
      "TotalHousesClaimed5",
      "TotalHousesClaimed6",
      "TotalHousesClaimed8",
      "TotalHousesClaimed7",
      "TotalHousesClaimed9",
      "TotalHousesClaimed10",
      "Generated energy",
      "Max energy",
      "Play Time",
      "Clicks",
      "Click energy",
      "Max clicks per second",
      "Building0",
      "Total Buildings",
      "Max Buildings",
      "Maximum Production",
      "TotalResearches",
      "ResearchesInARun",
      "Total Research Time",
      "Building1",
      "Evolved",
      "SpeciesEvolveAncient Age",
      "TimeToSpecies1",
      "Building2",
      "SpeciesEvolveMedieval Age",
      "TimeToSpecies2",
      "Building3",
      "LastSave",
      "accountAge",
      "Disaster amount",
      "Disaster clicks",
      "SpeciesEvolveAge of Discovery",
      "TimeToSpecies3",
      "Building4",
      "SpeciesEvolveIndustrial Age",
      "TimeToSpecies4",
      "SpeciesEvolveModern Age",
      "TimeToSpecies5",
      "SpeciesEvolveAge of Information",
      "TimeToSpecies6",
      "Building5",
      "Building6",
      "SpeciesEvolveTranshumanism",
      "TimeToSpecies7",
      "Building7",
      "cratesOpened",
      "MissedDisasters",
      "Time offline",
      "SpeciesEvolveSeer",
      "TimeToSpecies8",
      "SpeciesEvolveGuardian",
      "TimeToSpecies9",
      "SpeciesEvolveMastermind",
      "TimeToSpecies10",
      "TournamentJoinedArena",
      "TotalTimeTravel",
      "TimeTravelsUsed",
      "TotalExpeditionsClaimed",
      "TotalExpeditionsClaimed0",
      "ExpeditionTime",
      "TotalExpeditionsStarted",
      "TotalExpeditionsStarted2",
      "upgradedItems",
      "TournamentJoinedChampionship",
      "TotalPromotions",
      "TotalAscensions",
      "TotalExpeditionsStarted1",
      "TotalExpeditionsStarted0",
      "TournamentJoinedBattleground"
    ]
    """
    key: str
    value: Value
    type: int
    replace: Optional[int] = None


class Value1(BaseModel):
    m: float
    e: int


class HistoryStat(BaseModel):
    key: str
    value: Value1
    type: int
    replace: Optional[int] = None


class CData(BaseModel):
    CurrentStats: List[CurrentStat]
    DailyQuests: DailyQuests
    HistoryStats: List[HistoryStat]
    MailData: MailData
    achievements: Achievements
    actionlist: Actionlist
    ads: Ads
    antiparticles: Antiparticles
    bigCrunch: BigCrunch
    boostManager: BoostManager
    discardedOffers: DiscardedOffers
    firstSave: datetime
    gameData: GameData
    heroes: Heroes
    shopManager: ShopManager
    systemSettings: SystemSettings
    teamSetups: TeamSetups
    tutorial: Tutorial
    updatetime: datetime
    version: int


class Model(BaseModel):
    cdata: CData
    token: str
    function: str
