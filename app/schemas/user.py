import uuid
from datetime import datetime
from typing import (
    Dict,
    List,
    NewType,
    Optional,
)

from pydantic import BaseModel

from app.schemas.skill import Skill

UserId = NewType("UserId", uuid.UUID)


class UserSkill(Skill):
    pass


class UserCreateModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    years_of_experience: int
    skills: List[UserSkill]


class UserModel(BaseModel):
    id: UserId
    first_name: str
    last_name: str
    email: str
    years_of_experience: int
    skills: List[UserSkill]
    skills_dict: Dict[str, int]
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserUpdateModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    years_of_experience: Optional[int]
    skills: Optional[List[UserSkill]]
