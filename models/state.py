#!/usr/bin/python3
"""Module State"""


from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel"""
    name = ""

    def __init__(self):
        """Initialize State class"""
        super().__init__()
