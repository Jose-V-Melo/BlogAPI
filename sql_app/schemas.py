from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    email: str
    password: str


class PostBase(BaseModel):
    title: str
    body: str


class PostList(PostBase):
    created_date: datetime | None
    owner_id: int
    owner: User

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    name: str
    body: str
    email: str


class CommentList(CommentBase):
    id: int
    post_id: int
    created_date: datetime | None = None

    class Config:
        orm_mode = True