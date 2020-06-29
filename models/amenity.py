#!/usr/bin/python3
"""Module Amenity"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""
    name = ""

    def __init__(self):
        """Initialize Amenity class"""
        super().__init__()
