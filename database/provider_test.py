import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database.provider import PostgresConnectionProvider


class TestPostgresConnectionProvider:
    """Test the PostgresConnectionProvider class"""

    @patch('database.provider.psycopg2.connect')
    def test_init_with_default_values(self, mock_connect):
        """Test initialization with default environment values"""
        # Arrange
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # Act
        provider = PostgresConnectionProvider()

        # Assert
        mock_connect.assert_called_once_with(
            dbname="factsdb",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        assert provider.conn == mock_connection

    @patch('database.provider.psycopg2.connect')
    @patch.dict(os.environ, {
        'POSTGRES_DB': 'test_db',
        'POSTGRES_USER': 'test_user',
        'POSTGRES_PASSWORD': 'test_pass',
        'POSTGRES_HOST': 'test_host',
        'POSTGRES_PORT': '5433'
    })
    def test_init_with_environment_variables(self, mock_connect):
        """Test initialization with custom environment variables"""
        # Arrange
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # Act
        provider = PostgresConnectionProvider()

        # Assert
        mock_connect.assert_called_once_with(
            dbname="test_db",
            user="test_user",
            password="test_pass",
            host="test_host",
            port="5433"
        )
        assert provider.conn == mock_connection

    @patch('database.provider.psycopg2.connect')
    @patch.dict(os.environ, {
        'POSTGRES_DB': 'partial_db',
        'POSTGRES_USER': 'partial_user'
        # Only some env vars set - others should use defaults
    })
    def test_init_with_partial_environment_variables(self, mock_connect):
        """Test initialization with partial environment variables"""
        # Arrange
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        # Act
        provider = PostgresConnectionProvider()

        # Assert
        mock_connect.assert_called_once_with(
            dbname="partial_db",        # From env
            user="partial_user",        # From env
            password="password",        # Default
            host="localhost",           # Default
            port="5432"                 # Default
        )

    @patch('database.provider.psycopg2.connect')
    def test_init_connection_error(self, mock_connect):
        """Test handling of connection errors during initialization"""
        # Arrange
        mock_connect.side_effect = Exception("Connection failed")

        # Act & Assert
        with pytest.raises(Exception) as exc_info:
            PostgresConnectionProvider()

        assert "Connection failed" in str(exc_info.value)

    @patch('database.provider.psycopg2.connect')
    def test_cursor_method(self, mock_connect):
        """Test cursor method returns connection cursor"""
        # Arrange
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        provider = PostgresConnectionProvider()

        # Act
        result = provider.cursor()

        # Assert
        mock_connection.cursor.assert_called_once()
        assert result == mock_cursor

    @patch('database.provider.psycopg2.connect')
    def test_cursor_method_multiple_calls(self, mock_connect):
        """Test cursor method can be called multiple times"""
        # Arrange
        mock_connection = Mock()
        mock_cursor1 = Mock()
        mock_cursor2 = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.side_effect = [mock_cursor1, mock_cursor2]

        provider = PostgresConnectionProvider()

        # Act
        cursor1 = provider.cursor()
        cursor2 = provider.cursor()

        # Assert
        assert mock_connection.cursor.call_count == 2
        assert cursor1 == mock_cursor1
        assert cursor2 == mock_cursor2

    @patch('database.provider.psycopg2.connect')
    def test_commit_method(self, mock_connect):
        """Test commit method calls connection commit"""
        # Arrange
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        provider = PostgresConnectionProvider()

        # Act
        provider.commit()

        # Assert
        mock_connection.commit.assert_called_once()

    @patch('database.provider.psycopg2.connect')
    def test_close_method(self, mock_connect):
        """Test close method calls connection close"""
        # Arrange
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        provider = PostgresConnectionProvider()

        # Act
        provider.close()

        # Assert
        mock_connection.close.assert_called_once()

    @patch('database.provider.psycopg2.connect')
    def test_cursor_commit_close_workflow(self, mock_connect):
        """Test typical workflow: cursor, commit, close"""
        # Arrange
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        provider = PostgresConnectionProvider()

        # Act
        cursor = provider.cursor()
        provider.commit()
        provider.close()

        # Assert
        mock_connection.cursor.assert_called_once()
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()
        assert cursor == mock_cursor

    @patch('database.provider.psycopg2.connect')
    def test_connection_with_empty_env_vars(self, mock_connect):
        """Test behavior with empty environment variables"""
        # Arrange
        mock_connection = Mock()
        mock_connect.return_value = mock_connection

        with patch.dict(os.environ, {
            'POSTGRES_DB': '',
            'POSTGRES_USER': '',
            'POSTGRES_PASSWORD': '',
            'POSTGRES_HOST': '',
            'POSTGRES_PORT': ''
        }):
            # Act
            provider = PostgresConnectionProvider()

        # Assert - empty strings should be used, not defaults
        mock_connect.assert_called_once_with(
            dbname="",
            user="",
            password="",
            host="",
            port=""
        )

if __name__ == '__main__':
    pytest.main([__file__])