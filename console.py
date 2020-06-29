#!/usr/bin/python3
"""AirBnB console"""
import cmd, sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Console of AirBnB"""
    prompt = '(hbnb)'
    def do_quit(self, args):
        """Quit command, exits the program """
        exit()
    def do_EOF(self, args):
        """ End of file, exits the program"""
        exit()
    def do_create(self, args):
        """Creates a Base model instance and saves it to  the JSON file"""
        if len(args.split()) == 0:
            print("** class name missing **")
        else:
            if args.split()[0] == "BaseModel":
                instance = BaseModel()
                instance.save()
            else:
                print("** class doesn't exist **")
    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if len(args.split()) == 0:
            print("** class name missing **")
        elif len(args.split()) == 1:
            if args.split()[0] == "BaseModel":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            try:
                print(storage.all()[args.split()[0] + "." + args.split()[1]])
            except:
                print("** no instance found **")
    def do_destroy(self, args):
        """Destroys an instance"""
        if len(args.split()) == 0:
            print("** class name missing **")
        elif len(args.split()) == 1:
            if args.split()[0] == "BaseMode":
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            try:
                del storage.all()[args.split()[0] + "." + args.split()[1]]
                storage.save()
            except:
                print("** no instance found **")
    def do_all(self, args):
        print("[", end="")
        for i, instance in enumerate(BaseModel.instances):
            print("\"{}\"".format(instance), end="")
            if i != len(BaseModel.instances) - 1:
                print(", ")
        print("]")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
print("[", end=="")
