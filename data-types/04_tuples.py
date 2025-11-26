## Tuples
# A read-only list
point = () # empty tuple
point = 1 # int
point = 1, # tuple
point = (1, 2)
point = 1, 2 # If we have multiple elements, () is optional
print(type(point))

point = (1, 2) + (3, 4)
point = (1, 2) * 4

point = tuple('Hello World')
point = tuple([1, 2]) # from a list to tuple
print(point)

masala_spices = ('Cardamom', 'Cloves', 'Cinnamon')



# Unpacking
(spice1, spice2, spice3) = masala_spices
# print(f'Main Masala Spices: {spice1}, {spice2} and {spice3}')

point = (1, 2, 3)
x, y, z = point


# Behind the scene: 2, 1 is (2, 1)
ginger_ratio, cardamom_ratio = 2, 1


# Membership
# print(f'Is ginger in masala spices ? {"ginger" in masala_spices}')

point = (1, 2, 3)
if 10 in point:
    print('Exists')



# Swapping two variables
x = 10
y = 11
x, y = y, x # Internally it is tuple, 