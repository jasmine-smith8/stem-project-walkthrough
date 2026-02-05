import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os
from io import StringIO

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rest.router import create_app


class TestCreateApp:
    """Test the create_app function"""

    @patch('rest.router.Flask')
    def test_create_app_flask_initialization(self, mock_flask):
        """Test that Flask app is initialized with correct parameters"""
        # Arrange
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance

        # Act
        with patch('builtins.print'):  # Suppress print output
            result = create_app()

        # Assert
        mock_flask.assert_called_once_with(
            __name__,
            template_folder='../templates',
            static_folder='../static'
        )
        assert result == mock_app_instance

    @patch('rest.router.Flask')
    def test_create_app_url_rules_registration(self, mock_flask):
        """Test that all URL rules are registered correctly"""
        # Arrange
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # Act
        with patch('builtins.print'):
            create_app()

        # Assert - verify all routes are registered
        expected_calls = [
            # (endpoint, view_func, methods)
            ("/", 'rest.router.home_route', ["GET"]),
            ("/generate", 'rest.router.get_route', ["GET"]),
            ("/create", 'rest.router.create_route', ["GET", "POST"]),
            ("/api/vote", 'rest.router.vote_route', ["POST"]),
        ]

        assert mock_app_instance.add_url_rule.call_count == 4

        # Check each call individually
        calls = mock_app_instance.add_url_rule.call_args_list
        assert calls[0].kwargs['rule'] == "/" or calls[0][0][0] == "/"
        assert calls[0].kwargs['methods'] == ["GET"] or calls[0].kwargs.get('methods') == ["GET"]

    @patch('rest.router.Flask')
    @patch('rest.router.home_route')
    def test_create_app_home_route_registration(self, mock_home_route, mock_flask):
        """Test that home route is registered correctly"""
        # Arrange
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # Act
        with patch('builtins.print'):
            create_app()

        # Assert
        mock_app_instance.add_url_rule.assert_any_call(
            "/", view_func=mock_home_route, methods=["GET"]
        )

    @patch('rest.router.Flask')
    @patch('rest.router.get_route')
    def test_create_app_generate_route_registration(self, mock_get_route, mock_flask):
        """Test that generate route is registered correctly"""
        # Arrange
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # Act
        with patch('builtins.print'):
            create_app()

        # Assert
        mock_app_instance.add_url_rule.assert_any_call(
            "/generate", view_func=mock_get_route, methods=["GET"]
        )

    @patch('rest.router.Flask')
    @patch('rest.router.create_route')
    def test_create_app_create_route_registration(self, mock_create_route, mock_flask):
        """Test that create route is registered correctly"""
        # Arrange
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # Act
        with patch('builtins.print'):
            create_app()

        # Assert
        mock_app_instance.add_url_rule.assert_any_call(
            "/create", view_func=mock_create_route, methods=["GET", "POST"]
        )

    @patch('rest.router.Flask')
    @patch('rest.router.vote_route')
    def test_create_app_vote_route_registration(self, mock_vote_route, mock_flask):
        """Test that vote route is registered correctly"""
        # Arrange
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # Act
        with patch('builtins.print'):
            create_app()

        # Assert
        mock_app_instance.add_url_rule.assert_any_call(
            "/api/vote", view_func=mock_vote_route, methods=["POST"]
        )

if __name__ == '__main__':
    pytest.main([__file__])