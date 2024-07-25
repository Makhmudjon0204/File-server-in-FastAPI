from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db, session, engine
from app.schemas import schema_members
from app.crud import crud_members

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_members.Members)
async def create_member(member: schema_members.MembersCreate, db: Session = Depends(get_db)):
    return crud_members.create_member(db=db, member=member)


@router.get("/{member_id}", response_model=schema_members.Members)
async def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud_members.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@router.get("/", response_model=List[schema_members.Members])
async def read_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    members = crud_members.get_all_members(db, skip=skip, limit=limit)
    return members


@router.put("/{member_id}", response_model=schema_members.Members)
async def update_member(member_id: int, member: schema_members.MembersCreate, db: Session = Depends(get_db)):
    db_member = crud_members.update_member(db, member_id=member_id, member=member)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@router.delete("/{member_id}", response_model=schema_members.Members)
async def delete_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud_members.delete_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member