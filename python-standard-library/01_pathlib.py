"""Working with Paths"""

# pathlib: The pathlib library provides an object-oriented approach to handling filesystem paths

# Cross-platform compatibility: Path handles differences between Windows and Unix-style paths automatically.

# Readable and concise code: Path operations (joining, splitting, etc.) use operators and methods, making code easier to read and write.

from pathlib import Path

# Creating Path object: can be created using absolute or relative path

# Absolute path
# Path("C:\\Program Files\\Microsoft")
Path(r"C:\Program Files\Microsoft") # For windows
Path("/usr/local/bin") # linux/mac

Path() # current folder
# print(f'Current Folder: {Path()}')

# Home directory of current user
# print(f'Home: {Path.home()}')

# Path('ecommerce/__init__.py') # Current folder, then go to ecommerce folder and then __init__.py file

# Combine path objects together
Path() / Path('ecommerce')
# or combine Path() objects with string
Path() / 'ecommerce' / '__init__.py'

path = Path('ecommerce/__init__.py')
path2 = Path('ecommerce/')

print(f'Path exists ? : {path.exists()}')
print(f'Is it a file ? : {path.is_file()}')
print(f'Is it a directory ? : {path.is_dir()}')

print(path.name)  # returns the final component (the file or directory name) of the path as a string.
print(path2.name) # returns the final component (the file or directory name) of the path as a string.

print(path.stem) # returns the final component of the path, without its file extension.

print(path.suffix) # returns the file extension of the final component, including the dot.
print(path2.suffix)

print(path.parent) # returns the directory containing the final component, as a Path object.
print(type(path.parent)) # WindowsPath
print(path2.parent)

# Create a new path object with the same parent directory
path = path.with_name('file.txt')
# creates a new Path object with the same parent directory as path, but replaces the final component (file or directory name) with 'file.txt'.
print(path)
print(f'Absolute path: {path.absolute}') # get the absolute path


## Create a new path object with different suffix
#  creates a new Path object with the same parent and name as path, but replaces the file extension with .txt.

# It does not modify the original path, but returns a new one with the updated suffix.
path = path.with_suffix('.txt')
print(path)