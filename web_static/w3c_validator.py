#!/usr/bin/python3
"""
W3C validator for Holberton School

For HTML and CSS files.

Based on 1 API:
- https://validator.w3.org/docs/api.html

Usage:

Simple file:

```
./w3c_validator.py index.html
```

Multiple files:

```
./w3c_validator.py index.html header.html styles/common.css
```

All errors are printed in `STDERR`

Return:
Exit status is the # of errors, 0 on Success
"""
import sys
import requests
import os


def __print_stdout(msg):
    """Print message in STDOUT
    """
    sys.stdout.buffer.write(msg.encode('utf-8'))


def __print_stderr(msg):
    """Print message in STDERR
    """
    sys.stderr.buffer.write(msg.encode('utf-8'))


def __is_empty(file):
    if os.path.getsize(file) == 0:
        raise OSError("File '{}' is empty.".format(file))
def __validate(file_path, type):
    """
    Begin file validation
    """
    a = {'Content-Type': "{}; charset=utf-8".format(type)}
    # Open files in binary mode:
    # https://requests.readthedocs.io/en/master/user/advanced/
    x = open(file_path, "rb").read()
    y = "https://validator.w3.org/nu/?out=json"
    r = requests.post(u, headers=h, data=d)

    if not r.status_code < 400:
        raise ConnectionError("Unable to connect to API endpoint.")

    disp = []
    msgs = r.json().get('msgs', [])
    for t in msgs:
        # Files that have incomplete or broken HTML are captured
        if t['type'] == 'error' or t['type'] == 'info':
            disp.append("'{}' => {}".format(file_path, t['message']))
        else:
            disp.append("[{}:{}] {}".format(
                file_path, t['lastLine'], t['message']))
    return disp


def __analyse(file_path):
    """Start analyse of a file and print the result
    """
    nb_errors = 0
    try:
        result = None

        if file_path.endswith(".css"):
            __is_empty(file_path)
            result = __validate(file_path, "text/css")
        elif file_path.endswith((".html", ".htm")):
            __is_empty(file_path)
            result = __validate(file_path, "text/html")
        elif file_path.endswith(".svg"):
            __is_empty(file_path)
            result = __validate(file_path, "image/svg+xml")
        else:
            allowed_files = "'.css', '.html', '.htm' and '.svg'"
            raise OSError(
                "File {} does not have a valid file extension.\nOnly {} are "
                "allowed.".format(file_path, allowed_files)
   )

        if len(result) > 0:
            for msg in result:
                __print_stderr("{}\n".format(msg))
                nb_errors += 1
        else:
            __print_stdout("'{}' => OK\n".format(file_path))

    except Exception as e:
        __print_stderr("'{}' => {}\n".format(e.__class__.__name__, e))
    return nb_errors


def __files_loop():
    """Loop that analyses for each file from input arguments
    """
    nb_errors = 0
    for file_path in sys.argv[1:]:
        nb_errors += __analyse(file_path)

    return nb_errors


if __name__ == "__main__":
    """Main
    """
    if len(sys.argv) < 2:
        __print_stderr("usage: w3c_validator.py file1 file2 ...\n")
        exit(1)

    """execute tests, then exit. Exit status = # of errors (0 on success)
    """
    sys.exit(__files_loop())


                                                            
