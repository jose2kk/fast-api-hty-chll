from typing import (
    List,
    Optional,
)

from app.database.operations import (
    user as user_db,
    vacancy as vacancy_db,
)
from app.database.operations.exceptions import DatabaseNotFoundException
from app.logger import logger
from app.schemas.user import (
    UserCreateModel,
    UserId,
    UserModel,
    UserUpdateModel,
)
from app.schemas.vacancy import VacancyModel


def get_user_by_user_id(user_id: UserId) -> Optional[UserModel]:
    try:
        return user_db.get_user_by_id(user_id=user_id)
    except DatabaseNotFoundException:
        logger.debug(f"User not found by id={user_id}")
        return None


def create_user(user_create: UserCreateModel) -> Optional[UserModel]:
    user_already_exists = user_db.get_user_by_email(email=user_create.email)
    if user_already_exists:
        logger.debug(f"Email={user_create.email} already exists.")
        return None

    user_created = user_db.create_user(user_create=user_create)
    return user_created


def update_user(user_id: UserId, user_update: UserUpdateModel) -> Optional[UserModel]:
    try:
        user_updated = user_db.update_user(user_id=user_id, user_update=user_update)
        return user_updated
    except DatabaseNotFoundException:
        logger.debug(f"User not found by id={user_id}")
        return None


def delete_user_by_user_id(user_id: UserId) -> Optional[UserModel]:
    try:
        user_deleted = user_db.delete_user_by_id(user_id=user_id)
        return user_deleted
    except DatabaseNotFoundException:
        logger.debug(f"User not found by id={user_id}")
        return None


def get_user_vacancies_by_user_id(user_id: UserId) -> List[VacancyModel]:
    # TODO: Improve performance - reduce complexity -
    user = user_db.get_user_by_id(user_id=user_id)
    vacancies = vacancy_db.get_all_vacancies()  # this isn't ideal, but for time purposes the best I can do rn

    user_skills = user.skills_dict

    user_vacancies: List[VacancyModel] = []
    for vacancy in vacancies:
        vacancy_skills = vacancy.required_skills_dict
        total_required_skills = len(vacancy_skills.keys())

        if total_required_skills % 2 == 0:
            minimum_required_skills = total_required_skills // 2
        else:
            minimum_required_skills = (total_required_skills // 2) + 1

        count_of_valid_skills = 0
        for user_skills_name, user_skills_years in user_skills.items():
            try:
                # has a required skill?
                vacancy_skills_required_years = vacancy_skills[user_skills_name]
                # does he has enough experience years to count the skill?
                if user_skills_years >= vacancy_skills_required_years:
                    count_of_valid_skills += 1
            except KeyError:
                # user has no required skill
                continue

        if count_of_valid_skills >= minimum_required_skills:
            user_vacancies.append(vacancy)

    return user_vacancies
