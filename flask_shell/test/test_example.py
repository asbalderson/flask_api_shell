"""Test all routes for Answer creation, modification, and query."""

import datetime

from .base_test import BaseTest

from ..database import DB
from ..database.tables.example_table import Example


class TestAnswer(BaseTest):
    """Class based on UnitTest.TestCase for testing answer routes."""

    def create_app(self):
        """Configure and stand up the flask app for testing """
        return BaseTest.create_app(self)

    def setUp(self):
        """Create a database for testing."""
        BaseTest.setUp(self)

    def tearDown(self):
        """Delete the database used during testing."""
        BaseTest.tearDown(self)

    def test_get_example(self):
        """Test the route for querying a single answer."""
        example = Example(text='text',
                          boolean=False,
                          intger=1,
                          date=datetime.datetime.utcnow())
        self.default_get('example', example)

    def test_add_example(self):
        """Test the route for creating an answer."""
        payload = {'text': 'text',
                   'boolean': False,
                   'integer': 1,
                   'date': datetime.datetime.utcnow()}

        self.default_post('answer',
                          payload,
                          Example,
                          [])
