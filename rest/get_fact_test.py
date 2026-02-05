import pytest
from unittest.mock import Mock, patch
import sys
import os
import json

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
from rest.get_fact import get_route
from fact import Fact


class TestGetFactRoute:
    """Test the get_route function"""

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

    @patch('rest.get_fact.get_fact')
    def test_get_route_html_response(self, mock_get_fact, app):
        """Test GET request returns HTML template by default"""
        # Arrange
        mock_fact = Fact(id=1, fact="Test fact", category="science", likes=5, dislikes=2)
        mock_get_fact.return_value = mock_fact

        with app.test_request_context('/'):
            with patch('rest.get_fact.render_template') as mock_render:
                mock_render.return_value = "generate template"

                # Act
                result = get_route()

                # Assert
                assert result == "generate template"
                mock_get_fact.assert_called_once()
                mock_render.assert_called_once_with(
                    "generate.html",
                    random_fact="Test fact",
                    category="science",
                    random_fact_id=1,
                    random_fact_likes=5,
                    random_fact_dislikes=2
                )

    @patch('rest.get_fact.get_fact')
    def test_get_route_with_null_fact_attributes(self, mock_get_fact, app):
        """Test handling fact with NULL/None attributes"""
        # Arrange
        mock_fact = Fact(id=None, fact="Fact with null attributes", category=None, likes=None, dislikes=None)
        mock_get_fact.return_value = mock_fact

        with app.test_request_context('/?json=1'):
            with patch('rest.get_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "null attributes json"

                # Act
                result = get_route()

                # Assert
                assert result == "null attributes json"
                mock_jsonify.assert_called_once_with({
                    "id": None,
                    "fact": "Fact with null attributes",
                    "category": None,
                    "likes": 0,  # getattr default
                    "dislikes": 0  # getattr default
                })

    @patch('rest.get_fact.get_fact')
    def test_get_route_database_error(self, mock_get_fact, app):
        """Test handling database errors"""
        # Arrange
        mock_get_fact.side_effect = Exception("Database connection failed")

        with app.test_request_context('/'):
            # Act & Assert
            with pytest.raises(Exception) as exc_info:
                get_route()

            assert "Database connection failed" in str(exc_info.value)
            mock_get_fact.assert_called_once()

    @patch('rest.get_fact.get_fact')
    def test_get_route_render_template_error(self, mock_get_fact, app):
        """Test handling template rendering errors"""
        # Arrange
        mock_fact = Fact(id=8, fact="Template error fact", category="error", likes=1, dislikes=1)
        mock_get_fact.return_value = mock_fact

        with app.test_request_context('/'):
            with patch('rest.get_fact.render_template') as mock_render:
                mock_render.side_effect = Exception("Template not found")

                # Act & Assert
                with pytest.raises(Exception) as exc_info:
                    get_route()

                assert "Template not found" in str(exc_info.value)
                mock_get_fact.assert_called_once()

if __name__ == '__main__':
    pytest.main([__file__])