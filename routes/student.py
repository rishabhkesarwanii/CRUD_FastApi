from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import(
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)

from server.models import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/",response_description="Student data added into the databae")
async def add_student_data(student:StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student,"Student added Succesfully")


@router.get("/",response_description="Student retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved Succefully")
    return ErrorResponseModel(students,404,"Empty List returned")


@router.get("/{id}", response_description="Student data retrieved")
async def get_student(id:str):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Students data retrieved Succefully")
    return ErrorResponseModel(student, 404, "Student doesn't exist")


@router.put("/{id}", response_description="Student data updated")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} update is successful".format(id),
            "Student updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}",response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id),
            "Student deleted Succesfully"
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "Student with id {0} doesn't exsist".format(id)
    )