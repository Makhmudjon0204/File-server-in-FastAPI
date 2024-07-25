from sqlalchemy.orm import Session
from app.models.news import News
from app.schemas.schema_news import NewsCreate, NewsUpdate


def get_news(db: Session, news_id: int):
    return db.query(News).filter(News.id == news_id).first()

def get_all_news(db: Session, skip: int = 0, limit: int = 10):
    return db.query(News).offset(skip).limit(limit).all()

def create_news(db: Session, news: NewsCreate):
    db_news = News(
        title=news.title,
        logo=news.logo,
        full_text=news.full_text,
        created_date=news.created_date,
        updated_date=news.updated_date
    )
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def update_news(db: Session, news_id: int, news: NewsUpdate):
    db_news = get_news(db, news_id)
    if db_news:
        for key, value in news.dict().items():
            setattr(db_news, key, value)
        db.commit()
        db.refresh(db_news)
    return db_news

def delete_news(db: Session, news_id: int):
    db_news = get_news(db, news_id)
    if db_news:
        db.delete(db_news)
        db.commit()
    return db_news