"""Working with SQLite"""

import json
import sqlite3
from pathlib import Path

# movies = json.loads(Path('movies.json').read_text())
# print(data, type(data))

with open('movies.json', 'r') as file:
    movies = json.load(file)


# Write to db
# with sqlite3.connect('movies.sqlite3') as conn:

#     # # Create table if does not exist
#     # cursor = conn.cursor()

#     # cursor.execute('''
#     # CREATE TABLE IF NOT EXISTS Movies (
#     #     id INTEGER PRIMARY KEY,
#     #     title TEXT,
#     #     year INTEGER
#     #     )
#     #                '''
#     # )


#     command = 'INSERT INTO Movies VALUES (?, ?, ?)'
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()


# Read from db
with sqlite3.connect('movies.sqlite3') as conn:
    command = 'SELECT * FROM Movies'
    cursor = conn.execute(command)
    for row in cursor:
        print(row)

    # movies = cursor.fetchall() # fetches all movies in one go