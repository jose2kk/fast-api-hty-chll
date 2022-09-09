import uuid
from datetime import datetime
from typing import List

import pytest

from app import utils as app_utils
from app.schemas.vacancy import (
    CurrencyEnum,
    VacancyCreateModel,
    VacancyModel,
    VacancySkill,
    VacancyUpdateModel,
)


def build_vacancy_skill(name: str, years: int) -> VacancySkill:
    params = {f"{name}": years}

    return VacancySkill.parse_obj(params)


def build_vacancy_skills() -> List[VacancySkill]:
    return [
        build_vacancy_skill("SQL", 2),
        build_vacancy_skill("Python", 5),
    ]


@pytest.fixture
def vacancy_skills() -> List[VacancySkill]:
    return build_vacancy_skills()


def build_vacancy_create_model(**kwargs) -> VacancyCreateModel:
    params = dict(
        name="Python Dev",
        company_id=uuid.uuid4(),
        salary=99999,
        currency=CurrencyEnum.COP,
        vacancy_link="https://www.vacancy.com/pythondev",
        required_skills=build_vacancy_skills(),
    )

    params.update(kwargs)
    return VacancyCreateModel.parse_obj(params)


@pytest.fixture
def vacancy_create_model() -> VacancyCreateModel:
    return build_vacancy_create_model()


def build_vacancy_model(**kwargs) -> VacancyModel:
    params = dict(
        id=uuid.uuid4(),
        company_id=uuid.uuid4(),
        name="Python Dev",
        salary=99999,
        currency=CurrencyEnum.COP,
        vacancy_link="https://www.vacancy.com/pythondev",
        required_skills=build_vacancy_skills(),
        required_skills_dict=app_utils.get_skills_dict(build_vacancy_skills()),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    params.update(kwargs)
    return VacancyModel.parse_obj(params)


@pytest.fixture
def vacancy_model() -> VacancyModel:
    return build_vacancy_model()


def build_vacancy_update_model(**kwargs) -> VacancyUpdateModel:
    params = dict(
        salary=88888,
    )

    params.update(kwargs)
    return VacancyUpdateModel.parse_obj(params)


@pytest.fixture
def vacancy_update_model() -> VacancyUpdateModel:
    return build_vacancy_update_model()
