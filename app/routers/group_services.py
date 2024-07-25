from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, session, engine
from app.schemas import schema_group_services
from app.crud import crud_group_services

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_group_services.GroupServices)
async def create_group_service(group_service: schema_group_services.GroupServicesCreate, db: Session = Depends(get_db)):
    return crud_group_services.create_group_service(db=db, group_service=group_service)


@router.get("/", response_model=List[schema_group_services.GroupServices])
async def read_group_services(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_group_services.get_all_group_services(db, skip=skip, limit=limit)


@router.delete("/{group_id}/{service_id}", response_model=schema_group_services.GroupServices)
async def delete_group_service(group_id: int, service_id: int, db: Session = Depends(get_db)):
    deleted_group_service = crud_group_services.delete_group_service(db, group_id, service_id)
    if deleted_group_service is None:
        raise HTTPException(status_code=404, detail="Group service not found")
    return deleted_group_service