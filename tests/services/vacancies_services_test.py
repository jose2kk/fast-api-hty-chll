from datetime import datetime
from unittest.mock import (
    MagicMock,
    Mock,
)

import pytest

from app.database.operations.exceptions import DatabaseNotFoundException
from app.schemas.vacancy import (
    VacancyModel,
    VacancyCreateModel,
    VacancyUpdateModel,
)
from app.services.vacancies import service as vacancies_service
from fixtures.vacancy import (
    vacancy_create_model,
    vacancy_model,
    vacancy_update_model,
)

@pytest.fixture
def mock_vacancy_db(mocker) -> Mock:
    return mocker.patch('app.services.vacancies.service.vacancy_db', autospec=True, spec_set=True)


def test_get_vacancy_by_vacancy_id__vacancy_found(
    vacancy_model: VacancyModel,
    mock_vacancy_db: Mock,
):
    mock_vacancy_db.get_vacancy_by_id = MagicMock()
    mock_vacancy_db.get_vacancy_by_id.return_value = vacancy_model

    resp = vacancies_service.get_vacancy_by_vacancy_id(vacancy_id=vacancy_model.id)

    assert resp == vacancy_model

    mock_vacancy_db.get_vacancy_by_id.assert_called_once_with(vacancy_id=vacancy_model.id)


def test_get_vacancy_by_vacancy_id__vacancy_not_found(
    vacancy_model: VacancyModel,
    mock_vacancy_db: Mock,
):
    mock_vacancy_db.get_vacancy_by_id = MagicMock()
    mock_vacancy_db.get_vacancy_by_id.side_effect = DatabaseNotFoundException()

    resp = vacancies_service.get_vacancy_by_vacancy_id(vacancy_id=vacancy_model.id)

    assert resp is None

    mock_vacancy_db.get_vacancy_by_id.assert_called_once_with(vacancy_id=vacancy_model.id)


def test_create_vacancy__successful(
    vacancy_create_model: VacancyCreateModel,
    vacancy_model: VacancyModel,
    mock_vacancy_db: Mock,
):
    mock_vacancy_db.create_vacancy = MagicMock()
    mock_vacancy_db.create_vacancy.return_value = vacancy_model

    resp = vacancies_service.create_vacancy(vacancy_create=vacancy_create_model)

    assert resp == vacancy_model

    mock_vacancy_db.create_vacancy.assert_called_once_with(vacancy_create=vacancy_create_model)


def test_update_vacancy__successful(
    vacancy_update_model: VacancyUpdateModel,
    vacancy_model: VacancyModel,
    mock_vacancy_db: Mock,
):
    mock_vacancy_db.update_vacancy = MagicMock()
    mock_vacancy_db.update_vacancy.return_value = vacancy_model

    resp = vacancies_service.update_vacancy(vacancy_id=vacancy_model.id, vacancy_update=vacancy_update_model)

    assert resp == vacancy_model

    mock_vacancy_db.update_vacancy.assert_called_once_with(vacancy_id=vacancy_model.id, vacancy_update=vacancy_update_model)


def test_update_vacancy__vacancy_not_found(
    vacancy_update_model: VacancyUpdateModel,
    vacancy_model: VacancyModel,
    mock_vacancy_db: Mock,
):
    mock_vacancy_db.update_vacancy = MagicMock()
    mock_vacancy_db.update_vacancy.side_effect = DatabaseNotFoundException()

    resp = vacancies_service.update_vacancy(vacancy_id=vacancy_model.id, vacancy_update=vacancy_update_model)

    assert resp is None

    mock_vacancy_db.update_vacancy.assert_called_once_with(vacancy_id=vacancy_model.id, vacancy_update=vacancy_update_model)


def test_delete_vacancy__successful(
    vacancy_model: VacancyModel,
    mock_vacancy_db: Mock,
):
    vacancy_model.deleted_at = datetime.utcnow()

    mock_vacancy_db.delete_vacancy_by_id = MagicMock()
    mock_vacancy_db.delete_vacancy_by_id.return_value = vacancy_model

    resp = vacancies_service.delete_vacancy_by_vacancy_id(vacancy_id=vacancy_model.id)

    assert resp == vacancy_model
    assert resp.deleted_at is not None

    mock_vacancy_db.delete_vacancy_by_id.assert_called_once_with(vacancy_id=vacancy_model.id)

