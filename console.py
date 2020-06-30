#!/usr/bin/python3
"""AirBnB console"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console of AirBnB"""
    prompt = '(hbnb) '

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
                print(str(instance.id))
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id"""
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
            if args.split()[0] == "BaseModel":
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
        inst = []
        if args.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                inst.append(str(value))
            print(inst)

    def do_update(self, args):
        """updates an object considering its id"""
        setattr(storage.all()[args.split()[0] + "." + args.split()[1]],
                args.split()[2], args.split()[3])
        storage.save()

    def do_save(self, args):
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
