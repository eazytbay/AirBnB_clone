#!/usr/bin/env python3
"""
This is class that contains all the attributes required to model out the class
"place"
"""


from models.base_model import BaseModel



class Place(BaseModel):
    """
    Gives information about the listed place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
