#!/usr/bin/python3
"""that serializes instances to a JSON file and deserializes JSON file to instances"""
import json

class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.to_dict()["id"]] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(self.__file_path, mode="w+", encoding="utf-8") as File:
                copy = FileStorage.__objects.copy()
                for key, value in copy.items():
                    copy[key] = value.to_dict()
                string = json.dumps(copy)
                File.write(string)
        except(TypeError):
            pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as json_file:
                dicti_of_dicti = json.load(json_file)
                for key, value in dicti_of_dicti,items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
