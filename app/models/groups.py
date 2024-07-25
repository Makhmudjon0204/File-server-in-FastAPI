from app.database import Base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime, timezone


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    logo = Column(String(255), nullable=True)
    created_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))