from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    email: str
    full_name: str
    disabled: bool = None

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    disabled: bool = None

class UserRead(BaseModel):
    id: str
    username: str
    email: str
    full_name: str
    disabled: bool = None

class UserUpdate(BaseModel):
    username: str = None
    email: str = None
    full_name: str = None
    password: str = None
    disabled: bool = None

class UserInDB(User):
    hashed_password: str