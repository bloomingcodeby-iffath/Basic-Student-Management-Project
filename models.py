from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)

class StudentCreate(BaseModel):
    name: str
    age: int

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True