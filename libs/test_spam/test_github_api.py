from unittest.mock import Mock

import pytest
from avatar_photo import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/14204394?v=4'
    resp_mock.json.return_value = {
        'login': 'jokeCloud', 'id': 14204394,
        'avatar_url': url,
    }
    get_mock = mocker.patch('avatar_photo.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('jokeCloud')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('jokeCloud')
    assert 'https://avatars.githubusercontent.com/u/14204394?v=4' == url
