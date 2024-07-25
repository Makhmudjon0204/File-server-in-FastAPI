from pydantic import BaseModel


class CoursesBase(BaseModel):
    title: str
    short_description: str
    logo: str
    edu_link: str


class CoursesCreate(CoursesBase):
    pass


class CoursesUpdate(CoursesBase):
    pass


class Courses(CoursesBase):
    id: int

    class Config:
        orm_mode = True