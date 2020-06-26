#!/usr/bin/python3
'''
Base Model
'''
import time
from datetime import datetime
import uuid




class BaseModel:
    """ Base class manage id attribute in all your future classes """

    def __init__(self, id=None):
        """ Constructor method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")

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
        updated_at = datetime.today()

    def to_dict(self):
        """
        Method that returns the dictionary
        representation of the Base class
        """  
        self.__dict__['__class__'] = __class__.__name__
        return self.__dict__
