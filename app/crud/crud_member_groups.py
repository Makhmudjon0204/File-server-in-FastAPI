from sqlalchemy.orm import Session
from app.models.member_groups import MemberGroup
from app.schemas.schema_member_groups import MemberGroupCreate, MemberGroupUpdate

def get_member_group(db: Session, member_group_id: int):
    return db.query(MemberGroup).filter(MemberGroup.id == member_group_id).first()

def get_all_member_groups(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MemberGroup).offset(skip).limit(limit).all()

def create_member_group(db: Session, member_group: MemberGroupCreate):
    db_member_group = MemberGroup(
        group_id=member_group.group_id,
        member_id=member_group.member_id,
        created_date=member_group.created_date,
        updated_date=member_group.updated_date
    )
    db.add(db_member_group)
    db.commit()
    db.refresh(db_member_group)
    return db_member_group

def update_member_group(db: Session, member_group_id: int, member_group: MemberGroupUpdate):
    db_member_group = get_member_group(db, member_group_id)
    if db_member_group:
        for key, value in member_group.dict().items():
            setattr(db_member_group, key, value)
        db.commit()
        db.refresh(db_member_group)
    return db_member_group

def delete_member_group(db: Session, member_group_id: int):
    db_member_group = get_member_group(db, member_group_id)
    if db_member_group:
        db.delete(db_member_group)
        db.commit()
    return db_member_group