#!/usr/bin/python3
"""
Class BaseModel that defines all common attributes/methods for other classes:
"""

from datetime import date
import uuid

class BaseModel():
    def __init__(self):
        """
        Initializes class BaseModel
        """
        id = str(uuid.uuid4())
        created_at = datetime.today()
        updated_at = datetime.today()

    def __str__(self):
        """
        The __str__ magic method that returns
        the BaseModel description
        """
        return "[{}] ({}) {}".format(__class__, self.id, self.dict)
        
    def save(self):
        """
        Updates the public instance attribute update_at
        with the current datetime
        """
        updated_at = datetime.today()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        return self.__dict__
