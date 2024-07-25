from app.database import Base
from sqlalchemy import Column, String, Integer, Text


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False) 
    short_description = Column(Text, nullable=True)
    logo = Column(String(255), nullable=True)
    edu_link = Column(String(255), nullable=True)
