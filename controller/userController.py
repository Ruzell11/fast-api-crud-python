from sqlalchemy.orm import Session
from model.userModel import UserCreateSchema , UserModel

async def createUser(db: Session, user: UserCreateSchema):
    db_user = UserModel(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
                "message":"User created successfully",
                "user" : db_user
        }
