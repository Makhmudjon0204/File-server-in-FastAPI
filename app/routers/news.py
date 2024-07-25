from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_news
from app.database import get_db, session, engine
from app.schemas.schema_news import News, NewsCreate, NewsCreate

router = APIRouter()

session = session(bind=engine)

@router.post("/", response_model=News)
async def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    return crud_news.create_news(db=db, news=news)


@router.get("/{news_id}", response_model=News)
async def read_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud_news.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news


@router.get("/", response_model=List[News])
async def read_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    news = crud_news.get_all_news(db, skip=skip, limit=limit)
    return news


@router.put("/{news_id}", response_model=News)
async def update_news(news_id: int, news: NewsCreate, db: Session = Depends(get_db)):
    db_news = crud_news.update_news(db, news_id=news_id, news=news)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news


@router.delete("/{news_id}", response_model=News)
async def delete_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud_news.delete_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news