from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db, session, engine
from app.schemas import schema_member_info
from app.crud import crud_members_info

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_member_info.MemberInfo)
async def create_member_info(member_info: schema_member_info.MemberInfoCreate, db: Session = Depends(get_db)):
    return crud_members_info.create_member_info(db=db, member_info=member_info)


@router.get("/{member_info_id}", response_model=schema_member_info.MemberInfo)
async def read_member_info(member_info_id: int, db: Session = Depends(get_db)):
    db_member_info = crud_members_info.get_member_info(db, member_info_id=member_info_id)
    if db_member_info is None:
        raise HTTPException(status_code=404, detail="MemberInfo not found")
    return db_member_info


@router.get("/", response_model=List[schema_member_info.MemberInfo])
async def read_member_infos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    member_infos = crud_members_info.get_all_member_info(db, skip=skip, limit=limit)
    return member_infos


@router.put("/{member_info_id}", response_model=schema_member_info.MemberInfo)
async def update_member_info(member_info_id: int, member_info: schema_member_info.MemberInfoCreate, db: Session = Depends(get_db)):
    db_member_info = crud_members_info.update_member_info(db, member_info_id=member_info_id, member_info=member_info)
    if db_member_info is None:
        raise HTTPException(status_code=404, detail="MemberInfo not found")
    return db_member_info


@router.delete("/{member_info_id}", response_model=schema_member_info.MemberInfo)
async def delete_member_info(member_info_id: int, db: Session = Depends(get_db)):
    db_member_info = crud_members_info.delete_member_info(db, member_info_id=member_info_id)
    if db_member_info is None:
        raise HTTPException(status_code=404, detail="MemberInfo not found")
    return db_member_info