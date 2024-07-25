from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, session, engine
from app.schemas import services
from app.crud import crud_services

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=services.Services)
async def create_service(service: services.ServicesCreate, db: Session = Depends(get_db)):
    return crud_services.create_service(db=db, service=service)


@router.get("/{service_id}", response_model=services.Services)
async def read_service(service_id: int, db: Session = Depends(get_db)):
    db_service = crud_services.get_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service


@router.get("/", response_model=List[services.Services])
async def read_services(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    services = crud_services.get_all_services(db, skip=skip, limit=limit)
    return services


@router.put("/{service_id}", response_model=services.Services)
async def update_service(service_id: int, service: services.ServicesCreate, db: Session = Depends(get_db)):
    db_service = crud_services.update_service(db, service_id=service_id, service=service)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service


@router.delete("/{service_id}", response_model=services.Services)
async def delete_service(service_id: int, db: Session = Depends(get_db)):
    db_service = crud_services.delete_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service