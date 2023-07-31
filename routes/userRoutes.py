from fastapi import APIRouter , Depends
from model.userModel import  UserCreateSchema
from sqlalchemy.orm import Session
from database.session import get_db
from controller.userController import createUser\


router = APIRouter()

# Dependency


@router.post('/register' )
async def register_user(user:UserCreateSchema , db:Session = Depends(get_db)):
    return await createUser(db=db , user=user)