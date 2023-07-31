from database.db import Base
from sqlalchemy import Column, ForeignKey , Integer , String
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="tasks")


class TaskBaseSchema(BaseModel):
    title: str
    description: str


class TaskcreateSchema(TaskBaseSchema):
    pass


class TaskSchema(TaskBaseSchema):
    id: int
    user_id: int

    class Config:
        orm_mode = True
