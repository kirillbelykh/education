from fastapi import FastAPI
from backend.app.api.notes import router as notes_router
from backend.app.api.auth import router as auth_router


app = FastAPI()


app.include_router(notes_router)
app.include_router(auth_router)


@app.get("/")
def index():
    return {"status": "backend is running!"}

