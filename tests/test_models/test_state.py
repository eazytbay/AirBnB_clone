#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """This is Test Case for the State class."""

    def setUp(self):
        """This Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Instantiation of the state class."""

        x = State()
        self.assertEqual(str(type(x)), "<class 'models.state.State'>")
        self.assertIsInstance(x, State)
        self.assertTrue(issubclass(type(x), BaseModel))

    def test_8_attributes(self):
        """Attributes of State class test."""
        attributes = storage.attributes()["State"]
        o = State()
        for a, b in attributes.items():
            self.assertTrue(hasattr(o, a))
            self.assertEqual(type(getattr(o, a, None)), b)


if __name__ == "__main__":
    unittest.main()
