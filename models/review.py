#!/usr/bin/python3
"""Module Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """Initialize User class"""
        super().__init__()
