from pydantic import BaseModel
from typing import Optional


class ServicesBase(BaseModel):
    service_name: str
    image: Optional[str] = None
    short_description: Optional[str] = None
    full_info_link: Optional[str] = None


class ServicesCreate(ServicesBase):
    pass


class ServicesUpdate(ServicesBase):
    pass


class Services(ServicesBase):
    id: int

    class Config:
        orm_mode = True