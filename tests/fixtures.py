import tempfile

import pytest

from app.app import app


@pytest.fixture
def client():
    _, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
