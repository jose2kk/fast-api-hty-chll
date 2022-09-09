import json
from datetime import datetime
from unittest.mock import (
    MagicMock,
    Mock,
)

import pytest
from fastapi.testclient import TestClient

from app.schemas.user import (
    UserModel,
    UserCreateModel,
    UserUpdateModel,
)
from fixtures.client import test_client
from fixtures.user import (
    user_create_model,
    user_model,
    user_update_model,
)


@pytest.fixture
def mock_users_service(mocker) -> Mock:
    return mocker.patch('app.main.users_service', autospec=True, spec_set=True)


def test_get_user_endpoint__user_found(
    test_client: TestClient,
    user_model: UserModel,
    mock_users_service: Mock,
):
    mock_users_service.get_user_by_user_id = MagicMock()
    mock_users_service.get_user_by_user_id.return_value = user_model

    resp = test_client.get(f"/v1/users/{user_model.id}")

    assert resp.json() == {
        "message": json.loads(user_model.json(exclude_unset=True)),
    }
    assert resp.status_code == 200

    mock_users_service.get_user_by_user_id.assert_called_once_with(user_id=user_model.id)


def test_get_user_endpoint__user_not_found(
    test_client: TestClient,
    user_model: UserModel,
    mock_users_service: Mock,
):
    mock_users_service.get_user_by_user_id = MagicMock()
    mock_users_service.get_user_by_user_id.return_value = None

    resp = test_client.get(f"/v1/users/{user_model.id}")

    assert resp.json() == {
        "message": f"user={user_model.id} not found",
    }
    assert resp.status_code == 404

    mock_users_service.get_user_by_user_id.assert_called_once_with(user_id=user_model.id)


def test_create_user_endpoint__successful(
    test_client: TestClient,
    user_create_model: UserCreateModel,
    user_model: UserModel,
    mock_users_service: Mock,
):
    mock_users_service.create_user = MagicMock()
    mock_users_service.create_user.return_value = user_model

    resp = test_client.post(f"/v1/users/", json=user_create_model.dict(exclude_unset=True))

    assert resp.json() == {
        "message": json.loads(user_model.json(exclude_unset=True)),
    }
    assert resp.status_code == 201

    mock_users_service.create_user.assert_called_once_with(user_create=user_create_model)


def test_update_user_endpoint__successful(
    test_client: TestClient,
    user_update_model: UserUpdateModel,
    user_model: UserModel,
    mock_users_service: Mock,
):
    mock_users_service.update_user = MagicMock()
    mock_users_service.update_user.return_value = user_model

    resp = test_client.patch(f"/v1/users/{user_model.id}", json=user_update_model.dict(exclude_unset=True))

    assert resp.json() == {
        "message": json.loads(user_model.json(exclude_unset=True)),
    }
    assert resp.status_code == 200

    mock_users_service.update_user.assert_called_once_with(user_id=user_model.id, user_update=user_update_model)


def test_delete_user_endpoint__successful(
    test_client: TestClient,
    user_update_model: UserUpdateModel,
    user_model: UserModel,
    mock_users_service: Mock,
):
    user_model.deleted_at = datetime.utcnow()

    mock_users_service.delete_user_by_user_id = MagicMock()
    mock_users_service.delete_user_by_user_id.return_value = user_model

    resp = test_client.delete(f"/v1/users/{user_model.id}")

    assert resp.json() == {
        "message": json.loads(user_model.json(exclude_unset=True)),
    }
    assert resp.status_code == 200

    mock_users_service.delete_user_by_user_id.assert_called_once_with(user_id=user_model.id)
