from sqlalchemy.orm import Session
from app.models.courses import Courses
from app.schemas.schema_courses import CoursesCreate, CoursesUpdate

def get_course(db: Session, course_id: int):
    return db.query(Courses).filter(Courses.id == course_id).first()

def get_all_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Courses).offset(skip).limit(limit).all()

def create_course(db: Session, course: CoursesCreate):
    db_course = Courses(
        title=course.title,
        short_description=course.short_description,
        logo=course.logo,
        edu_link=course.edu_link
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: CoursesUpdate):
    db_course = get_course(db, course_id)
    if db_course:
        for key, value in course.dict().items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course