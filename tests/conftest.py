import pytest

base_url = 'https://reqres.in/api/'


@pytest.fixture(scope="function")
def open_url():
    return base_url
