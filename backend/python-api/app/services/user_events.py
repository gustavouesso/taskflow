from app.schemas.user import UserCreate, UserRead, UserUpdate
from uuid import uuid4
from app.models.user import UserInDB
from app.db import get_db
from sqlalchemy.orm import Session

def create_user(data: UserCreate) -> UserRead:
    db: Session = get_db()
    user_id = str(uuid4())
    user = UserInDB(id=user_id, **data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"User created with ID: {user_id}")
    return UserRead(id=user_id, **data.dict())
def get_user(user_id: str) -> UserRead:
    db: Session = get_db()
    user = db.query(UserInDB).filter(UserInDB.id == user_id).first()
    if user:
        return UserRead(id=user.id, **user.dict())
    else:
        print(f"User with ID {user_id} not found.")
        return None
def get_all_users() -> list[UserRead]:
    db: Session = get_db()
    users = db.query(UserInDB).all()
    return [UserRead(id=user.id, **user.dict()) for user in users]
def update_user(user_id: str, data: UserUpdate) -> UserRead:
    db: Session = get_db()
    user = db.query(UserInDB).filter(UserInDB.id == user_id).first()
    if user:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        print(f"User with ID {user_id} updated.")
        return UserRead(id=user.id, **user.dict())
    else:
        print(f"User with ID {user_id} not found.")
        return None