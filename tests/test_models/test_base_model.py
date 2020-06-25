#!/usr/bin/python3
"""Testing to Base Models"""
import unittest
from models.base_model import BaseModel


class TestBaseModels(unittest.TestCase):
    """
    testing the id
    """
    def Test_uuid(self):
        """
        test id
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
