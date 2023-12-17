import pytest

base_url = 'https://reqres.in/api/'


@pytest.fixture(scope="function")
def browser_open():
    return base_url
