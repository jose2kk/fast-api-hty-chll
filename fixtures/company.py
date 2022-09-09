import uuid
from datetime import datetime

import pytest

from app.schemas.company import (
    CompanyCreateModel,
    CompanyModel,
    CompanyUpdateModel,
)


def build_company_create_model(**kwargs) -> CompanyCreateModel:
    params = dict(
        name="2kk LLC",
    )

    params.update(kwargs)
    return CompanyCreateModel.parse_obj(params)


@pytest.fixture
def company_create_model() -> CompanyCreateModel:
    return build_company_create_model()


def build_company_model(**kwargs) -> CompanyModel:
    params = dict(
        id=uuid.uuid4(),
        name="2kk LLC",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    params.update(kwargs)
    return CompanyModel.parse_obj(params)


@pytest.fixture
def company_model() -> CompanyModel:
    return build_company_model()


def build_company_update_model(**kwargs) -> CompanyUpdateModel:
    params = dict(
        name="2kk LLC",
    )

    params.update(kwargs)
    return CompanyUpdateModel.parse_obj(params)


@pytest.fixture
def company_update_model() -> CompanyUpdateModel:
    return build_company_update_model()
