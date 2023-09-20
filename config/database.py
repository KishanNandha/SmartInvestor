from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from constants.CONST import DATABASE_URL

# Create the SQLAlchemy engine


engine = create_engine(
    DATABASE_URL,echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def init_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()