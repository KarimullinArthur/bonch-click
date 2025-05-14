from contextlib import contextmanager
from unittest.mock import MagicMock

import pytest

from common import database


@pytest.fixture
def mock_session(monkeypatch):
    mock_sess = MagicMock()
    mock_sess.scalar.return_value = None
    mock_sess.add.return_value = None
    mock_sess.commit.return_value = None

    @contextmanager
    def fake_session_local():
        yield mock_sess

    monkeypatch.setattr(database.crud, "SessionMaker", fake_session_local)
    return mock_sess
