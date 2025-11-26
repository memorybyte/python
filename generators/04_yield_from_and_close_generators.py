## yield from

# yield from is used to flatten and combine the outputs of multiple generators into a single sequence

# It is a concise way to yield all values from another iterable or generator and to delegate generator control flow.

def local_chai():
    yield 'Masala Chai'
    yield 'Ginger Chai'

def imported_chai():
    yield 'Matcha'
    yield 'Oolong'

def full_menu():
    yield from local_chai()
    yield from imported_chai()

# for chai in full_menu():
#     print(chai)

# Creates a sub-iterator from the generator you specify (e.g., local_chai()).

# Iterates through each value from the sub-iterator, yielding them one by one to the caller of full_menu().

# After the first sub-iterator is exhausted, it moves to the next yield from (here, imported_chai()), and repeats the process.

# Handles two-way communication: If the caller sends values or exceptions, they are forwarded to the sub-generator.


## close()

# The close() function on a generator is used to stop the generator and clean up resources.

# What happens when you call generator.close()?

# It raises a GeneratorExit exception inside the generator at the current yield.

# The generator can handle this exception (usually in a try...except or finally block) to perform cleanup.

# After close() is called, further calls to next() or send() will raise StopIteration.

# Typical use cases:
# To stop a generator early (before it is exhausted).
# To trigger cleanup code inside the generator (like closing files or releasing resources).

def chai_stall():
    try:
        while True:
            order = yield 'Waiting for Chai Order'
            print(order)
    except:
        print('Stall Closed, No more chai')

stall = chai_stall()
print(next(stall))
stall.send('Hi')
stall.close()