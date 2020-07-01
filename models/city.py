#!/usr/bin/python3
"""Module City"""


from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from Base Model"""
    state = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City class"""
        super().__init__(*args, **kwargs)
