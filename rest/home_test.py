import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
from rest.home import home_route


class TestHomeRoute:
    """Test the home_route function"""

    @pytest.fixture
    def app(self):
        """Create test Flask app"""
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    @pytest.fixture
    def client(self, app):
        """Create test client"""
        with app.test_request_context():
            return app.test_client()

    def test_home_route_success(self, app):
        """Test successful home route call"""
        with app.test_request_context('/'):
            with patch('rest.home.render_template') as mock_render:
                mock_render.return_value = "home template content"

                # ACT
                result = home_route()

                # ASSERT
                assert result == "home template content"
                mock_render.assert_called_once_with("home.html")

    def test_home_route_template_error(self, app):
        """Test handling of template rendering errors"""
        with app.test_request_context('/'):
            with patch('rest.home.render_template') as mock_render:
                mock_render.side_effect = Exception("Template not found")

                # ACT & ASSERT
                with pytest.raises(Exception) as exc_info:
                    home_route()

                assert "Template not found" in str(exc_info.value)
                mock_render.assert_called_once_with("home.html")

if __name__ == '__main__':
    pytest.main([__file__])