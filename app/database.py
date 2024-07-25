from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:1111@localhost/TQQT_project_db',
                       echo=True)

Base = declarative_base()
session = sessionmaker()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()