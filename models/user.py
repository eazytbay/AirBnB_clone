#!/usr/bin/env python3


"""
This is a class "user" and what it does is to inherit from the
BaseModel created
"""


from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    This class Models out a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
