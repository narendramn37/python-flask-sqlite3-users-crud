import unittest
from unittest.mock import MagicMock, patch
from db import DBConnection
from model import User


class TestDBConnection(unittest.TestCase):
    @patch('db.sqlite3')
    def test_create_tables(self, mock_sqlite3):
        mock_cursor = MagicMock()
        mock_db_conn = MagicMock()
        mock_db_conn.cursor.return_value = mock_cursor
        mock_sqlite3.connect.return_value = mock_db_conn

        db = DBConnection()
        mock_cursor.execute.return_value = None
        status, response, message, status_code = db.create_tables()
        self.assertTrue(status)
        self.assertEqual(response, None)
        self.assertEqual(message, "Table created successfully")
        self.assertEqual(status_code, 201)

    @patch('db.sqlite3')
    def test_create_user(self, mock_sqlite3):
        # Create a mock cursor
        mock_cursor = MagicMock()

        # Create a mock database connection
        mock_db_conn = MagicMock()
        mock_db_conn.cursor.return_value = mock_cursor
        mock_sqlite3.connect.return_value = mock_db_conn
        db = DBConnection()
        mock_cursor.execute.return_value = None
        sample_user = User("Narendra", "narendra@gmail.com", 25, True)

        status, response, message, status_code = db.create_user(sample_user)

        self.assertTrue(status)
        self.assertEqual(response, sample_user.__dict__)
        self.assertEqual(message, "User created successfully")
        self.assertEqual(status_code, 201)


if __name__ == '__main__':
    unittest.main()
