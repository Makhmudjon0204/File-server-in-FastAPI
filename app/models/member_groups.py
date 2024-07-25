from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime, timezone


class MemberGroup(Base):
    __tablename__ ='member_group'

    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), primary_key=True)
    created_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
