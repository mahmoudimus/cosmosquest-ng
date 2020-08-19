

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel


class Model(BaseModel):
    defending_time: datetime
    log: List[str]
