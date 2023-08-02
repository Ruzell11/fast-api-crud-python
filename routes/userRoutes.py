from fastapi import APIRouter, Depends, HTTPException , FastAPI
from model.userModel import UserCreateSchema , UserBaseSchema , UserSchemaLogin
from sqlalchemy.orm import Session
from database.session import get_db
from controller.userController import createUser, getSingleUserDetails, getUserByEmail , updateUserDetails , deleteUser , getAllUser , loginUser
from constants.index import HTTP_CODE_BAD_REQUEST


router = APIRouter()


@router.post("/register")
async def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    is_email_exist = await getUserByEmail(db=db, email=user.email)

    if is_email_exist:
        raise HTTPException(
            status_code=HTTP_CODE_BAD_REQUEST, detail="Email already registered"
        )
        
    return await createUser(db=db, user=user)


@router.post('/login-user')
async def login_user(user:UserSchemaLogin , db:Session = Depends(get_db)):
    return await loginUser(db=db , user=user)


@router.get("/user")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return await getSingleUserDetails(db=db, user_id=user_id)

@router.get("/all-users")
async def get_all_user(db:Session = Depends(get_db)):
    return await getAllUser(db=db)


@router.patch("/update-user")
async def update_user(user:UserBaseSchema , db:Session = Depends(get_db)):
    return await updateUserDetails(db=db , user=user)


@router.delete("/delete-user")
async def delete_user(user_id: int , db:Session = Depends(get_db)):
    return await deleteUser(db=db , user_id=user_id)

