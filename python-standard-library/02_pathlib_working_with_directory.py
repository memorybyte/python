"""Working with Directory"""

from pprint import pprint
from pathlib import Path

# Path to directory
path = Path('ecommerce')

path.exists() # checks if this path exists or not

# mkdir()
# path.mkdir() # creates a new directory at the location specified by the Path object.
# path.mkdir(parents=True, exist_ok=True) 
# parents=True ->  means that any missing parent directories in the path will also be created automatically.
# exist_ok=True -> Does not Raise FileExistsError if the directory already exists

# rmdir(): removes (deletes) the directory specified by the Path object, but only if the directory is empty. Otherwise raises OSError
# path.rmdir()

# rename(): renames the file or directory represented by path to 'ecommerce2'.
# path.rename('ecommerce2') # renames dir commerce to commerce2, since path holds ecommerce

# path = Path('ecommerce/__init__.txt')
# p = path.rename('ecommerce/__init__.py')
# print(f'{path}\n{p}')


# iterdir(): returns an iterator over all files and directories in the given directory.
path = Path()
# pprint(path.iterdir()) # returns generator
# pprint(list(path.iterdir())) # returns generator

paths = [p for p in path.iterdir()]
paths = [p for p in path.iterdir() if not p.is_dir()]
# pprint(paths)


# glob():  returns an iterator of all files and directories matching a specified pattern within the given directory.
# It searches only the immediate directory (not subdirectories).
# For recursive search, use path.rglob().
py_files = [p for p in path.glob('*.py')]
# pprint(py_files)


# rglob()
py_files = [p for p in path.rglob('*.py')]
pprint(py_files)