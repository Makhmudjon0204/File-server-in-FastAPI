from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class GroupsBase(BaseModel):
    title: str
    logo: Optional[str] = None


class GroupsCreate(GroupsBase):
    created_date: datetime
    updated_date: datetime


class GroupsUpdate(GroupsBase):
    updated_date: datetime


class Groups(GroupsBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True