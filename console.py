#!/usr/bin/python3
"""AirBnB console"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """Console of AirBnB"""
    prompt = '(hbnb)'
    def do_quit(self, args):
        """Quit command, exits the program """
        exit()
    def do_EOF(self, args):
        """ End of file, exits the program"""
        exit()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
