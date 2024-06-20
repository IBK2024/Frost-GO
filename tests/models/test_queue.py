from datetime import datetime
from typing import Any, Generator

import mongomock
from pytest import fixture as pytest_fixture

import models.queue as queue_collection


class TestQueue:
    """Test the queue model"""

    @pytest_fixture
    def queue(self) -> Generator[queue_collection.QueueModel, Any, None]:
        """Fake queue model"""
        yield queue_collection.QueueModel(
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

    @pytest_fixture
    def mock_collection(self, mock_db):
        "Mock collection"
        yield mock_db["collection"]

    @pytest_fixture
    def queue_object(self, mock_collection):
        """Fake queue object"""
        yield queue_collection.Queue(mock_collection)

    def test_add(self, mock_collection, queue, queue_object):
        """Test create queue function"""
        new_item = queue_object.add(queue.url)

        items = list(mock_collection.find())

        assert [
            item
            for item in items
            if item["id"] == new_item["id"]
            if item["url"] == new_item["url"]
        ]
        assert len(items) == 1

    def test_get(self, queue, queue_object):
        """Test get queue function"""
        new_item = queue_object.add(queue.url)
        items = queue_object.get()

        assert [
            item
            for item in items
            if item["id"] == new_item["id"]
            if item["url"] == new_item["url"]
        ]
        assert len(items) == 1

    def test_delete(self, queue, queue_object):
        "Test delete queue function"
        new_item = queue_object.add(queue.url)
        queue_object.delete(new_item["id"])
        items = queue_object.get()

        assert len(items) == 0
