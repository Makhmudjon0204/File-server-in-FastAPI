from sqlalchemy.orm import Session
from app.models.member_info import MemberInfo
from app.schemas.schema_member_info import MemberInfoCreate, MemberInfoUpdate

def get_member_info(db: Session, member_info_id: int):
    return db.query(MemberInfo).filter(MemberInfo.id == member_info_id).first()

def get_all_member_info(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MemberInfo).offset(skip).limit(limit).all()

def create_member_info(db: Session, member_info: MemberInfoCreate):
    db_member_info = MemberInfo(
        first_name=member_info.first_name,
        last_name=member_info.last_name,
        title=member_info.title,
        member_id=member_info.member_id,
        description=member_info.description,
        created_date=member_info.created_date,
        updated_date=member_info.updated_date
    )
    db.add(db_member_info)
    db.commit()
    db.refresh(db_member_info)
    return db_member_info

def update_member_info(db: Session, member_info_id: int, member_info: MemberInfoUpdate):
    db_member_info = get_member_info(db, member_info_id)
    if db_member_info:
        for key, value in member_info.dict().items():
            setattr(db_member_info, key, value)
        db.commit()
        db.refresh(db_member_info)
    return db_member_info

def delete_member_info(db: Session, member_info_id: int):
    db_member_info = get_member_info(db, member_info_id)
    if db_member_info:
        db.delete(db_member_info)
        db.commit()
    return db_member_info