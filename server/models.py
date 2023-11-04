from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    fullname : str = Field(...) #Field(...) tell the field is required
    email: EmailStr = Field(...) # pip install pydantic[email]
    course_of_study : str = Field(...)
    year: int = Field(...,gt=0,le=4)
    gpa: float = Field(...,le=4.0)

    class config:
        schema_extra = {
            "example":{
                "fullname":"John Doe",
                "email":"hello@gmail.com",
                "course_of_study":"B.tech in IT",
                "year":2,
                "gpa":"3.0"
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }

def ResponseModel(data, message):
    return {
        "data":[data],
        "code": 200,
        "message":message,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error":error,
        "code": code,
        "message":message,
        }