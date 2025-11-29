"""Working with JSON Files"""

from pathlib import Path
import json

'''
json.dump(obj, file):
Serializes (converts) a Python object (obj) to JSON and writes it directly to a file-like object (file).

json.dumps(obj):
Serializes a Python object (obj) to a JSON-formatted string (returns the string, does not write to a file).


json.load(file):
Reads JSON data from a file-like object and deserializes it into a Python object.

json.loads(s):
Reads JSON data from a string (s) and deserializes it into a Python object.

'''


# use json.loads(), json.load(), json.dumps(), json.dump()

## 1. Convert python format to JSON
# movies = [
#     {'id': 1, 'title': 'Terminator', 'year': 1984},
#     {'id': 2, 'title': 'Kindergarten', 'year': 1990},
# ]

# Convert to json format
# data = json.dumps(movies) # dumps(): Get JSON as a string
# print(f'Type: {type(data)},\nData: {data}')

# Write to a file
# Path('movies.json').write_text(data)

# dump(data, file): write to a file
# with open('movies.json', 'w') as file:
#     json.dump(data, file)


## 2. Convert JSON to python format

# using Path(), json.loads()
# json_data = Path('movies.json').read_text()
# movies = json.loads(json_data)
# print(f'Type: {type(movies)}\nData: {movies}')

# using file, json.load()
with open('movies.json', 'r') as file:
    movies = json.load(file)
    print(f'Type: {type(movies)}\nData: {movies}')