
## Method 01: (Not pythonic solution)
# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price
    
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError('Price cannot be negative.')
#         self.__price = value
        
# product = Product(-50)



## Method 02
# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price
    
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError('Price cannot be negative.')
#         self.__price = value

#     # After defining these two attributes, define an ideal class attribute
#     # built-in property() function, takes 4 parameters, all are optional
#     price = property(get_price, set_price)

# product = Product(10)
# print(product.price)
# product.price = -10 # error

# Still, ouside get_price and set_price are accessible

    


## Method 03
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value

product = Product(10)
print(product.price)
# product.price = -10

# While defining proeprties, we do not need to define the getter and setter always
# We can have read-only property by no having the setter