from fastapi import APIRouter, Depends
from app.schemas.task import TaskCreate, TaskRead
from app.services.task_events import create_task

router = APIRouter()

@router.post("/", response_model=TaskRead)
def create(task: TaskCreate):
    return create_task(task)