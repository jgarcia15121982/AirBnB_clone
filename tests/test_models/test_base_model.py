#!/usr/python3
'''
tests
'''
import unittest
from models.base_model import BaseModel

class test_constructor(unittest.TestCase):
    ''' tests for Base Class Constructor Method '''

    def test_id_normal(self):
        '''id'''
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
