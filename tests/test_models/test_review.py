#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """ A test Case for the Review class."""

    def setUp(self):
        """Test methods is set up."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """FileStorage data rested."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Class Review instantiation test."""

        x = Review()
        self.assertEqual(str(type(x)), "<class 'models.review.Review'>")
        self.assertIsInstance(x, Review)
        self.assertTrue(issubclass(type(x), BaseModel))

    def test_8_attributes(self):
        """Class "Review" attributes tests"""
        attributes = storage.attributes()["Review"]
        o = Review()
        for a, b in attributes.items():
            self.assertTrue(hasattr(o, a))
            self.assertEqual(type(getattr(o, a, None)), b)


if __name__ == "__main__":
    unittest.main()
