AirBnB Clone
0x00. Table of Contents
0x01 Overview
0x02 Setup
0x03 Installation Guide
0x04 Testing Procedures
0x05 Usage Instructions
0x06 Creators
0x01 Overview
This is a collaborative project aimed at replicating the functionalities of AirBnB through a custom-built platform.

The core component is a command-line interpreter designed to facilitate the management of object abstractions and their storage. The interpreter is tasked with several key functions:

Creating new objects
Retrieving objects from files
Executing operations on objects
Destroying objects
0x02 Setup
<!-- Operating System -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Ubuntu"></a> <!-- Shell --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="Bash"></a> <!-- Programming Language --> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="Python"></a> </a> <!-- Text Editor --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Vim"></a> <!-- Integrated Development Environment --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Visual Studio Code"></a> </a><!-- Version Control System --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="Git"></a> <!-- Hosting Service --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="GitHub"></a>

Style guidelines adhered to:
pycodestyle (version 2.7.*)
PEP8
The entire development and testing process was conducted on an Ubuntu 20.04 LTS operating system utilizing Python 3.8.3. Text editing was performed using Vim 8.1.2269. Version control was managed through Git 2.25.1.

0x03 Installation Guide

https://github.com/eazytbay/AirBnB_clone.git

Navigate to the AirBnb directory and execute the following command:

bash
Copy code
./console.py
Execution
Interactive mode:

bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
Non-interactive mode:

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
