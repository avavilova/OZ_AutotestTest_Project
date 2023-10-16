import pytest

import requests

BASE_URL = 'https://send-request.me/'


class Endpoints:
    POST_AUTHORIZE_ENDPOINT = f'{BASE_URL}api/auth/authorize'
    GET_AUTH_USER_ENDPOINT = f'{BASE_URL}api/auth/me'

class PostBodyValues:
    valid_body: dict = {"login": 'Alice', "password": 'qwerty12345'}
    invalid_password_body: list = [('Alex', ''), ('Maria', 'qwerty1234'), ('Adam', 'qwerty'), ('Tomas', '12345')]
    invalid_login_body: list = [('', 'qwerty12345'), ('a', 'qwerty12345'), ('Li', 'qwerty12345')]

@pytest.fixture(scope='module')
def post_auth_response():
    post_auth_response = requests.post(Endpoints.POST_AUTHORIZE_ENDPOINT, json=PostBodyValues.valid_body)
    return post_auth_response

@pytest.fixture(scope='module')
def auth_token(post_auth_response):
    auth_data = post_auth_response.json()
    return auth_data['token']

@pytest.fixture(scope='module')
def get_user_by_token(auth_token):
    return requests.get(Endpoints.GET_AUTH_USER_ENDPOINT, headers={'x-token': auth_token})

@pytest.fixture()
def post_auth_with_invalid_password(login, inv_password):
    post_invalid_password_body = {"login": login, "password": inv_password}
    post_invalid_password_response = requests.post(Endpoints.POST_AUTHORIZE_ENDPOINT, json=post_invalid_password_body)
    return post_invalid_password_response

@pytest.fixture()
def post_auth_with_invalid_login(inv_login, password):
    post_invalid_login_body = {"login": inv_login, "password": password}
    post_invalid_login_response = requests.post(Endpoints.POST_AUTHORIZE_ENDPOINT, json=post_invalid_login_body)
    return post_invalid_login_response

@pytest.fixture()
def get_user_with_invalid_token(inv_token):
    return requests.get(Endpoints.GET_AUTH_USER_ENDPOINT, headers={'x-token': inv_token})


def test_is_post_status_200(post_auth_response):
    assert post_auth_response.status_code == 200

def test_is_post_body_response_not_empty(post_auth_response):
    assert post_auth_response.json()

def test_is_token_not_empty(post_auth_response):
    assert post_auth_response.json()['token']

def test_get_user_status(get_user_by_token):
    assert get_user_by_token.status_code == 200

def test_user_name(get_user_by_token):
    assert get_user_by_token.json()['user_name'] == PostBodyValues.valid_body['login']

def test_email(get_user_by_token):
    assert get_user_by_token.json()['email_address'] == PostBodyValues.valid_body['login'] + "@example.com"

def test_is_valid_till_not_empty(get_user_by_token):
    assert get_user_by_token.json()['valid_till']

@pytest.mark.parametrize("login, inv_password", PostBodyValues.invalid_password_body)
def test_post_invalid_password_status(post_auth_with_invalid_password):
    assert post_auth_with_invalid_password.status_code == 403

@pytest.mark.parametrize("inv_login, password", PostBodyValues.invalid_login_body)
def test_post_invalid_login_status(post_auth_with_invalid_login):
    assert post_auth_with_invalid_login.status_code == 422

@pytest.mark.parametrize("inv_token", ['123456', 'kyjtiytiuytiyt', ''])
def test_get_user_invalid_token_status(get_user_with_invalid_token):
    assert get_user_with_invalid_token.status_code == 403
    assert get_user_with_invalid_token.json()['detail']['reason'] == 'Token is incorrect. Please login and try again'



