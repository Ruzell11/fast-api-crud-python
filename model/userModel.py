from database.db import Base
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , index=True)
    email = Column(String , unique=True , index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    """ Note RelationShip"""
    tasks = relationship("TaskModel", back_populates="user") 


class UserBaseSchema(BaseModel):
    email:str
    first_name:str
    last_name:str
    
    class Config:
        from_attributes = True
 
    

class UserCreateSchema(UserBaseSchema):
    password:str



class UserSchema(UserBaseSchema):
    id:int
    email:str
    first_name:str
    last_name:str
    tasks: list = []

    class Config:
        from_attributes = True
    

class UserSchemaLogin(BaseModel):
    email:str
    password:str
    
 