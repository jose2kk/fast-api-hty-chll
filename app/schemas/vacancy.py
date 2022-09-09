import uuid
from datetime import datetime
from enum import Enum
from typing import (
    Dict,
    List,
    NewType,
    Optional,
)

from pydantic import BaseModel

from app.schemas.company import CompanyId
from app.schemas.skill import Skill

VacancyId = NewType("VacancyId", uuid.UUID)
VacancyUrl = NewType("VacancyUrl", str)


class CurrencyEnum(str, Enum):
    COP = "COP"
    USD = "USD"


class VacancySkill(Skill):
    pass


class VacancyCreateModel(BaseModel):
    name: str
    salary: float
    currency: CurrencyEnum
    company_id: CompanyId
    vacancy_link: VacancyUrl
    required_skills: List[VacancySkill]


class VacancyModel(BaseModel):
    id: VacancyId
    name: str
    salary: float
    currency: CurrencyEnum
    company_id: CompanyId
    vacancy_link: VacancyUrl
    required_skills: List[VacancySkill]
    required_skills_dict: Dict[str, int]
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class VacancyUpdateModel(BaseModel):
    name: Optional[str]
    salary: Optional[float]
    currency: Optional[CurrencyEnum]
    vacancy_link: Optional[VacancyUrl]
    required_skills: Optional[List[VacancySkill]]
