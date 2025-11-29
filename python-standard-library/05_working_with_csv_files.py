"""Working with CSV Files"""

import csv

# Write to a CSV
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file, )

#     writer.writerow(['transaction_id', 'product_id', 'price'])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])


# Read from a CSV
with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)

    rows = list(reader)

    for row in rows:
        print(row)