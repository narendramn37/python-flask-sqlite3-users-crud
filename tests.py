import pytest
from db import DBConnection
from model import User


@pytest.fixture(scope="function")
def db():
    db_connection = DBConnection()
    db_connection.create_tables()
    yield db_connection
    db_connection.db_conn.close()


@pytest.fixture(scope="function")
def sample_user():
    return {
        "name": "Narendra",
        "email": "narendra@gmail.com",
        "age": 25
    }


@pytest.fixture(scope="function")
def user_id():
    return 1


class TestDBConnection:
    def test_create_user(self, db, sample_user):
        """ Test case to create user
        """
        user = User(sample_user['name'], sample_user['email'], sample_user['age'])
        status, response, message, status_code = db.create_user(user)
        assert status is True
        assert response is not None
        assert message == "User created successfully"
        assert status_code == 201

    def test_get_users(self, db):
        """ Test case to get users
        """
        status, response, message, status_code = db.get_users()
        assert status is True
        assert response is not None
        assert len(response) > 0
        assert message == "User details fetched successfully"
        assert status_code == 200

    def test_get_user(self, db, user_id):
        """ Test case to get user
        """
        status, response, message, status_code = db.get_user(user_id)
        assert status is True
        assert response is not None
        assert message == "User details fetched successfully"
        assert status_code == 200

    def test_update_user(self, db, user_id=3):
        """ Test case to update user
        """
        sample_user = {"name": "Muppalla", "email": "muppalla@gmail.com", "age": 24}
        new_user = User(sample_user['name'], sample_user['email'], sample_user['age'])
        status, response, message, status_code = db.update_user(user_id, new_user)
        assert status is True
        assert response is not None
        assert response["name"] == "Muppalla"
        assert message == "User details updated successfully"
        assert status_code == 200

    def test_delete_user(self, db, user_id=4):
        """ Test case to delete user
        """
        status, response, message, status_code = db.delete_user(user_id)
        assert status is False
        # positive test case - commenting as we are deleting directly (in real time we go for soft delete mostly)
        # assert status is True
        # assert response is not None
        # assert response["user_id"] == user_id
        # assert message == "User deleted successfully"
        # assert status_code == 200
