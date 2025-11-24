## Types of Functions:
# 1. Pure Function vs Impure Function
# 2. Recursive Function
# 3. Lambda or Anonymous Function


# 1. 

def pure_chai(cups):
    return cups * 10

total_chai = 0

# Not recommended
# Impure functions modify global variables
def impure_chai(cups):
    global total_chai

    total_chai += cups

# 2. 

def pour_chai(n):
    if n == 0:
        return 'All cups poured'
    return pour_chai(n-1)


# 3. Lambda Function

chai_type = ['Light', 'Kadak', 'Ginger', 'Kadak']
strong_chai = list(filter(lambda chai: chai!='Kadak', chai_type))
print(strong_chai)