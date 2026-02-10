import pytest
from unittest.mock import Mock, patch
import sys
import os
import json

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask
from rest.vote_fact import vote_route
from fact import Fact


class TestVoteFactRoute:
    """Test the vote_route function"""

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

    @patch('rest.vote_fact.vote_fact')
    def test_vote_route_like_success(self, mock_vote_fact, app):
        """Test successful like vote"""
        # ARRANGE
        mock_fact = Fact(id=1, fact="Test fact", category="science", likes=6, dislikes=2)
        mock_vote_fact.return_value = mock_fact

        json_data = {"fact_id": 1, "vote_type": "like"}

        with app.test_request_context('/', method='POST', json=json_data):
            with patch('rest.vote_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "json response"

                # ACT
                result = vote_route()

                # ASSERT
                mock_vote_fact.assert_called_once_with(1, "like")
                mock_jsonify.assert_called_once_with({
                    "fact_id": 1,
                    "new_count": 6,  # updated_fact.likes (like vote)
                    "likes": 6,
                    "dislikes": 2
                })
                assert result == ("json response", 200)

    @patch('rest.vote_fact.vote_fact')
    def test_vote_route_dislike_success(self, mock_vote_fact, app):
        """Test successful dislike vote"""
        # ARRANGE
        mock_fact = Fact(id=2, fact="Another fact", category="history", likes=5, dislikes=8)
        mock_vote_fact.return_value = mock_fact

        json_data = {"fact_id": 2, "vote_type": "dislike"}

        with app.test_request_context('/', method='POST', json=json_data):
            with patch('rest.vote_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "dislike response"

                # ACT
                result = vote_route()

                # ASSERT
                mock_vote_fact.assert_called_once_with(2, "dislike")
                mock_jsonify.assert_called_once_with({
                    "fact_id": 2,
                    "new_count": 8,  # updated_fact.dislikes (dislike vote)
                    "likes": 5,
                    "dislikes": 8
                })
                assert result == ("dislike response", 200)

    @patch('rest.vote_fact.vote_fact')
    def test_vote_route_value_error_handling(self, mock_vote_fact, app):
        """Test handling of ValueError from vote_fact function"""
        # ARRANGE
        mock_vote_fact.side_effect = ValueError("Invalid vote type")
        json_data = {"fact_id": 1, "vote_type": "invalid"}

        with app.test_request_context('/', method='POST', json=json_data):
            with patch('rest.vote_fact.jsonify') as mock_jsonify:
                mock_jsonify.return_value = "error response"

                # ACT
                result = vote_route()

                # ASSERT
                mock_vote_fact.assert_called_once_with(1, "invalid")
                mock_jsonify.assert_called_once_with({"error": "Invalid vote type"})
                assert result == ("error response", 400)

if __name__ == '__main__':
    pytest.main([__file__])