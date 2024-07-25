from app.database import Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


class MemberInfo(Base):
    __tablename__ ='member_info'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'))
    description = Column(Text, nullable=True)
    created_dated = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_dated = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    member = relationship("Member")