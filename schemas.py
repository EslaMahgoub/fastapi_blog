"""Pydantic schemas for request/response validation and serialization."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """Base fields shared by user-related schemas (username, email)."""

    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)


class UserCreate(UserBase):
    """Schema for creating a new user (same as UserBase)."""

    password: str = Field(min_length=8)


class UserPublic(BaseModel):
    """Schema for user in API Public responses; includes id, username, image_file, image_path."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    image_file: str | None
    image_path: str


class UserPrivate(UserPublic):
    """Schema for user in API Private responses;
    includes id, username, image_file, image_path, email."""

    email: EmailStr


class UserUpdate(BaseModel):
    """Schema for partial user update; all fields optional."""

    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=120)
    image_file: str | None = Field(default=None, min_length=1, max_length=200)


class Token(BaseModel):
    access_token: str
    token_type: str


class PostBase(BaseModel):
    """Base fields for post schemas (title, content)."""

    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)


class PostCreate(PostBase):
    """Schema for creating a new post; includes user_id."""

    pass


class PostUpdate(BaseModel):
    """Schema for partial post update; title and content optional."""

    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None = Field(default=None, min_length=1)


class PostResponse(PostBase):
    """Schema for post in API responses; includes id, user_id, date_posted, author."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserPublic
