from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {
        'name': 'John',
        'age' : 27,
        'year' : 'year 12'
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {'Name': 'first data'}  # place '/docs' after the URL for cool documentation

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(None, description='Enter the student ID', gt=0)): # gt means greater than, ge is greater than equals to
    return students[student_id]

# to use more than one parameters in the query, use a *
# example = get_student(*,name : str, number : int)

# @app.get('/get-by-name')
# def get_student(name : Optional[str] = None): # if you want to make it option or 'not required' use ' str = None' other way is using Option[]
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {'Data':'Not Found'}

# Combining query parameters

@app.get('/get-by-name/{student_id}')
def get_student(*, student_id: int, name : Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {'Data': 'Not Found'}

# creating a new entry

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {'Error': 'Student already exists'}

    students[student_id] = student
    return students[student_id]

# updating an entry

@app.put('/update-student/{student_id')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {'Error':'Student does not exist'}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

# Deleting data

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {'Error':'Student does not exist'}

    del students[student_id]
    return {'Message':'Data deleted'}