## 1. Class 
# class Chai:
#     pass

# class ChaiTime:
#     pass

# print(f'Type: {type(Chai)}')
# ginger_tea = Chai()
# print(f'Type: {type(ginger_tea)}')
# print(type(ginger_tea) is Chai)
# print(type(ginger_tea) is ChaiTime)

## 2. Namespace
# Each object has its own namespace which does not affect other objects and class.

# class Chai:
#     origin = 'India'

# # print(Chai.origin)

# Chai.is_hot = True
# print(Chai.is_hot)

# # Creating objects from class chai
# masala = Chai()
# # print(f'{masala.origin} - {masala.is_hot}')

# masala.is_hot = False
# print(Chai.is_hot)

# masala.flavour = 'Masala'
# print(masala.flavour)
# print(Chai.flavour) # Exception: No attribute with name 'flavour'


## 3. Attribute Shadowing Property

# What is Attribute Shadowing:
#   - Attribute shadowing occurs when a variable in a subclass or instance hides a variable with the same name in its parent class.

#   - Each instance can have its own unique attributes that overshadow those inherited from the class.

#   - The parent class attribute remains accessible unless explicitly overridden in the subclass or instance.

#   - Attributes can be added or modified at runtime, providing flexibility in how instances behave.

#   - If an attribute is deleted from an instance, attempting to access it may lead to errors if it doesn’t exist in the parent class.

#   - Shadowing allows for better encapsulation of data specific to an instance or subclass, enabling behavior customization without altering the parent class.


# class Chai:
#     temperature = 'hot'
#     strength = 'strong'

# cutting = Chai()
# print(f'{cutting.temperature}')

# cutting.temperature = 'Mild'
# cutting.cup = 'Small'

# print(f'After changing: {cutting.temperature}')
# print(f'Cutting Cup Size: {cutting.cup}')
# print(f'Direct look into the class: {Chai.temperature}')

# del cutting.temperature
# del cutting.cup

# print(f'After deletion, temperature: {cutting.temperature}')
# print(f'After deletion, cup size: {cutting.cup}')



## 4. Self Argument

# class ChaiCup:
#     size = 150 # in ml

#     def describe(self):
#         return f'A {self.size} ml chai cup'

# cup = ChaiCup()

# print(cup.describe())
# # print(ChaiCup.describe()) # Generates exception
# print(ChaiCup.describe(cup))

# cup2 = ChaiCup()
# cup2.size = 100
# print(ChaiCup.describe(cup2))



## 5. Constructor and Init

# class ChaiOrder:

#     def __init__(self, type_, size):
#         self.type = type_
#         self.size = size

#     def summary(self):
#         return f'{self.size} ml of {self.type} chai'
    

# order = ChaiOrder('Masala', 200)
# print(order.summary())

# order_two = ChaiOrder('Ginger', 220)
# print(order_two.summary())



## 6. Inheritance and Composition

# class BaseChai:
#     def __init__(self, type_):
#         self.type = type_

#     def prepare(self):
#         print(f'Preparing {self.type} chai....')

    
# class MasalaChai(BaseChai):

#     def add_spices(self):
#         print(f'Adding cardamom, ginger, cloves....')


# class ChaiShop:
#     chai_cls = BaseChai # Composition, 

#     def __init__(self):
#         self.chai = self.chai_cls('Regular')

#     def serve(self):
#         print(f'Serving {self.chai.type} chai in the shop')   
#         self.chai.prepare()

# class FancyChaiShop(ChaiShop):
#     chai_cls = MasalaChai


# shop = ChaiShop()
# fancy = FancyChaiShop()
# shop.serve()
# fancy.serve()
# # fancy.chai_cls.add_spices() # error
# fancy.chai_cls.add_spices(fancy.chai) # works
# fancy.chai.add_spices(fancy.chai) # works


## 7. 3 Ways to Access Base Class 

# 1. Code Duplicaton - avoid this
# 2. Explicit call
# 3. using super()

class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength



# Code Duplication
# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         self.type = type_  # Code Duplication
#         self.strength = strength  # Code Duplication
#         self.spice_level = spice_level


# Using Explicit Call to BaseClass
# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength) # Explicit Call
#         self.spice_level = spice_level


# Using super()
# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         super().__init__(type_, strength)
#         self.spice_level = spice_level

# chai = GingerChai('Masala Chai', 'Hard', 'Low')
# print(chai.type)
# print(chai.strength)
# print(chai.spice_level)


## 8. Method Resolution Order (MRO):

class A:
    label = 'A: Base Class'

class B(A):
    label = 'B: Masala Blend'

class C(A):
    label = 'C: Herbal Blend'

class D(B, C):
    pass

# cup = D()
# print(cup.label)
# print(D.__mro__)

## 9. Static Methods

# class ChaiUtils:
#     @staticmethod
#     def clean_ingredients(text):
#         return [item.strip() for item in text.split(',')]


# text = 'Water, milk , ginger , chai'
# utils = ChaiUtils()

# result = ChaiUtils.clean_ingredients(text)
# # result = utils.clean_ingredients(text) # Error  
# print(result)


## 10. ClassMethod vs StaticMethod

class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['tea_type'],
            order_data['sweetness'],
            order_data['size']
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split('-')
        return cls(tea_type, sweetness, size)

class ChaiUtils:

    @staticmethod
    def is_valid_size(size):
        return size in ['Small', 'Medium', 'Large']

# print(ChaiUtils.is_valid_size('Medium'))
# print(ChaiUtils.is_valid_size('Extra-Large'))


order1 = ChaiOrder.from_dict({'tea_type': 'masala', 'sweetness': 'low', 'size': 'small'})
order2 = ChaiOrder.from_string('ginger-high-medium')
order3 = ChaiOrder('lemon tea', 'no', 'large')
# print(order1.size)

# print(order3.__dict__)
# print(order3.__dict__)

## 11. Property Decorartor:

class TeaLeaf:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError('Tea leaf age must be between 1 and 5 years')
    
leaf = TeaLeaf(10)
print(leaf.age)
leaf.age = 12
print(leaf.age)