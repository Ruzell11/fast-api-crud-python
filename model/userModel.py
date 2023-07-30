from database.db import Database
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import relationship

Base = Database.Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True , index=True)
    email = Column(String , unique=True , index=True)
    hashed_password = Column(String)

    """ Note RelationShip"""
    tasks = relationship("Task" , back_populate="user") 

