from unittest.mock import patch
from appel_api import recuperation_api

@patch('appel_api.requests.get')
def test_recuperation_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'mail': 'johndoe@mail.com'} 
    assert recuperation_api('https://www.example.com') == {'mail': 'johndoe@mail.com'}

    mock_get.return_value.status_code = 404
    assert recuperation_api('https://www.example.com') is None