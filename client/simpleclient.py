import argparse
import datetime
import json
import logging
import pprint
import typing
from dataclasses import dataclass

from itertools import repeat, chain
from collections import defaultdict

import ipdb
import requests
import requests.cookies
import sys
import time
from pydantic import ValidationError

from server import models as m


# constants
TIME_OF_RUN = datetime.datetime.now()
DEFAULT_USER_AGENT = 'KosmosQuest'
HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': DEFAULT_USER_AGENT,
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Accept-Language': 'en-us',
}

# module scoped
logger = logging.getLogger(__name__)


def add_logging_options(options):
    options.add_argument(
        "-l",
        "--log-level",
        default="info",
        help="Set the logging level",
        choices=["debug", "info", "warn", "warning", "error", "critical"],
    )
    options.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Verbose output is equivalent to setting debug logging level",
    )
    return options


def conf_logging():
    _log = logging.getLogger()
    # fmt="%(funcName)s():%(lineno)i: %(message)s %(levelname)s"
    _fmt = "%(funcName)s() ➡ %(lineno)i:@%(asctime)s:%(levelname)s: %(message)s"
    formatter = logging.Formatter(_fmt)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    _log.addHandler(handler)


def set_log_lvl(cli_arguments, log_level=None):
    _log = logging.getLogger()

    if log_level is None:  # Not sure if log_level can be the number 0
        log_level = cli_arguments.log_level.upper()
    if isinstance(log_level, str):
        log_level = log_level.upper()  # check to make sure it is upper
        log_level = getattr(logging, log_level)
    _log.setLevel(log_level)


def _add_options(p: argparse.ArgumentParser) -> argparse.ArgumentParser:
    p.add_argument(
        "--starting-era",
        action="store",
        type=int,
        default=0,
        help="Beginning era to execute from"
    )
    p.add_argument(
        "--ending-era",
        action="store",
        type=int,
        default=11,
        help="Ending era to stop executing"
    )
    p.add_argument(
        "-m", "--missions",
        action="store",
        type=int,
        default=5,
        help="How many missions per era?"
    )
    p.add_argument(
        "--all-missions",
        action="store_true",
        default=False,
        help="All missions per era"
    )
    p.add_argument(
        "--sleep",
        action="store",
        type=int,
        default=5,
        help="Sleep interval between requests"
    )
    p.add_argument(
        "-r", "--responses",
        dest="save_response",
        action="store_true",
        default=False,
        help="store responses, disabled by default"
    )
    p.add_argument(
        "--time-travel",
        dest="time_travel",
        action="store_true",
        default=False,
        help="Manual time travel"
    )
    return p


def login2(args, kong_auth_token):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': DEFAULT_USER_AGENT,
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Accept-Language': 'en-us'
    }

    data = {
        'lid': '',
        'kongid': '',
        'kong_auth': kong_auth_token,
        'uniqueid': '',
        'function': 'login2'
    }

    r = requests.post(
        'https://cq.gaiabyte.com/character',
        headers=headers,
        data=json.dumps(data)
    )
    if r.status_code == 200:
        logger.debug('login2: %s', r.json())
        return r.json()['token']
    else:
        r.raise_for_status()


@dataclass
class Hero(object):
    name: str
    hid: str


class Equipment(object):

    CARNAGE_BOMB = {"eid": "Exxxx"}


class Heroes(object):

    SNIPER = Hero("sniper", "Hxxx")
    PILOT = Hero("pilot", "Hxxx")
    INFECTED = Hero("infected", "Hxxx")
    BRAINIAC = Hero("brainiac", "Hxxx")
    HACKER = Hero("hacker", "Hxxx")
    BLACK_HOLE_CANNON = Hero("black_hole_cannon", "Hxxx")
    CYBORG = Hero("cyborg", "Hxxx")
    ORACLE = Hero("oracle", "Hxxx")
    ORB_SUMMONER = Hero("orb_summoner", "Hxxx")
    STARGAZER = Hero("stargazer", "Hxxx")
    CANNON = Hero("cannon", "Hxxx")
    MONSTER = Hero("monster", "Hxxx")
    PALADIN = Hero("paladin", "Hxxx")
    MONK = Hero("monk", "Hxxx")
    TANK = Hero("tank", "Hxxx")
    CATAPULT = Hero("catapult", "Hxxx")



def _on_err(status_code, err):
    try:
        r = m.errors.Model(**err)
    except ValidationError:
        r = m.errors.Model.construct(**err)

    logger.info(r)
    if r.customStatusCode == 4300 or r.error == 'SRV_ERROR_4300':
        pass
    else:
        pass
    if (err.get('customStatusCode') == 4300 or
            err.get('error') == 'SRV_ERROR_4300'):
        logger.info(f"Skipping era! No warps available! :: {err}")
    else:
        logger.info(f"Result: {status_code} - ERROR! :: {err}")


def execute(args: argparse.Namespace) -> typing.Dict[typing.Any, list]:
    set_log_lvl(args, logging.getLevelName("DEBUG") if args.verbose else None)
    logger.debug(args)

    kong_auth_token = get_kong_auth_token(args)
    logger.debug('kong_auth_token: %s', kong_auth_token)
    token = login2(args, kong_auth_token)
    logger.debug('token: %s', token)

    eras = defaultdict(list)
    if args.time_travel:
        play_timetravel(token)
    else:
        try:
            play_freeadcrate2(token)
            play_getboost2(token)
            play_alliance_donation(token)
            play_defense_team(token)
            play_fight_titan(token)
            play_greet_all(token)
            play_expeditionendall(token)
            play_expeditionstart(token)
            play_towerbattle(token, team=[], fightall=True)
            play_claim_daily_data(token)
            play_claim_daily_mission(token)
            play_extraconquestbattle2(token, args, eras)
        except Exception as e:
            logger.exception("Exception has been raised!", e)

    return eras


"""
actionlistconsume
alliance_donation
characterdataupdate
claim_daily_data
claim_daily_mission
defense_team
errors
extraconquestbattle2
fight_titan
general
get_alliance_info
get_friends_data
getmail
getpasttournaments
gettournamentdata
greet_all
invasionbattle
invasiondata
promote-character
shopbuyitem
timetravel
tournamentregister
towerbattle
"""


def log_response(eras, log_fname=f'responses-{TIME_OF_RUN:%Y%m%d%H%M%S}.json'):
    if not eras:
        return

    with open(log_fname, 'w', encoding='utf-8') as fo:
        json.dump(eras, fo, ensure_ascii=False, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Cosmos Quest Client"
    )
    parser = add_logging_options(parser)
    parser = _add_options(parser)
    args = parser.parse_args()
    conf_logging()
    try:
        eras = execute(args)
    except Exception as ex:
        ipdb.pm()
    else:
        if args.save_response:
            log_response(eras)


if __name__ == "__main__":
    main()
