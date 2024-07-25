from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, engine, session
from app.crud import crud_courses
from app.schemas import schema_courses

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=schema_courses.Courses)
async def create_course(course: schema_courses.CoursesCreate, db: Session = Depends(get_db)):
    return crud_courses.create_course(db=db, course=course)


@router.get("/{course_id}", response_model=schema_courses.Courses)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud_courses.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.get("/", response_model=List[schema_courses.Courses])
async def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = crud_courses.get_all_courses(db, skip=skip, limit=limit)
    return courses


@router.put("/{course_id}", response_model=schema_courses.Courses)
async def update_course(course_id: int, course: schema_courses.CoursesCreate, db: Session = Depends(get_db)):
    db_course = crud_courses.update_course(db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.delete("/{course_id}", response_model=schema_courses.Courses)
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud_courses.delete_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course