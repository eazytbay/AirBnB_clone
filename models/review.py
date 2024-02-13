#!/usr/bin/env python3
"""
This class models the class "review" class
"""



from models.base_model import BaseModel



class Review(BaseModel):
    """
    All reviews will be modelled from this particular class
    """
    place_id = ""
    user_id = ""
    text = ""
