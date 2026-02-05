import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
from rest.create_fact import create_route
from fact import Fact


class TestCreateFactRoute:
    """Test the create_route function"""

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

    def test_create_route_get_request(self, app):
        """Test GET request returns create.html template"""
        with app.test_request_context('/', method='GET'):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "create template"

                result = create_route()

                assert result == "create template"
                mock_render.assert_called_once_with("create.html")

    @patch('rest.create_fact.create_fact')
    def test_create_route_post_success(self, mock_create_fact, app):
        """Test successful POST request with valid data"""
        # Arrange
        mock_fact = Fact(id=1, fact="Test fact", category="science", likes=0, dislikes=0)
        mock_create_fact.return_value = mock_fact

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Test fact',
            'category': 'science'
        }):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "success template"

                # Act
                result = create_route()

                # Assert
                assert result == "success template"
                mock_create_fact.assert_called_once_with('Test fact', 'science')
                mock_render.assert_called_once_with(
                    "create.html", 
                    random_fact="Test fact", 
                    category="science"
                )

    @patch('rest.create_fact.create_fact')
    def test_create_route_post_with_empty_category(self, mock_create_fact, app):
        """Test POST request with empty category"""
        # Arrange
        mock_fact = Fact(id=2, fact="Fact without category", category=None, likes=0, dislikes=0)
        mock_create_fact.return_value = mock_fact

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Fact without category',
            'category': ''
        }):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "template with empty category"

                # Act
                result = create_route()

                # Assert
                assert result == "template with empty category"
                mock_create_fact.assert_called_once_with('Fact without category', '')
                mock_render.assert_called_once_with(
                    "create.html", 
                    random_fact="Fact without category", 
                    category=None
                )

    @patch('rest.create_fact.create_fact')
    def test_create_route_post_with_missing_category(self, mock_create_fact, app):
        """Test POST request with missing category field"""
        # Arrange
        mock_fact = Fact(id=3, fact="Fact with no category field", category=None, likes=0, dislikes=0)
        mock_create_fact.return_value = mock_fact

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Fact with no category field'
            # No category field provided
        }):
            with patch('rest.create_fact.render_template') as mock_render:
                mock_render.return_value = "template with None category"

                # Act
                result = create_route()

                # Assert
                assert result == "template with None category"
                mock_create_fact.assert_called_once_with('Fact with no category field', None)
                mock_render.assert_called_once_with(
                    "create.html", 
                    random_fact="Fact with no category field", 
                    category=None
                )

    def test_create_route_post_missing_fact_text(self, app):
        """Test POST request with missing fact_text returns 400 error"""
        with app.test_request_context('/', method='POST', data={
            'category': 'science'
            # No fact_text provided
        }):
            # Act
            result = create_route()

            # Assert
            assert result == ("Fact text is required", 400)

    @patch('rest.create_fact.create_fact')
    def test_create_route_database_error(self, mock_create_fact, app):
        """Test POST request when database function raises an error"""
        # Arrange
        mock_create_fact.side_effect = Exception("Database connection failed")

        with app.test_request_context('/', method='POST', data={
            'fact_text': 'Test fact',
            'category': 'science'
        }):
            # Act & Assert
            with pytest.raises(Exception) as exc_info:
                create_route()

            assert "Database connection failed" in str(exc_info.value)
            mock_create_fact.assert_called_once_with('Test fact', 'science')

if __name__ == '__main__':
    pytest.main([__file__])