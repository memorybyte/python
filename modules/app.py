from pprint import pprint

## 1. Modules

from ecommerce.shopping.sales import calc_shopping, calc_tax
# from sales import *

calc_shopping()
calc_tax()




## 2. Compiled Python Files
# Compiled Python files (.pyc) are created to improve performance by caching the bytecode, so Python doesn’t have to recompile the source code every time the program runs.





## 3. Module Search Path
# The module search path is a list of directories that Python searches to find a module when you use an import statement.


# When you import a module, Python looks for it in the following order:

# 1. The directory containing the input script (or the current directory).
# 2. The directories listed in the PYTHONPATH environment variable (if set).
# 3. The standard library directories.

import sys
# pprint(sys.path) # list of path that python will search for module

# If Python can’t find the module in any of these locations, it raises a ModuleNotFoundError.



## 4. Packages
# A package in Python is a way of organizing related modules into a single directory hierarchy. A package is simply a directory that contains a special __init__.py file (which can be empty) and one or more module files or sub-packages.

# Purpose:
# Packages help you organize and structure large codebases by grouping related modules together.

# You can import modules from a package using dot notation.


## 5. Sub-Packages
# A subpackage is a package that exists inside another package. 
# It is simply a subdirectory within a package directory, and it must also contain its own __init__.py file.
 


## 6. Intra-Package References:
# Intra-package reference refers to importing modules or subpackages from within the same package using relative imports.

# Relative imports use a dot (.) notation:
# 1. A single dot (.) refers to the current package.
# 2. Two dots (..) refer to the parent package.

# Intra-package references help keep imports organized and avoid hardcoding full package paths.




## 7. The dir() Function:
# The dir() function in Python returns a list of names in the current local scope or the attributes of a specified object.
# dir() — Lists all names in the current scope.
# dir(object) — Lists all valid attributes and methods of the given object.
pprint(__file__)

from ecommerce.shopping import sales

print("DIR(sales): ", dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)


## 8. Executing Module as Scripts

