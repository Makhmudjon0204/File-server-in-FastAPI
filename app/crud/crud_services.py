from sqlalchemy.orm import Session
from app.models.services import Services
from app.schemas.services import ServicesCreate, ServicesUpdate

def get_service(db: Session, service_id: int):
    return db.query(Services).filter(Services.id == service_id).first()

def get_all_services(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Services).offset(skip).limit(limit).all()

def create_service(db: Session, service: ServicesCreate):
    db_service = Services(
        service_name=service.service_name,
        image=service.image,
        short_description=service.short_description,
        full_info_link=service.full_info_link
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def update_service(db: Session, service_id: int, service: ServicesUpdate):
    db_service = get_service(db, service_id)
    if db_service:
        for key, value in service.dict().items():
            setattr(db_service, key, value)
        db.commit()
        db.refresh(db_service)
    return db_service

def delete_service(db: Session, service_id: int):
    db_service = get_service(db, service_id)
    if db_service:
        db.delete(db_service)
        db.commit()
    return db_service