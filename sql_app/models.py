from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    title = Column(String)
    body = Column(String)
    url = Column(URLType)
    is_active = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post_related")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    email = Column(EmailType)
    name = Column(String)
    body = Column(String)
    is_active = Column(Boolean, default=True)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post_related = relationship("Post", back_populates="comments")