#!/usr/bin/python3

"""Unittest module for the User Class."""


import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """This is a test Case for the User class."""

    def setUp(self):
        """This Sets up the test methods."""
        pass

    def tearDown(self):
        """This tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """FileStorage data reseted."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """User class test instantiation."""

        x = User()
        self.assertEqual(str(type(x)), "<class 'models.user.User'>")
        self.assertIsInstance(x, User)
        self.assertTrue(issubclass(type(x) BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for a, b in attributes.items():
            self.assertTrue(hasattr(o, a))
            self.assertEqual(type(getattr(o, a, None)), b)


if __name__ == "__main__":

    unittest.main()
