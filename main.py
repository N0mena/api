from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.requests import Request

app = FastAPI()

@app.get("/hello")
def read_root():
    return JSONResponse({"message": f"Hello World"}, status_code=200)


class WelcomeRequest(BaseModel):
    name: str

@app.get("/welcome")
def welcome_user(request: Request, name :str ):
    return JSONResponse({"message": f"Welcome {name}"}, status_code=200)


class StudentsRequest(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int


@app.post("/students")
def students(request : StudentsRequest):
    return JSONResponse(
        content={[request]},
        status_code=300)



@app.get("/students")
def students():
    return Response()