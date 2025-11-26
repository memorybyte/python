class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')

class Mammal(Animal):
    def walk(self):
        print('walk')

class Fish(Animal):
    def swim(self):
        print('walk')

# m = Mammal()
# m.eat()
# print(m.age)


# A goog example of Inheritance

class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open.')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed.')
        self.opened = False
    

class FileStream(Stream):
    def read(self):
        print('Reading data from file...')

class NetworkStream(Stream):
    def read(self):
        print('Reading data from network...')