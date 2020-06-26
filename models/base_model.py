#!/usr/bin/python3
'''
Base Model
'''
import time
from datetime import date
import uuid



class BaseModel:
    """ Base class manage id attribute in all your future classes """

    def __init__(self, id=None):
        """ Constructor method """
        self.id = str(uuid.uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()

    def __str__(self):
        """
        The __str__ magic method that returns
        the BaseModel description
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute update_at
        with the current datetime
        """
        updated_at = date.today()

    def to_dict(self):
        """
        Method that returns the dictionary
        representation of the Base class
        """
        bs_dict = {}
        bs_dict['id'] = self.id
        bs_dict['created_at'] = self.created_at.isoformat()
        bs_dict['updated_at'] = self.updated_at.isoformat()
        return bs_dict
