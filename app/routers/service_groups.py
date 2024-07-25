from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, session, engine
from app.schemas import service_groups
from app.crud import crud_services_groups

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=service_groups.ServiceGroup)
async def create_service_group(service_group: service_groups.ServiceGroupCreate, db: Session = Depends(get_db)):
    return crud_services_groups.create_service_group(db=db, service_group=service_group)


@router.get("/{service_group_id}", response_model=service_groups.ServiceGroup)
async def read_service_group(service_group_id: int, db: Session = Depends(get_db)):
    db_service_group = crud_services_groups.get_service_group(db, service_group_id=service_group_id)
    if db_service_group is None:
        raise HTTPException(status_code=404, detail="Service group not found")
    return db_service_group


@router.get("/", response_model=List[service_groups.ServiceGroup])
async def read_service_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service_groups = crud_services_groups.get_all_service_groups(db, skip=skip, limit=limit)
    return service_groups


@router.put("/{service_group_id}", response_model=service_groups.ServiceGroup)
async def update_service_group(service_group_id: int, service_group: service_groups.ServiceGroupCreate,
                         db: Session = Depends(get_db)):
    db_service_group = crud_services_groups.update_service_group(db, service_group_id=service_group_id, service_group=service_group)
    if db_service_group is None:
        raise HTTPException(status_code=404, detail="Service group not found")
    return db_service_group


@router.delete("/{service_group_id}", response_model=service_groups.ServiceGroup)
async def delete_service_group(service_group_id: int, db: Session = Depends(get_db)):
    db_service_group = crud_services_groups.delete_service_group(db, service_group_id=service_group_id)
    if db_service_group is None:
        raise HTTPException(status_code=404, detail="Service group not found")
    return db_service_group