import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Enum as SqlEnum,
    Float,
    ForeignKey,
    String,
)
from sqlalchemy.dialects.postgresql import (
    JSONB,
    UUID,
)

from app.database.models.base import Base
from app.schemas.vacancy import CurrencyEnum


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    currency = Column(SqlEnum(CurrencyEnum, name="vacancy_salary_currency"), nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    vacancy_link = Column(String, nullable=False)
    required_skills = Column(JSONB, nullable=False, default=list)
    required_skills_dict = Column(JSONB, nullable=False, default=dict)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)
