# backend/app/schemas.py
from pydantic import BaseModel
from typing import List


class TabData(BaseModel):
    host: str
    url: str
    title: str


class GroupResponse(BaseModel):
    groups: List[int]