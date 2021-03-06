"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import platform
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv[0])

# Print out the OS platform you're using:
# YOUR CODE HERE
print(platform.system())

# Print out the version of Python you're using:
# YOUR CODE HERE
print(platform.release())

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.geteuid())


# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print(os.environ.get('USER'))





'''
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
elif _platform == "darwin":
    # MAC OS X
elif _platform == "win32":
    # Windows
elif _platform == "win64":
'''
