from fastapi import APIRouter , Depends
from model.userModel import  UserCreateSchema
from sqlalchemy.orm import Session
from database.db import SessionLocal
from controller.userController import createUser


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        print("Database is running")
        yield db
    finally:
        db.close()
        print("Database is error")


@router.post('/register' )
async def register_user(user:UserCreateSchema , db:Session = Depends(get_db)):
    return await createUser(db=db , user=user)