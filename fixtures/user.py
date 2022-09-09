import uuid
from datetime import datetime
from typing import List

import pytest

from app import utils as app_utils
from app.schemas.user import (
    UserCreateModel,
    UserModel,
    UserSkill,
    UserUpdateModel,
)


def build_user_skill(name: str, years: int) -> UserSkill:
    params = {f"{name}": years}

    return UserSkill.parse_obj(params)


def build_user_skills() -> List[UserSkill]:
    return [
        build_user_skill("SQL", 3),
        build_user_skill("Python", 4),
    ]


@pytest.fixture
def user_skills() -> List[UserSkill]:
    return build_user_skills()


def build_user_create_model(**kwargs) -> UserCreateModel:
    params = dict(
        first_name="Jose A",
        last_name="Morales L",
        email="jose@email.com",
        years_of_experience=4,
        skills=build_user_skills(),
    )

    params.update(kwargs)
    return UserCreateModel.parse_obj(params)


@pytest.fixture
def user_create_model() -> UserCreateModel:
    return build_user_create_model()


def build_user_model(**kwargs) -> UserModel:
    params = dict(
        id=uuid.uuid4(),
        first_name="Jose A",
        last_name="Morales L",
        email="jose@email.com",
        years_of_experience=4,
        skills=build_user_skills(),
        skills_dict=app_utils.get_skills_dict(build_user_skills()),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    params.update(kwargs)
    return UserModel.parse_obj(params)


@pytest.fixture
def user_model() -> UserModel:
    return build_user_model()


def build_user_update_model(**kwargs) -> UserUpdateModel:
    params = dict(
        years_of_experience=4,
    )

    params.update(kwargs)
    return UserUpdateModel.parse_obj(params)


@pytest.fixture
def user_update_model() -> UserUpdateModel:
    return build_user_update_model()
