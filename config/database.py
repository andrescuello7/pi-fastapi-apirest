from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decouple import config

# Connection with database
engine = create_engine(config("DATABASE_URL"))
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create variables db for calling to database
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()