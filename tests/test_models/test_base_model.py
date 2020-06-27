#!/usr/python3
'''
tests
'''
import unittest
from models.base_model import BaseModel
from engine.file_storage import FileStorage
import datetime


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
        self.assertIsInstance(bm1.to_dict()['created_at'], str)
        self.assertNotIsInstance(bm1.updated_at, str)
        self.assertEqual(type(bm1.updated_at), datetime.datetime)
        self.assertIsInstance(bm1.updated_at, datetime.datetime)

    def test_adding_thing_from_outside(self):
        """testing adding attributes from outside"""
        bm1 = BaseModel()
        bm1.name = "Holberton"
        self.assertTrue(bm1.to_dict()["name"])
        self.assertIn("name", bm1.to_dict())

    def test_to_dictionary_recreating(self):
        """Generating the dictionary """
        bm1 = BaseModel()
        bm1.name = "Holberton"
        dictionary_bm1 = bm1.to_dict()
        bm2 = BaseModel(**dictionary_bm1)
        self.assertIsNot(bm1, bm2)
        self.assertEqual(bm1.to_dict(), bm2.to_dict())

    def test_FileStorage_all_module(self):
        """Testing all module"""
        bm1 = BaseModel()
        bm1.name = "Holberton"
        bm1.QQQQQQQQ = "!!!!!!!!!!!!"
        bm2 = BaseModel()
        fs1 = FileStorage()
        fs1_all_return = fs1.all()
        print(fs1_all_return)
