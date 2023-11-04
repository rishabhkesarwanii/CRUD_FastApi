import motor.motor_asyncio

from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

students_collection = database.get_collection("students")



def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


#Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in students_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student =  await students_collection.insert_one(student_data)
    new_student = await students_collection.find_one({"_id":student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await students_collection.find_one({"_id":ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id:str, data:dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await students_collection.find_one({"_id":ObjectId(id)})
    if student:
        updated_student = await students_collection.update_one(
            {"_id":ObjectId(id)},{"$set":data}
        )
        if update_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student:
        await students_collection.delete_one({"_id": ObjectId(id)})
        return True