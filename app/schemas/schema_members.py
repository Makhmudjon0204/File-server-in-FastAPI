from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MembersBase(BaseModel):
    full_name: str
    image: Optional[str] = None
    short_description: Optional[str] = None
    full_info_link: Optional[str] = None


class MembersCreate(MembersBase):
    created_date: datetime
    updated_date: datetime


class MembersUpdate(MembersBase):
    updated_date: datetime


class Members(MembersBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True