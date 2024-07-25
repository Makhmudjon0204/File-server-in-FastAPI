from datetime import datetime
from pydantic import BaseModel


class BlogsBase(BaseModel):
    title: str
    short_info: str
    logo: str
    blog_link: str


class BlogsCreate(BlogsBase):
    created_date: datetime
    updated_date: datetime


class BlogsUpdate(BlogsBase):
    updated_date: datetime


class Blogs(BlogsBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True