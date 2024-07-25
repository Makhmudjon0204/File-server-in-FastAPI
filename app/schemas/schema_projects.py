from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProjectsBase(BaseModel):
    title: str
    body: Optional[str] = None
    logo: str
    start_date: date
    end_date: date


class ProjectsCreate(ProjectsBase):
    pass


class ProjectsUpdate(ProjectsBase):
    pass


class Projects(ProjectsBase):
    id: int

    class Config:
        orm_mode = True