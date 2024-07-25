from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey


class GroupServices(Base):
    __tablename__ = 'group_services'
    group_id = Column(Integer, ForeignKey('service_group.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'), primary_key=True)