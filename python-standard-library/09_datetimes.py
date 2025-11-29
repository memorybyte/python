"""Working with Datetimes"""

from datetime import datetime
import time

dt = datetime(2018, 2, 1, 19, 10, 59)
current = dt.now()

# print(dt)
# print(current)

# datetime.strptime(): parses a string representing a date and/or time and returns a datetime object, using a specified format.
dt = datetime.strptime('2025-11-30', '%Y-%m-%d')
# print(dt)  # # Output: 2025-11-30 00:00:00

# Convert timestamp into datetime object
dt = datetime.fromtimestamp(time.time())
# print(dt)


## datetime.strftime(): formats a datetime object as a string according to a specified format.
# while True:
#     dt = datetime.now()
#     formatted = dt.strftime('%Y-%m-%d %H:%M:%S')
#     print(formatted)  # Example output: 2025-11-30 14:23:45
#     time.sleep(1)