from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user_events import create_user, get_user, update_user

router = APIRouter()

@router.post("/", response_model=UserRead)
def create(user: UserCreate):
    return create_user(user)
@router.get("/{user_id}", response_model=UserRead)
def read(user_id: str):
    return get_user(user_id)
@router.get("/", response_model=list[UserRead])
def read_all():
    return get_all_users()
@router.put("/{user_id}", response_model=UserRead)
def update(user_id: str, user: UserUpdate):
    return update_user(user_id, user)