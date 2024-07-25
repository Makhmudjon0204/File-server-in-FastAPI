from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, session, engine
from app.schemas import schema_member_groups
from app.crud import crud_member_groups

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_member_groups.MemberGroup)
async def create_member_group(member_group: schema_member_groups.MemberGroupCreate, db: Session = Depends(get_db)):
    return crud_member_groups.create_member_group(db=db, member_group=member_group)


@router.get("/{group_id}/{member_id}", response_model=schema_member_groups.MemberGroup)
async def read_member_group(group_id: int, member_id: int, db: Session = Depends(get_db)):
    db_member_group = crud_member_groups.get_member_group(db, group_id=group_id, member_id=member_id)
    if db_member_group is None:
        raise HTTPException(status_code=404, detail="Member group not found")
    return db_member_group


@router.get("/", response_model=List[schema_member_groups.MemberGroup])
async def read_member_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    member_groups = crud_member_groups.get_all_member_groups(db, skip=skip, limit=limit)
    return member_groups


@router.delete("/{group_id}/{member_id}", response_model=schema_member_groups.MemberGroup)
async def delete_member_group(group_id: int, member_id: int, db: Session = Depends(get_db)):
    db_member_group = crud_member_groups.delete_member_group(db, group_id=group_id, member_id=member_id)
    if db_member_group is None:
        raise HTTPException(status_code=404, detail="Member group not found")
    return db_member_group