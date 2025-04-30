from app.schemas.task import TaskCreate, TaskRead
from uuid import uuid4

def create_task(data: TaskCreate) -> TaskRead:
    task_id = str(uuid4())
    print(f"Publishing to SQS: {{'id': task_id, **data.dict()}}")
    return TaskRead(id=task_id, **data.dict())
def get_task(task_id: str) -> TaskRead:
    # Simula consulta ao banco de dados
    return TaskRead(id=task_id, title="Sample Task", description="This is a sample task.")