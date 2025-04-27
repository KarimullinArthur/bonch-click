import database.crud as crud
import database.models as models


def test_create_account(mock_session):
    crud.create_account(email="a@b.c", password="123")
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()


def test_get_account(mock_session):
    mock_account = models.Account(email="test@example.com", password="secret")
    mock_session.scalar.return_value = mock_account

    result = crud.get_account(email="test@example.com")

    assert result == mock_account
    mock_session.scalar.assert_called_once()


def test_get_all_accounts(mock_session):
    mock_account1 = models.Account(email="user1@example.com", password="pass1")
    mock_account2 = models.Account(email="user2@example.com", password="pass2")

    mock_session.scalars.return_value.all.return_value = [mock_account1, mock_account2]

    result = crud.get_all_accounts()

    assert result == [mock_account1, mock_account2]
    mock_session.scalars.assert_called_once()
