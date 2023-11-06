from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql://root:root@localhost:3306/mini'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        