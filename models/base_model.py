#!/usr/bin/python3
"""
A class called BaseModel that defines all common 
attributes/methods for other classes 
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """This  base class is for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Here, a new model is Instantiated if not created as a dictionary
            and its input is assigned the same instance attributes as their respective
            values when passed in as command line arguments

            """
        if kwargs.__len__() != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dig = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__
        representing the class name of the object.
        """
        custom_dict = self.__dict__.copy()
        custom_dict['__class__'] = self.__class__.__name__
        custom_dict['created_at'] = self.created_at.isoformat()
        custom_dict['updated_at'] = self.updated_at.isoformat()
        return custom_dict
