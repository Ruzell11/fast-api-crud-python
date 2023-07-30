from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

USER_NAME = "root"
PASSWORD = ""
SERVER_NAME = "localhost"
DB_NAME = "fast-api-crud-python"

DATABASE_URL = f"mysql://{USER_NAME}:{PASSWORD}@{SERVER_NAME}/{DB_NAME}"


database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)
Base = declarative_base()



