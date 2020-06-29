#!/usr/bin/python3
"""Module User"""


from models.base_model import Base


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """Initialize User class"""
        super().__init__()
