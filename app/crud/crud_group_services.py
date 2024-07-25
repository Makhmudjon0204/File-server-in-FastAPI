from sqlalchemy.orm import Session
from app.models.group_services import GroupServices
from app.schemas.schema_group_services import GroupServicesCreate, GroupServicesUpdate

def get_group_service(db: Session, group_service_id: int):
    return db.query(GroupServices).filter(GroupServices.id == group_service_id).first()

def get_all_group_services(db: Session, skip: int = 0, limit: int = 10):
    return db.query(GroupServices).offset(skip).limit(limit).all()

def create_group_service(db: Session, group_service: GroupServicesCreate):
    db_group_service = GroupServices(
        group_id=group_service.group_id,
        service_id=group_service.service_id
    )
    db.add(db_group_service)
    db.commit()
    db.refresh(db_group_service)
    return db_group_service

def update_group_service(db: Session, group_service_id: int, group_service: GroupServicesUpdate):
    db_group_service = get_group_service(db, group_service_id)
    if db_group_service:
        for key, value in group_service.dict().items():
            setattr(db_group_service, key, value)
        db.commit()
        db.refresh(db_group_service)
    return db_group_service

def delete_group_service(db: Session, group_service_id: int):
    db_group_service = get_group_service(db, group_service_id)
    if db_group_service:
        db.delete(db_group_service)
        db.commit()
    return db_group_service