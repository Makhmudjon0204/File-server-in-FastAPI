from app.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime
from datetime import datetime, timezone


class Blogs(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    short_info = Column(Text, nullable=True)
    logo = Column(String(255), nullable=True)
    blog_link = Column(String(255), nullable=True)
    created_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
