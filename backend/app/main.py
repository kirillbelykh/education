from fastapi import FastAPI
from backend.app.api.notes import router as notes_router


app = FastAPI()


app.include_router(notes_router)


@app.get("/")
def index():
    return {"status": "backend is running!"}

