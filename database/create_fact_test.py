import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database.create_fact import create_fact
from fact import Fact


class TestCreateFact:
    """Test the create_fact function"""

    @patch.object(sys.modules['database.create_fact'], 'PostgresConnectionProvider')
    def test_create_fact_success(self, mock_provider_class):
        """Test successful fact creation"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return values
        mock_cursor.fetchone.return_value = (1, "Test fact", "science", 0, 0)

        # Act
        result = create_fact("Test fact", "science")

        # Assert
        assert isinstance(result, Fact)
        assert result.id == 1
        assert result.fact == "Test fact"
        assert result.category == "science"
        assert result.likes == 0
        assert result.dislikes == 0

        # Verify SQL execution
        mock_cursor.execute.assert_called_once()
        mock_provider.commit.assert_called_once()

    @patch.object(sys.modules['database.create_fact'], 'PostgresConnectionProvider')
    def test_create_fact_with_null_likes_dislikes(self, mock_provider_class):
        """Test fact creation when likes/dislikes are NULL in database"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database return with NULL values
        mock_cursor.fetchone.return_value = (2, "Another fact", "history", None, None)

        # Act
        result = create_fact("Another fact", "history")

        # Assert
        assert result.id == 2
        assert result.fact == "Another fact"
        assert result.category == "history"
        assert result.likes == 0  # Should default to 0 when NULL
        assert result.dislikes == 0  # Should default to 0 when NULL

    @patch.object(sys.modules['database.create_fact'], 'PostgresConnectionProvider')
    def test_create_fact_empty_strings(self, mock_provider_class):
        """Test fact creation with empty strings"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        mock_cursor.fetchone.return_value = (4, "", "", 0, 0)

        # Act
        result = create_fact("", "")

        # Assert
        assert result.id == 4
        assert result.fact == ""
        assert result.category == ""

    @patch.object(sys.modules['database.create_fact'], 'PostgresConnectionProvider')
    def test_create_fact_database_error(self, mock_provider_class):
        """Test handling of database errors during fact creation"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock database error
        mock_cursor.execute.side_effect = Exception("Database connection failed")

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            create_fact("Test fact", "test")

        assert "Database connection failed" in str(exc_info.value)
        mock_provider.commit.assert_not_called()

    @patch.object(sys.modules['database.create_fact'], 'PostgresConnectionProvider')
    def test_create_fact_no_result_returned(self, mock_provider_class):
        """Test handling when no result is returned from database"""
        # Arrange
        mock_provider = Mock()
        mock_cursor = Mock()
        mock_provider_class.return_value = mock_provider
        mock_provider.cursor.return_value.__enter__ = Mock(return_value=mock_cursor)
        mock_provider.cursor.return_value.__exit__ = Mock(return_value=None)

        # Mock no result returned
        mock_cursor.fetchone.return_value = None

        # Act & Assert
        with pytest.raises((TypeError, AttributeError)):
            create_fact("Test fact", "test")


if __name__ == '__main__':
    pytest.main([__file__])