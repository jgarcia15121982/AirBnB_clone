# AirBnB Clone Project

![AirBnB Clone](http://www.plugandgo.es/wp-content/uploads/2018/09/airbnb-logo-meaning.jpg)

## AirBnB clone - The console

```bash
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```

## Description

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## Learning Objectives

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## How to Use it
* To install the console, clone our repository by running the command `git clone https://github.com/AngieCastano1634/AirBnB_clone.git`
* To start the console, run the command `./console.py` in the main directory (`AirBnB_clone`) for interactive mode.
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb)
```
* Our console also works in non-interactive mode as such:
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```
For help on syntax, type the command `help <command>` into the console.

## Authors

* Angie Castaño <1634@holbertonschool.com>
* John Garcia <1620@holbertonschool.com>

