

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Model(BaseModel):
    customStatusCode: int
    error: str
    severity: int
    log: List[str]
