from app.database import Base
from sqlalchemy import Column, String, Integer, Text, Date


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=True)
    logo = Column(String(255), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)