from app.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime, timezone


class Members(Base):
    __tablename__ ='members'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=True)
    short_description = Column(Text, nullable=True)
    full_into_link = Column(String(255), nullable=True)
    created_dated = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_dated = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
