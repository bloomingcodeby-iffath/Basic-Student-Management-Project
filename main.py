from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
from models import Base, Student, StudentCreate, StudentResponse


app = FastAPI()
Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Database Connected Successfully"}

@app.post("/students")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(name=student.name, age=student.age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student added!", "id": new_student.id}

@app.get("/students", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students