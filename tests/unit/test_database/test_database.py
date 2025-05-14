import pytest

import common.database.crud as crud
import common.database.models as models

ACCOUNT_PARAMS = [
    {"email": "test1@example.com", "password": "pass1"},
    {"email": "test2@example.com", "password": 2},
]


@pytest.fixture(
    params=[
        {"email": "test1@example.com", "password": "pass1"},
        {"email": "test2@example.com", "password": 1},
    ]
)
def account_data(request):
    return request.param


def test_create_account(mock_session, account_data):
    crud.create_account(email=account_data["email"], password=account_data["password"])
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()


def test_get_account(mock_session, account_data):
    mock_account = models.Account(email=account_data["email"], password=account_data["password"])
    mock_session.scalar.return_value = mock_account

    result = crud.get_account(email=account_data["email"])

    assert result == mock_account
    mock_session.scalar.assert_called_once()


@pytest.mark.parametrize(
    "new_password",
    [
        ("321"),
    ],
)
def test_edit_account(mock_session, account_data, new_password):
    mock_account = models.Account(email=account_data["email"], password=account_data["password"])
    mock_session.scalar.return_value = mock_account

    edited_account = crud.edit_account(email=account_data["email"], new_password=new_password)

    assert edited_account.password == new_password
    mock_session.scalar.assert_called_once()


def test_delete_account(mock_session):
    mock_account = models.Account(email="test@example.com", password="secret")
    mock_session.scalar.return_value = mock_account

    crud.delete_account("test@example.com")

    mock_session.scalar.assert_called_once()
    mock_session.delete.assert_called_once_with(mock_account)
    mock_session.commit.assert_called_once()


def test_get_all_accounts(mock_session):
    mock_account1 = models.Account(email="user1@example.com", password="pass1")
    mock_account2 = models.Account(email="user2@example.com", password="pass2")

    mock_session.scalars.return_value.all.return_value = [mock_account1, mock_account2]

    result = crud.get_all_accounts()

    assert result == [mock_account1, mock_account2]
    mock_session.scalars.assert_called_once()
