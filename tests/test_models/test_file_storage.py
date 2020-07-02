#!/usr/bin/python3
"""File User Test Module"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unittest for class FileStorage"""
    def test_file_path(self):
        self.storage = FileStorage()
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.storage = FileStorage()
        self.assertIs(type(self.storage._FileStorage__objects), dict)

    def test_all(self):
        self.storage = FileStorage()
        obj_dict = self.storage.all()
        self.assertTrue(type(obj_dict) is dict)

    def test_new(self):
        bm1 = BaseModel()
        bm1_id = "{}.{}".format(bm1.__class__.__name__, bm1.id)
        self.storage = FileStorage()
        obj_dict = self.storage.all()
        self.assertTrue(bm1_id in obj_dict)
        self.assertTrue(obj_dict[bm1_id] is bm1)

    def test_save(self):
        bm1 = BaseModel()
        bm1_id = "{}.{}".format(bm1.__class__.__name__, bm1.id)
        self.storage = FileStorage()
        obj_dict_presave = self.storage.all()
        bm1.save()
        self.storage.reload()
        obj_dict_postsave = self.storage.all()
        self.assertTrue(bm1_id in obj_dict_postsave)
        self.assertTrue(obj_dict_postsave == obj_dict_presave)

    def test_reload(self):
        bm1 = BaseModel()
        bm1_id = "{}.{}".format(bm1.__class__.__name__, bm1.id)
        self.storage = FileStorage()
        obj_dict_presave = self.storage.all()
        bm1.save()
        self.storage.reload()
        obj_dict_postsave = self.storage.all()
        self.assertTrue(bm1_id in obj_dict_postsave)
        self.assertTrue(obj_dict_postsave == obj_dict_presave)

    def test_private_class_attributes(self):
        self.storage = FileStorage()
        with self.assertRaises(AttributeError):
            print(self.storage.__objects)
        with self.assertRaises(AttributeError):
            print(self.storage.__file_path)
