"""Working with timedelta"""

from datetime import datetime, timedelta

# timedelta: deals with duration
# datetime: deals with point in time

dt1 = datetime(2025, 11, 28)
dt2 = datetime.now()

duration = dt2 - dt1
# print(type(duration), duration)

# print(f'Days: {duration.days}')
# print(f'Seconds: {duration.seconds}')
# print(f'Minutes: {duration.seconds / 60}')
# print(f'Total Seconds: {duration.total_seconds()}')


# We can add timedelta object to datetime object

dt1 = datetime(2025, 11, 29) + timedelta(days=1)
print(dt1)