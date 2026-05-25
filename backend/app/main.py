from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def index():
    return {"status": "backend is running!"}

@app.get("/lessons/{lesson_id}")
def get_lesson_by_id(lesson_id: int):
        
    return {"number": lesson_id}
