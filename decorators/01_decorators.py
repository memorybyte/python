## Decorators

from functools import wraps

def my_decorators(func):
    @wraps(func) # To preserve the function metadata
    def wrapper():
        print(f'Before function runs')
        func()
        print(f'After function runs')
    
    return wrapper

@my_decorators
def greet():
    print(f'Hello from decorators class from World')

greet()

print(greet.__name__)