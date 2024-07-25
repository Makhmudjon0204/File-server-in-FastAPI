from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_blogs
from app.schemas.schema_blogs import Blogs, BlogsCreate, BlogsUpdate
from app.database import get_db, session, engine

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=Blogs)
async def create_blog(blog: BlogsCreate, db: Session = Depends(get_db)):
    return crud_blogs.create_blog(db=db, blog=blog)


@router.get("/{blog_id}", response_model=Blogs)
async def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud_blogs.get_blogs(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog


@router.get("/", response_model=List[Blogs])
async def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reads_blogs = crud_blogs.get_all_blogs(db, skip=skip, limit=limit)
    return reads_blogs


@router.put("/{blog_id}", response_model=Blogs)
async def update_blog(blog_id: int, blog: BlogsCreate, db: Session = Depends(get_db)):
    db_blog = crud_blogs.update_blog(db, blog_id=blog_id, blog=blog)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog


@router.delete("/{blog_id}", response_model=Blogs)
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud_blogs.delete_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog