from database.db import Base
from sqlalchemy import Column, ForeignKey , Integer , String
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    description = Column(String)

    """ Note RelationShip"""
    user_id = Column(Integer , ForeignKey("users.id"))

    user = relationship("UserModel" , back_populates="tasks")


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
