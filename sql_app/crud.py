from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session


from . import models, schemas

SECRET_KEY = "9644d8eeaaee3be87ea2cbe2a099845129ead566c6f5555a74ecda2ce9c599e1"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_post(db: Session, title: str, body: str, user_id: int, image_url: str):
    db_post = models.Post(title=title, body=body, url=image_url, owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def post_for_user(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.owner_id == user_id).all()


def get_post(db: Session, post_id: int):
    post = db.query(models.Post).filter(models.Post.id==post_id).first()
    comment = db.query(models.Comment).filter(models.Comment.post_id == post_id)
    active_comment = comment.filter(models.Comment.is_active == True).all()
    return {"post": post, "comments": active_comment}


def list_post(db: Session):
    return db.query(models.Post).all()

def create_comment(db: Session, post_id: str, comment: schemas.CommentBase):
    db_comment = models.Comment(**comment.dict(), post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment