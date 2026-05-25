from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    pages: int 

class BookResponse(BaseModel):
    id: int
    title: str
    pages: int


@app.get("/")
def index():
    return {"status": "backend is running!"}


@app.get("/lessons")
def get_lessons(limit: int = 10):
    return {"lessons_limit": limit}


@app.get("/lessons/{lesson_id}")
def get_lesson_by_id(lesson_id: int):
    return {"number": lesson_id}


@app.post("/books", response_model=BookResponse)
def create_book(request: BookCreate):
    return {
        "id": 1,
        "title": request.title,
        "pages": request.pages,
    }
