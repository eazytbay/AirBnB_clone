#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """This is a Test Case for the Amenity class."""

    def setUp(self):
        """This Sets up test for methods."""
        pass

    def tearDown(self):
        """This Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """FileStorage data reseted."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Amenity class test instantiation."""

        x = Amenity()
        self.assertEqual(str(type(x)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(x, Amenity)
        self.assertTrue(issubclass(type(x), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for a, b in attributes.items():
            self.assertTrue(hasattr(o, a))
            self.assertEqual(type(getattr(o, a, None)), b)


if __name__ == "__main__":
    unittest.main()
