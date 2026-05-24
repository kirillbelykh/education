from pydantic import BaseModel
from datetime import datetime

class NoteRead(BaseModel):
    id: int
    title: str 
    text: str
    created_at: datetime
    created_by: int 