from app.schemas.task import TaskCreate, TaskRead
from uuid import uuid4

# Simula envio para SQS (print)
def create_task(data: TaskCreate) -> TaskRead:
    task_id = str(uuid4())
    print(f"Publishing to SQS: {{'id': task_id, **data.dict()}}")
    return TaskRead(id=task_id, **data.dict())