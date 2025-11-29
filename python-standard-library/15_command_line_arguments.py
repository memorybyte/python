"""Working with command line arguments"""

import sys


# print(sys.argv)
# Prints the list sys.argv, which contains the command-line arguments passed to the script.
# sys.argv[0] is the script name always
# sys.argv[1:] are any additional arguments.

if len(sys.argv) == 1:
    print(f'USAGE: python3 app.py <password>')
else:
    password = sys.argv[1]
    print(f'Password: {password}')