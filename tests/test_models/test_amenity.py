#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)
    
    def test_pep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")



if __name__ == "__main__":
    unittest.main()
