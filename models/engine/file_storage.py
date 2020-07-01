#!/usr/bin/python3
"""that serializes instances from and to a JSON file"""
import json
import sys
from models.base_model import BaseModel


class FileStorage():
    """serializes instances from and to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        try:
            copy_dict = FileStorage.__objects.copy()
            for key, value in copy_dict.items():
                if not isinstance(value, dict):
                    copy_dict[key] = value.to_dict()
            with open(self.__file_path, "w") as File:
                json.dump(copy_dict, File)
        except(TypeError):
            pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as json_file:
                dict_from_json = json.load(json_file)
                for key, value in dict_from_json.items():
                    tmp = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = tmp
        except(FileNotFoundError):
            pass
