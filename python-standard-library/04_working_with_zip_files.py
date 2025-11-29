"""Working with Zip Files"""

from pathlib import Path
from zipfile import ZipFile

# Writing to zip file
# with ZipFile('files.zip', 'w') as zip:
#     path = Path('ecommerce').rglob('*.*')

#     for p in path:
#         zip.write(p)

# Reading from zip file
with ZipFile('files.zip', 'r') as zip:
    print(zip.namelist()) # names all the files in zip file
    info = zip.getinfo('ecommerce/__init__.py')
    print(info.file_size)
    print(info.compress_size)
    zip.extractall('extract') # Extract the zip file to a folder 'extract'