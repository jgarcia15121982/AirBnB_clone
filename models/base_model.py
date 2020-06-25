#!/usr/bin/python3
'''
Base Model
'''
import uuid


class BaseModel:
    ''' Base class manage id attribute in all your future classes '''

    def __init__(self, id=None):
        ''' Constructor method '''
        self.id = uuid.uuid4()
