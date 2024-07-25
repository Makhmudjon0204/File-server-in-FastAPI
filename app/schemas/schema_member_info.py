from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class MemberInfoBase(BaseModel):
    first_name: str
    last_name: str
    title: str
    member_id: int
    description: Optional[str] = None


class MemberInfoCreate(MemberInfoBase):
    created_date: datetime
    updated_date: datetime


class MemberInfoUpdate(MemberInfoBase):
    updated_date: datetime


class MemberInfo(MemberInfoBase):
    id: int
    create_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True