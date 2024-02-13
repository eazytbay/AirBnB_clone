#!/usr/bin/python3
"""This is Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """This is a test Case for the BaseModel class."""

    def setUp(self):
        """This Sets up test methods."""
        pass

    def tearDown(self):
        """Test methods are torn down."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """FileStorage data is reseted."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_instantiation(self):
        """Instantiation of BaseModel class test."""

        x = BaseModel()
        self.assertEqual(str(type(x)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(x), BaseModel))

    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        disp = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), disp)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [y for y in range(1000)]
        x = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        x = BaseModel(*args)

    def test_3_attributes(self):
        """Tests attributes value for instance of a BaseModel class."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for a, b in attributes.items():
            self.assertTrue(hasattr(o, a))
            self.assertEqual(type(getattr(o, a, None)), b)

    def test_3_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        x = BaseModel()
        diff = x.updated_at - x.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = x.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_3_id(self):
        """Tests for unique user ids."""

        t = [BaseModel().id for y in range(1000)]
        self.assertEqual(len(set(t)), len(t))

    def test_3_save(self):
        """Tests the public instance method save()."""

        x = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        x.save()
        diff = x.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_3_str(self):
        """Tests for __str__ method."""
        x = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        a = res.group(3)
        b = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        c = json.loads(s.replace("'", '"'))
        c2 = b.__dict__.copy()
        c2["created_at"] = repr(c2["created_at"])
        c2["updated_at"] = repr(c2["updated_at"])
        self.assertEqual(c, c2)

    def test_3_to_dict(self):
        """Tests the public instance method to_dict()."""

        x = BaseModel()
        x.name = "Laura"
        x.age = 23
        c = x.to_dict()
        self.assertEqual(c["id"], x.id)
        self.assertEqual(c["__class__"], type(x.__name__)
        self.assertEqual(c["created_at"], x.created_at.isoformat())
        self.assertEqual(c["updated_at"], x.updated_at.isoformat())
        self.assertEqual(c["name"], x.name)
        self.assertEqual(c["age"], x.age)

    def test_3_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        disp = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), disp)

    def test_3_to_dict_excess_args(self):
        """Tests to_dict() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        disp = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_4_instantiation(self):
        """Tests instantiation with **kwargs."""

        custom_model = BaseModel()
        custom_model.name = "Holberton"
        custom_model.my_number = 89
        custom_model_json = my_model.to_dict()
        custom_new_model = BaseModel(**my_model_json)
        self.assertEqual(custom_new_model.to_dict(), custom_model.to_dict())

    def test_4_instantiation_dict(self):
        """Tests instantiation with **kwargs from custom dict."""
        c = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        o = BaseModel(**c)
        self.assertEqual(o.to_dict(), c)

    def test_5_save(self):
        """Tests that storage.save() is called from save()."""
        self.resetStorage()
        x = BaseModel()
        x.save()
        key = "{}.{}".format(type(x).__name__, c.id)
        c = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(x)))
            f.seek(0)
            self.assertEqual(json.load(f), c)

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        disp = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), disp)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        disp = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), disp)


if __name__ == '__main__':
    unittest.main()
