from datetime import datetime

import mongomock
from pytest import fixture as pytest_fixture

import models.queue as queue_collection
from general.cursor_deserialize import cursor_deserialize


class TestQueue:
    """Test the queue model"""

    @pytest_fixture
    def queue(self):
        """Fake queue item"""
        yield queue_collection.Queue(
            id=datetime.today().timestamp(), url="https://google.com"
        )

    @pytest_fixture
    def mock_client(self):
        """Mock mongodb client"""
        yield mongomock.MongoClient()

    @pytest_fixture
    def mock_db(self, mock_client):
        """Mock database"""
        yield mock_client["db"]

    def test_create_queue(self, mock_db, queue):
        """Test get queue function"""
        new_item = queue_collection.create_queue(queue.url, mock_db)

        items = cursor_deserialize(mock_db.queue.find())

        assert [
            item
            for item in items
            if item["id"] == new_item["id"]
            if item["url"] == new_item["url"]
        ]
        assert len(items) == 1

    def test_get_queue(self, mock_db, queue):
        """Test get queue function"""
        new_item = queue_collection.create_queue(queue.url, mock_db)
        items = cursor_deserialize(queue_collection.get_queue(mock_db))

        assert [
            item
            for item in items
            if item["id"] == new_item["id"]
            if item["url"] == new_item["url"]
        ]
        assert len(items) == 1
