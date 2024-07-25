from app.database import Base
from sqlalchemy import Column, String, Integer


class ServiceGroup(Base):
    __tablename__ = 'service_group'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False) 
    logo = Column(String(255), nullable=True)
