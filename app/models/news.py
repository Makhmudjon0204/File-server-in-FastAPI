from app.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime, timezone


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    logo = Column(String(255), nullable=True)
    full_text = Column(Text, nullable=True)
    created_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))