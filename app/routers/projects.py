from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, session, engine
from app.schemas import schema_projects
from app.crud import crud_projects

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_projects.Projects)
async def create_project(project: schema_projects.ProjectsCreate, db: Session = Depends(get_db)):
    return crud_projects.create_project(db=db, project=project)


@router.get("/{project_id}", response_model=schema_projects.Projects)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud_projects.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get("/", response_model=List[schema_projects.Projects])
async def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    projects = crud_projects.get_all_projects(db, skip=skip, limit=limit)
    return projects


@router.put("/{project_id}", response_model=schema_projects.Projects)
async def update_project(project_id: int, project: schema_projects.ProjectsCreate, db: Session = Depends(get_db)):
    db_project = crud_projects.update_project(db, project_id=project_id, project=project)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.delete("/{project_id}", response_model=schema_projects.Projects)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud_projects.delete_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project