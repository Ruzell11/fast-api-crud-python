from database.db import Base
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from model.taskModel import Task


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , index=True)
    email = Column(String , unique=True , index=True)
    password = Column(String)

    """ Note RelationShip"""
    tasks = relationship("Task" , back_populates="user") 


class UserBaseSchema(BaseModel):
    email:str

class UserCreateSchema(UserBaseSchema):
    password:str

class UserSchema(UserBaseSchema):
    id:int
    tasks: list[Task] = []

    class Config:
        orm_mode = True
    

