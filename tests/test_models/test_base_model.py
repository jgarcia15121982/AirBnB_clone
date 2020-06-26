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
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertIsInstance(bm1.id, str)
        self.assertNotEqual(bm1, bm2)
        self.assertNotEqual(bm1.id, bm2.id)

    def test_dict(self):
        """ testing to_dict method"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1.to_dict(), dict)
        self.assertTrue(bm1.to_dict()["__class__"])
        self.assertTrue(type(bm1.created_at), type(bm1.updated_at))
        bm1.save()
        self.assertTrue(type(bm1.created_at), type(bm1.updated_at))
        self.assertNotEqual(bm1.created_at, bm1.updated_at)
        self.assertIsInstance(bm1.created_at, str)
        self.assertIsInstance(bm1.updated_at, str)

    def test_adding_thing_from_outside(self):
        """testing adding attributes from outside"""
        bm1 = BaseModel()
        bm1.name = "Holberton"
        self.assertTrue(bm1.to_dict()["name"])
        self.assertIn("name", bm1.to_dict())
