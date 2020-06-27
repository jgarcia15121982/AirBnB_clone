#!/usr/bin/python3
'''
Base Model
'''
import time
from datetime import datetime
import uuid
from models import storage

class BaseModel:
    """ Base class manage id attribute in all your future classes """
    def __init__(self, **kwargs):
        """ Constructor method"""
        if kwargs:
            kwargs.pop('__class__')
            for a in kwargs:
                if a == "created_at" or a == "updated_at":
                    setattr(self, a, datetime.strptime(kwargs[a],
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, a, kwargs[a])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """
        The __str__ magic method that returns
        the BaseModel description
        """
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute update_at
        with the current datetime
        """
        updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        Method that returns the dictionary
        representation of the Base class
        """
        copy = self.__dict__.copy()
        copy['__class__'] = self.__class__.__name__
        copy['created_at'] = self.created_at.isoformat()
        copy['updated_at'] = self.updated_at.isoformat()
        return copy
    
