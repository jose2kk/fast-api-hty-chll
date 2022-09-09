from datetime import datetime
from typing import (
    List,
    Optional,
)

from pydantic import parse_obj_as

from app import utils as app_utils
from app.database import (
    session,
)
from app.database.models.vacancy import Vacancy
from app.database.operations.exceptions import DatabaseNotFoundException
from app.logger import logger
from app.schemas.vacancy import (
    VacancyCreateModel,
    VacancyId,
    VacancyModel,
    VacancyUpdateModel,
)


def create_vacancy(vacancy_create: VacancyCreateModel) -> VacancyModel:
    vacancy = Vacancy(
        **vacancy_create.dict(exclude_unset=True),
        created_at=datetime.utcnow(),
        required_skills_dict=app_utils.get_skills_dict(skills=vacancy_create.required_skills),
    )
    session.add(vacancy)
    session.commit()
    return VacancyModel.from_orm(vacancy)


def _get_vacancy_by_id(vacancy_id: VacancyId) -> Vacancy:
    vacancy_from_db = session.query(Vacancy).get(vacancy_id)

    if not vacancy_from_db:
        raise DatabaseNotFoundException(f'{VacancyModel.__name__} with id={vacancy_id} not found')

    return vacancy_from_db


def get_vacancy_by_id(vacancy_id: VacancyId) -> VacancyModel:
    return VacancyModel.from_orm(_get_vacancy_by_id(vacancy_id=vacancy_id))


def update_vacancy(vacancy_id: VacancyId, vacancy_update: VacancyUpdateModel) -> VacancyModel:
    vacancy = _get_vacancy_by_id(vacancy_id=vacancy_id)

    for key, value in vacancy_update.dict(exclude_unset=True).items():
        setattr(vacancy, key, value)

    session.add(vacancy)
    session.commit()

    return VacancyModel.from_orm(vacancy)


def delete_vacancy_by_id(vacancy_id: VacancyId) -> Optional[VacancyModel]:
    vacancy = _get_vacancy_by_id(vacancy_id=vacancy_id)

    if vacancy.deleted_at:
        logger.debug(f"Vacancy={vacancy.id} deleted already.")
        return 

    vacancy.deleted_at = datetime.utcnow()
    session.add(vacancy)
    session.commit()

    return VacancyModel.from_orm(vacancy)


def get_all_vacancies() -> List[VacancyModel]:
    return parse_obj_as(
        List[VacancyModel],
        session.query(Vacancy).all(),
    )
