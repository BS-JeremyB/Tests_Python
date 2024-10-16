from unittest.mock import patch
from notification import envoi_notification

@patch('notification.print')
def test_envoi_notification(mock_print):
    envoi_notification('johndo@mail.com', 'Hello')
    mock_print.assert_called_with('Notification envoyée a johndoe@mail.com : Hello')