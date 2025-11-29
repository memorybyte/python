"""Working with Timestamps"""

'''
The time module in Python provides functions to work with time and dates. 
It allows you to:
    - Get the current time
    - Pause (sleep) the program for a specified number of seconds
    - Measure elapsed time
    - Format and parse time values
'''

import time

print(time.time()) # Time in seconds from the beginning of time: 1970 January 1st
# We use this to performa calculations

def send_emails():
    for i in range(10000000000):
        pass


start = time.time()
send_emails()
end = time.time()

print(f'Total Time: {end - start:.5f}')