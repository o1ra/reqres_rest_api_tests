import jsonschema
import pytest
import requests
from tests.conftest import open_url
from utils.load_shema import load_schema


def test_get_list_users_unknown_successfully(open_url):
    url = f'{open_url}unknown'
    schema = load_schema("get_list_unknown.json")

    result = requests.get(url)

    jsonschema.validate(result.json(), schema)
    assert result.status_code == 200
    assert result.json()["per_page"] == len(result.json()['data'])


def test_post_register_successful(open_url):
    url = f'{open_url}register'
    schema = load_schema("post_register_successful.json")
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    result = requests.post(url, payload)

    jsonschema.validate(result.json(), schema)
    assert result.status_code == 200


def test_post_register_unsuccessful(open_url):
    url = f'{open_url}register'
    payload = {
        "email": "eve.holt@reqres.in",

    }

    result = requests.post(url, payload)

    assert result.status_code == 400
    assert result.json()["error"] == "Missing password"


def test_post_register_incorrect_mail(open_url):
    url = f'{open_url}register'
    payload = {
        "email": "eve.holt",
        "password": "pistol"
    }

    result = requests.post(url, payload)

    assert result.status_code == 400
    assert result.json()["error"] == "Note: Only defined users succeed registration"


@pytest.mark.parametrize('id_', [3])
def test_put_update_successfull(id_, open_url):
    url = f'{open_url}users/{id_}'
    schema = load_schema("put_update.json")
    payload = {
        "name": "Oleg",
        "job": "QA engineer"
    }

    result = requests.put(url, payload)

    jsonschema.validate(result.json(), schema)
    assert result.status_code == 200
    assert result.json()["name"] == "Oleg"
    assert result.json()["job"] == "QA engineer"


@pytest.mark.parametrize('id_', [3])
def test_user_delete_successfull(id_, open_url):
    url = f'{open_url}users/{id_}'

    result = requests.delete(url)

    assert result.status_code == 204


@pytest.mark.parametrize('id_', [3])
def test_user_delete_successfull(id_, open_url):
    url = f'{open_url}users/{id_}'

    result = requests.delete(url)

    assert result.status_code == 204


def test_post_create(open_url):
    url = f'{open_url}users'
    schema = load_schema("post_create.json")
    payload = {
        "name": "Ivan",
        "job": "leader"
    }

    result = requests.post(url, payload)
    jsonschema.validate(result.json(), schema)
    assert result.status_code == 201


@pytest.mark.parametrize('id_', [13, 23])
def test_unknown_unsuccsessfuly(id_, open_url):
    url = f'{open_url}unknown/{id_}'
    result = requests.get(url)
    assert result.status_code == 404
    assert result.json() == {}
