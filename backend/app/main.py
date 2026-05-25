from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def index():
    return {"status": "backend is running!"}


@app.get("/lessons")
def get_lessons(limit: int = 10):
    return {"lessons_limit": limit}


@app.get("/lessons/{lesson_id}")
def get_lesson_by_id(lesson_id: int):
    return {"number": lesson_id}


