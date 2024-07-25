from sqlalchemy.orm import Session
from app.models.blogs import Blogs
from app.schemas.schema_blogs import BlogsCreate, BlogsUpdate

def get_blogs(db: Session, blog_id: int):
    return db.query(Blogs).filter(Blogs.id == blog_id).first()

def get_all_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Blogs).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: BlogsCreate):
    db_blog = Blogs(
        title=blog.title,
        short_info=blog.short_info,
        logo=blog.logo,
        blog_link=blog.blog_link,
        created_date=blog.created_date,
        updated_date=blog.updated_date
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db: Session, blog_id: int, blog: BlogsUpdate):
    db_blog = get_blogs(db, blog_id)
    if db_blog:
        for key, value in blog.dict().items():
            setattr(db_blog, key, value)
        db.commit()
        db.refresh(db_blog)
    return db_blog

def delete_blog(db: Session, blog_id: int):
    db_blog = get_blogs(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog