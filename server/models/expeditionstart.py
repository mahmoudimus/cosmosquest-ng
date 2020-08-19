

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Model(BaseModel):
    result: bool
    log: List[str]
