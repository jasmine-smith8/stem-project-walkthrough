import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database.vote_fact import vote_fact
from fact import Fact


class TestVoteFact:
    """Test the vote_fact function"""

    @patch.object(sys.modules['database.vote_fact'], 'PostgresConnectionProvider')
    def test_vote_fact_like_success(self, mock_provider_class):
        """Test successful like vote on a fact"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return values after like
        mock_cursor.fetchone.return_value = (1, "Test fact", "science", 6, 2)

        # Act
        result = vote_fact(1, "like")

        # Assert
        assert isinstance(result, Fact)
        assert result.id == 1
        assert result.fact == "Test fact"
        assert result.category == "science"
        assert result.likes == 6
        assert result.dislikes == 2

        # Verify SQL execution
        assert mock_cursor.execute.call_count == 2
        # Check like update query
        mock_cursor.execute.assert_any_call(
            "UPDATE facts SET likes = likes + 1 WHERE id = %s;",
            (1,)
        )
        # Check select query
        mock_cursor.execute.assert_any_call(
            "SELECT id, fact, category, likes, dislikes FROM facts WHERE id = %s;",
            (1,)
        )
        mock_provider.commit.assert_called_once()

    @patch.object(sys.modules['database.vote_fact'], 'PostgresConnectionProvider')
    def test_vote_fact_dislike_success(self, mock_provider_class):
        """Test successful dislike vote on a fact"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return values after dislike
        mock_cursor.fetchone.return_value = (2, "Another fact", "history", 5, 8)

        # Act
        result = vote_fact(2, "dislike")

        # Assert
        assert isinstance(result, Fact)
        assert result.id == 2
        assert result.fact == "Another fact"
        assert result.category == "history"
        assert result.likes == 5
        assert result.dislikes == 8

        # Verify SQL execution
        assert mock_cursor.execute.call_count == 2
        # Check dislike update query
        mock_cursor.execute.assert_any_call(
            "UPDATE facts SET dislikes = dislikes + 1 WHERE id = %s;",
            (2,)
        )
        # Check select query
        mock_cursor.execute.assert_any_call(
            "SELECT id, fact, category, likes, dislikes FROM facts WHERE id = %s;",
            (2,)
        )
        mock_provider.commit.assert_called_once()

    @patch.object(sys.modules['database.vote_fact'], 'PostgresConnectionProvider')
    def test_vote_fact_invalid_vote_type(self, mock_provider_class):
        """Test error handling for invalid vote type"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            vote_fact(1, "invalid")

        assert "Invalid vote type" in str(exc_info.value)

        # Verify no SQL execution for update (only cursor setup)
        mock_cursor.execute.assert_not_called()
        mock_provider.commit.assert_not_called()

    @patch.object(sys.modules['database.vote_fact'], 'PostgresConnectionProvider')
    def test_vote_fact_empty_vote_type(self, mock_provider_class):
        """Test error handling for empty vote type"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            vote_fact(1, "")

        assert "Invalid vote type" in str(exc_info.value)
        mock_cursor.execute.assert_not_called()
        mock_provider.commit.assert_not_called()

    @patch.object(sys.modules['database.vote_fact'], 'PostgresConnectionProvider')
    def test_vote_fact_with_null_likes_dislikes(self, mock_provider_class):
        """Test voting on fact with NULL likes/dislikes"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock result with NULL values
        mock_cursor.fetchone.return_value = (3, "Fact with nulls", "trivia", None, None)

        # Act
        result = vote_fact(3, "like")

        # Assert
        assert result.id == 3
        assert result.fact == "Fact with nulls"
        assert result.category == "trivia"
        assert result.likes is None
        assert result.dislikes is None

    @patch.object(sys.modules['database.vote_fact'], 'PostgresConnectionProvider')
    def test_vote_fact_cursor_context_manager(self, mock_provider_class):
        """Test that cursor context manager is used properly"""
        # Arrange
        mock_provider = Mock()
        mock_cursor_context = Mock()
        mock_cursor = Mock()

        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value = mock_cursor_context
        mock_cursor_context.__enter__ = Mock(return_value=mock_cursor)
        mock_cursor_context.__exit__ = Mock(return_value=None)

        mock_cursor.fetchone.return_value = (1, "Test fact", "test", 1, 0)

        # Act
        vote_fact(1, "like")

        # Assert
        mock_provider.cursor.assert_called_once()
        mock_cursor_context.__enter__.assert_called_once()
        mock_cursor_context.__exit__.assert_called_once()

if __name__ == '__main__':
    pytest.main([__file__])