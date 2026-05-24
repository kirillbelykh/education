from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

db_url = "postgresql://test_user_1:test_password@localhost:5432/test_db_1"
engine = create_engine(url=db_url)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



