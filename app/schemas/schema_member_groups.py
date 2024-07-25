from datetime import datetime
from pydantic import BaseModel


class MemberGroupBase(BaseModel):
    group_id: int
    member_id: int


class MemberGroupCreate(MemberGroupBase):
    created_date: datetime
    updated_date: datetime


class MemberGroupUpdate(MemberGroupBase):
    updated_date: datetime


class MemberGroup(MemberGroupBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True