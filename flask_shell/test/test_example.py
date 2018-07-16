"""Test all routes for data creation, modification, and query."""

import datetime

from .base_test import BaseTest

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
        """Test the route for querying a single database value."""
        example = Example(string='text',
                          boolean=False,
                          integer=1)
        self.default_get('/example', example)

    def test_add_example(self):
        """Test the route for creating a database value."""
        payload = {'string': 'text',
                   'boolean': False,
                   'integer': 1}

        self.default_post('example',
                          payload,
                          Example,
                          [])
