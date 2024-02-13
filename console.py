#!/usr/bin/env python3
"""
The console.py contains the entry point of the command line interpreter
"""
#import the various modules needed

import cmd
import string
import sys
import string,sys
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This is command line interpreter that functions as
    a console to interact with the objects
    """
    def __init__(self):
        """
        Displays (hbnb) as the prompt text
        """
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exits the program when you type quit or q
        """
        sys.exit(1)

    def do_EOF(self, arg):
        """
        This functions to make the console know that no more input
        will be sent when you type EOF
        """
        return True

    def emptyline(self):
        """
        This is function that makes the console do nothing when no command is passed 
        or when a return character or space is pressed
        """
        pass

    def do_create(self, user_input):
        """This function creates a new BaseModel instance
            user_input = args
        """
        if len(user_input) == 0:
            print('** class name missing **')
            return
        try:
            instance_name = user_input + "()"
            new_instance = eval(instance_name)
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, user_input):

        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 49faff9a-6318-451f-87b6-910505c55907
        prints [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) 
        {
        'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 
        'id': '49faff9a-6318-451f-87b6-910505c55907', 
        'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)
        }
        """
        try:
            x = user_name.split()
            if len(x) == 0:
                print("** class name missing **")
                return
            for key, value in models.storage.all().items():
                if len(x) == 2:
                    if key == f"{x[0]}.{x[1]}":
                        print(value)
                        return
                if len(x) == 1:
                    if key.split(".")[0] != x[0]:
                        print("** class doesn't exist **")
                        return
                    if key.split(".")[0] == x[0]:
                        print("** instance id missing **")
                        return
            print("** no instance found **")
            return
        except Exception as exception:
            print(exception)

    def do_destroy(self, user_input):
        """
        This is a function that deletes an instance base on the class name and id
        ** no instance found **
        """
        try:
            x = user_input.split()
            if len(x) == 0:
                print("** class name missing **")
                return
            for key, value in models.storage.all().items():
                print(key.split(".")[0])
                if len(x) == 2:
                    if key == f"{x[0]}.{x[1]}":
                        models.storage.all().pop(key)
                        models.storage.save()
                        return
                if len(x) == 1:
                    if key.split(".")[0] != x[0]:
                        print("** class doesn't exist **")
                        return
                    if key.split(".")[0] == x[0]:
                        print("** instance id missing **")
                        return
            print("** no instance found **")
            return
        except Exception as exception:
            print(exception)

    def do_all(self, user_input):
        """
        This function Prints all the string represented on all instances whether 
        it is based on the class name or not.
        """
        x = user_name.split()
        try:
            for key, value in models.storage.all().items():
                if len(x) == 0:
                    print(value)
                    continue
                if len(x) == 1:
                    if key.split(".")[0] == x[0]:
                        print(value)
                        return
            print("** class doesn't exist **")
            return

        except Exception as exception:
            print(exception)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attributes
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        custom_arg = args.split()
        try:
            custom_obj = models.storage.all()
            if len(custom_arg) == 0:
                print("** class name missing **")
                return
            for key, value in models.storage.all().items():
                if len(custom_arg) >= 2:
                    if len(custom_arg) >= 4:
                        if key == f"{custom_arg[0]}.{custom_arg[1]}":
                            custom_obj[key].__dict__[custom_arg[2]] = custom_arg[3].strip('"')
                            models.storage.save()
                            return
                    else:
                        if custom_arg[2]:
                            print("** value missing **")
                            return
                        if custom_arg[1]:
                            print("** attribute name missing **")
                            return       
                if len(custom_arg) == 1:
                    if key.split(".")[0] != custom_arg[0]:
                        print("** class doesn't exist **")
                        return
                    if key.split(".")[0] == custom_arg[0]:
                        print("** instance id missing **")
                        return
            print("** no instance found **")
            return

        except Exception as exception:
            print(exception)


    #shortcuts
    do_q = do_quit
    do_c = do_create
    do_s = do_show
    do_d = do_destroy
    do_u = do_update

if __name__ == "__main__":
    HBNBCommand().cmdloop()
