"""Working with Files"""

from pathlib import Path
from time import ctime

path = Path('ecommerce/__init__.py')

# path.exists()
# path.rename('init.txt')
# path.unlink() # delete the file
# path.stat() # returns the information about the file
print(ctime(path.stat().st_birthtime)) # Creation time of this file


# Read files from the path
# path.read_bytes() # reads the content of the file as bytes object as binary data
# path.read_text() # read the content of the file as string

# Write to files
# path.write_bytes()
# path.write_text()


# Copying files
# Method 1
source = Path('ecommerce/__init__.py')
destination = Path() / '__init__.py'

# destination.write_text(source.read_text())

# MEthod 2
import shutil

shutil.copy(source, destination)
