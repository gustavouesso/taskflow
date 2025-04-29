from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskRead(TaskCreate):
    id: str