## GENERATOR Comprehension

# SYNTAX: (expression for item in iterable if condition)
# Generates one at a time

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = (sale for sale in daily_sales  if sale > 5)

# print(total_cups.__next__())
print(sum(total_cups))