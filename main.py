from fastapi import FastAPI 
from app.routes import notes_router

app = FastAPI()
router = app.router

@router.get("/")
def index():
    return {"message": "hello"} 

app.router.add_api_route('/notes', notes_router)
