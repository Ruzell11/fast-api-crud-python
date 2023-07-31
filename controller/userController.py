from sqlalchemy.orm import Session
from model.userModel import UserModel, UserCreateSchema, UserSchema , UserBaseSchema
from model.taskModel import TaskModel, TaskcreateSchema
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from constants.index import HTTP_CODE_OK, HTTP_CODE_BAD_REQUEST, HTTP_CODE_NOT_FOUND


async def getUserByEmail(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


async def getAllUser(db:Session):
    return db.query(UserModel).all()

async def createUser(db: Session, user: UserCreateSchema):
    db_user = UserModel(email=user.email, password=user.password , first_name=user.first_name , last_name=user.last_name)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "message": "User created successfully",
        "success" : True,
        "user":db_user
    }
    

async def getSingleUserDetails(db: Session, user_id: int):
    user_details = db.query(UserModel).filter(UserModel.id == user_id).first()

    if user_details is None:
        raise HTTPException(status_code=HTTP_CODE_NOT_FOUND, detail="User not found")

    user_details_json = jsonable_encoder(user_details)
    
    return {
        "message": "User details",
        "user": UserSchema(**user_details_json).model_dump(),
        "success" : True
    }
    
    
async def updateUserDetails(db: Session, user: UserBaseSchema):
    user_details = db.query(UserModel).filter(UserModel.email == user.email).first()

    if user_details is None:
        raise HTTPException(status_code=HTTP_CODE_NOT_FOUND, detail="User not found")

    # Update the user_details with the data from user
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(user_details, key, value)

    # Commit the changes to the database
    db.commit()

    # Return the updated user details
    return {
        "message": "User details updated successfully",
        "user": UserSchema.from_orm(user_details).model_dump(),
        "success": True,
    }

      
async def deleteUser(db: Session , user_id):
    user_details = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user_details is None:
        raise HTTPException(status_code=HTTP_CODE_NOT_FOUND, detail="User not found")
    
    db.delete(user_details)
    db.commit()
    
    return {
        "message" : "User deleted successfully",
        "success" : True
    }


 