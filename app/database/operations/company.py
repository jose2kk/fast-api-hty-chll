from datetime import datetime
from typing import Optional

from app.database import session
from app.database.models.company import Company
from app.database.operations.exceptions import DatabaseNotFoundException
from app.logger import logger
from app.schemas.company import (
    CompanyCreateModel,
    CompanyId,
    CompanyModel,
    CompanyUpdateModel,
)


def create_company(company_create: CompanyCreateModel) -> CompanyModel:
    company = Company(
        **company_create.dict(exclude_unset=True),
        created_at=datetime.utcnow(),
    )
    session.add(company)
    session.commit()
    return CompanyModel.from_orm(company)


def _get_company_by_id(company_id: CompanyId) -> Company:
    company_from_db = session.query(Company).get(company_id)

    if not company_from_db:
        raise DatabaseNotFoundException(f'{CompanyModel.__name__} with id={company_id} not found')

    return company_from_db


def get_company_by_id(company_id: CompanyId) -> CompanyModel:
    return CompanyModel.from_orm(_get_company_by_id(company_id=company_id))


def update_company(company_id: CompanyId, company_update: CompanyUpdateModel) -> CompanyModel:
    company = _get_company_by_id(company_id=company_id)

    for key, value in company_update.dict(exclude_unset=True).items():
        setattr(company, key, value)

    session.add(company)
    session.commit()

    return CompanyModel.from_orm(company)


def delete_company_by_id(company_id: CompanyId) -> Optional[CompanyModel]:
    company = _get_company_by_id(company_id=company_id)

    if company.deleted_at:
        logger.debug(f"Company={company.id} deleted already.")
        return 

    company.deleted_at = datetime.utcnow()
    session.add(company)
    session.commit()

    return CompanyModel.from_orm(company)
