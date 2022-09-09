from typing import Optional

from app.database.operations import company as company_db
from app.database.operations.exceptions import DatabaseNotFoundException
from app.logger import logger
from app.schemas.company import (
    CompanyCreateModel,
    CompanyId,
    CompanyModel,
    CompanyUpdateModel,
)


def get_company_by_company_id(company_id: CompanyId) -> Optional[CompanyModel]:
    try:
        return company_db.get_company_by_id(company_id=company_id)
    except DatabaseNotFoundException:
        logger.debug(f"Company not found by id={company_id}")
        return None


def create_company(company_create: CompanyCreateModel) -> Optional[CompanyModel]:
    company_created = company_db.create_company(company_create=company_create)
    return company_created


def update_company(company_id: CompanyId, company_update: CompanyUpdateModel) -> Optional[CompanyModel]:
    try:
        company_updated = company_db.update_company(company_id=company_id, company_update=company_update)
        return company_updated
    except DatabaseNotFoundException:
        logger.debug(f"Company not found by id={company_id}")
        return None


def delete_company_by_company_id(company_id: CompanyId) -> Optional[CompanyModel]:
    try:
        company_deleted = company_db.delete_company_by_id(company_id=company_id)
        return company_deleted
    except DatabaseNotFoundException:
        logger.debug(f"Company not found by id={company_id}")
        return None
