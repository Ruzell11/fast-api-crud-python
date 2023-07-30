from database.db import Database
from sqlalchemy import Column, ForeignKey , Integer , String
from sqlalchemy.orm import relationship
from pydantic import BaseModel

Base = Database.Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    description = Column(String)

    """ Note RelationShip"""
    user_id = Column(Integer , ForeignKey("users.id"))

    user = relationship("User" , back_populate="tasks")


class TaskBase(BaseModel):
    title: str
    description: str


class Taskcreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
