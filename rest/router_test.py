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

    # Patch the Flask class to mock Flask app creation
    @patch('rest.router.Flask')
    def test_create_app_flask_initialization(self, mock_flask):
        """Test that Flask app is initialized with correct parameters"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        # Fix: Make url_map.iter_rules() return an empty list
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):  # Suppress print output
            result = create_app()

        # ASSERT
        mock_flask.assert_called_once_with(
            'rest.router',  # This should be the module name, not __name__
            template_folder='../templates',
            static_folder='../static'
        )
        assert result == mock_app_instance

    # Patch the Flask class to mock Flask app creation and the route functions to verify route registration
    @patch('rest.router.Flask')
    @patch('rest.router.home_route')
    def test_create_app_home_route_registration(self, mock_home_route, mock_flask):
        """Test that home route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/", view_func=mock_home_route, methods=["GET"]
        )

    # Patch the Flask class to mock Flask app creation and the route functions to verify route registration
    @patch('rest.router.Flask')
    @patch('rest.router.get_route')
    def test_create_app_generate_route_registration(self, mock_get_route, mock_flask):
        """Test that generate route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/generate", view_func=mock_get_route, methods=["GET"]
        )

    # Patch the Flask class to mock Flask app creation and the route functions to verify route registration
    @patch('rest.router.Flask')
    @patch('rest.router.create_route')
    def test_create_app_create_route_registration(self, mock_create_route, mock_flask):
        """Test that create route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/create", view_func=mock_create_route, methods=["GET", "POST"]
        )

    # Patch the Flask class to mock Flask app creation and the route functions to verify route registration
    @patch('rest.router.Flask')
    @patch('rest.router.vote_route')
    def test_create_app_vote_route_registration(self, mock_vote_route, mock_flask):
        """Test that vote route is registered correctly"""
        # ARRANGE
        mock_app_instance = Mock()
        mock_flask.return_value = mock_app_instance
        mock_app_instance.url_map.iter_rules.return_value = []

        # ACT
        with patch('builtins.print'):
            create_app()

        # ASSERT
        mock_app_instance.add_url_rule.assert_any_call(
            "/api/vote", view_func=mock_vote_route, methods=["POST"]
        )

if __name__ == '__main__':
    pytest.main([__file__])