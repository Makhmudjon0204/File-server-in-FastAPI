from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import schema_groups
from app.database import get_db, session, engine
from app.crud import crud_groups

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_groups.Groups)
async def create_group(group: schema_groups.GroupsCreate, db: Session = Depends(get_db)):
    return crud_groups.create_group(db=db, group=group)


@router.get("/{group_id}", response_model=schema_groups.Groups)
async def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud_groups.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group


@router.get("/", response_model=List[schema_groups.Groups])
async def read_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    groups = crud_groups.get_all_groups(db, skip=skip, limit=limit)
    return groups


@router.put("/{group_id}", response_model=schema_groups.Groups)
async def update_group(group_id: int, group: schema_groups.GroupsCreate, db: Session = Depends(get_db)):
    db_group = crud_groups.update_group(db, group_id=group_id, group=group)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group


@router.delete("/{group_id}", response_model=schema_groups.Groups)
async def delete_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud_groups.delete_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group