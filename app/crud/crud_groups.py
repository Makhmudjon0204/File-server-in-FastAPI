from sqlalchemy.orm import Session
from app.models.groups import Groups
from app.schemas.schema_groups import GroupsCreate, GroupsUpdate

def get_group(db: Session, group_id: int):
    return db.query(Groups).filter(Groups.id == group_id).first()

def get_all_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Groups).offset(skip).limit(limit).all()

def create_group(db: Session, group: GroupsCreate):
    db_group = Groups(
        title=group.title,
        logo=group.logo,
        created_date=group.created_date,
        updated_date=group.updated_date
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def update_group(db: Session, group_id: int, group: GroupsUpdate):
    db_group = get_group(db, group_id)
    if db_group:
        for key, value in group.dict().items():
            setattr(db_group, key, value)
        db.commit()
        db.refresh(db_group)
    return db_group

def delete_group(db: Session, group_id: int):
    db_group = get_group(db, group_id)
    if db_group:
        db.delete(db_group)
        db.commit()
    return db_group