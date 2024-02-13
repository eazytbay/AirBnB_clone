#!/usr/bin/python3
"""This is a Unittest module for the Class "City"."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
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
        """Tests instantiation of City class."""

        x = City()
        self.assertEqual(str(type(x)), "<class 'models.city.City'>")
        self.assertIsInstance(x, City)
        self.assertTrue(issubclass(type(x), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        o = City()
        for a, b in attributes.items():
            self.assertTrue(hasattr(o, a))
            self.assertEqual(type(getattr(o, a, None)), b)


if __name__ == "__main__":
    unittest.main()
