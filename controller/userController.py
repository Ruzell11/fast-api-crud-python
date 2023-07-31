from sqlalchemy.orm import Session
from model.userModel import UserModel, UserCreateSchema
from model.taskModel import TaskModel, TaskcreateSchema

async def createUser(db: Session, user: UserCreateSchema):
    db_user = UserModel(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
                "message":"User created successfully",
            }
