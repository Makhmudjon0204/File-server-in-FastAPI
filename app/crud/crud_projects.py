from sqlalchemy.orm import Session
from app.models.projects import Projects
from app.schemas.schema_projects import ProjectsCreate, ProjectsUpdate

def get_project(db: Session, project_id: int):
    return db.query(Projects).filter(Projects.id == project_id).first()

def get_all_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Projects).offset(skip).limit(limit).all()

def create_project(db: Session, project: ProjectsCreate):
    db_project = Projects(
        title=project.title,
        body=project.body,
        start_date=project.start_date,
        end_date=project.end_date,
        logo=project.logo
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id: int, project: ProjectsUpdate):
    db_project = get_project(db, project_id)
    if db_project:
        for key, value in project.dict().items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = get_project(db, project_id)
    if db_project:
        db.delete(db_project)
        db.commit()
    return db_project