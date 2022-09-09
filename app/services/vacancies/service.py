from typing import Optional

from app.database.operations import vacancy as vacancy_db
from app.database.operations.exceptions import DatabaseNotFoundException
from app.logger import logger
from app.schemas.vacancy import (
    VacancyCreateModel,
    VacancyId,
    VacancyModel,
    VacancyUpdateModel,
)


def get_vacancy_by_vacancy_id(vacancy_id: VacancyId) -> Optional[VacancyModel]:
    try:
        return vacancy_db.get_vacancy_by_id(vacancy_id=vacancy_id)
    except DatabaseNotFoundException:
        logger.debug(f"Vacancy not found by id={vacancy_id}")
        return None


def create_vacancy(vacancy_create: VacancyCreateModel) -> Optional[VacancyModel]:
    vacancy_created = vacancy_db.create_vacancy(vacancy_create=vacancy_create)
    return vacancy_created


def update_vacancy(vacancy_id: VacancyId, vacancy_update: VacancyUpdateModel) -> Optional[VacancyModel]:
    try:
        vacancy_updated = vacancy_db.update_vacancy(vacancy_id=vacancy_id, vacancy_update=vacancy_update)
        return vacancy_updated
    except DatabaseNotFoundException:
        logger.debug(f"Vacancy not found by id={vacancy_id}")
        return None


def delete_vacancy_by_vacancy_id(vacancy_id: VacancyId) -> Optional[VacancyModel]:
    try:
        vacancy_deleted = vacancy_db.delete_vacancy_by_id(vacancy_id=vacancy_id)
        return vacancy_deleted
    except DatabaseNotFoundException:
        logger.debug(f"Vacancy not found by id={vacancy_id}")
        return None
