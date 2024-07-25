from app.database import Base
from sqlalchemy import Column, String, Integer, Text


class Services(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=True)
    short_description = Column(Text, nullable=True)
    full_info_link = Column(String(255), nullable=True)
