from datetime import datetime
from typing import Optional
from app import utils as app_utils

from app.database import (
    session,
)
from app.database.models.user import User
from app.database.operations.exceptions import DatabaseNotFoundException
from app.logger import logger
from app.schemas.user import (
    UserCreateModel,
    UserId,
    UserModel,
    UserUpdateModel,
)


def create_user(user_create: UserCreateModel) -> UserModel:
    user = User(
        **user_create.dict(exclude_unset=True),
        created_at=datetime.utcnow(),
        skills_dict=app_utils.get_skills_dict(user_create.skills),
    )
    session.add(user)
    session.commit()

    return UserModel.from_orm(user)


def get_user_by_email(email: str) -> Optional[UserModel]:
    user_from_db = session.query(User).filter(User.email == email).first()

    if not user_from_db:
        return None

    return UserModel.from_orm(user_from_db)


def _get_user_by_id(user_id: UserId) -> User:
    user_from_db = session.query(User).filter(User.id == str(user_id)).first()

    if not user_from_db:
        raise DatabaseNotFoundException(f'{UserModel.__name__} with id={user_id} not found')

    return user_from_db


def get_user_by_id(user_id: UserId) -> UserModel:
    return UserModel.from_orm(_get_user_by_id(user_id=user_id))


def update_user(user_id: UserId, user_update: UserUpdateModel) -> UserModel:
    user = _get_user_by_id(user_id=user_id)

    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)

    session.add(user)
    session.commit()

    return UserModel.from_orm(user)


def delete_user_by_id(user_id: UserId) -> Optional[UserModel]:
    user = _get_user_by_id(user_id=user_id)

    if user.deleted_at:
        logger.debug(f"User={user.id} deleted already.")
        return

    user.deleted_at = datetime.utcnow()
    session.add(user)
    session.commit()

    return UserModel.from_orm(user)
