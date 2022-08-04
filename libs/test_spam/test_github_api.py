from unittest.mock import Mock

from avatar_photo import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'jokeCloud', 'id': 14204394,
        'avatar_url': 'https://avatars.githubusercontent.com/u/14204394?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('jokeCloud')
    assert 'https://avatars.githubusercontent.com/u/14204394?v=4' == url
