from database.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        print("Database is running")
        yield db
    finally:
        db.close()
        print("Database is error")

