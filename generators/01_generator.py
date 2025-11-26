## Generators:

# 1. Creation: Calling a generator function returns a generator object (doesn't execute the function)

# 2. First next(): Execution starts, runs until first yield, returns value and pauses

# 3. Subsequent next(): Resumes from last pause point, continues until next yield

# 4. Completion: When function ends, raises StopIteration exception

# - State Preservation: Local variables and execution position are saved between yields 
# - Lazy Evaluation: Values computed only when requested
# - Memory Efficient: Only one value in memory at a time(vs lists stroring all values)


def serve_chai():
    yield 'Cup 1: Masala Chai'
    yield 'Cup 2: Ginger Chai'
    yield 'Cup 3: Elaichi Chai'

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ['Cup 1', 'Cup 2', 'Cup 3']

# Generator Function
def get_chai_gen():
    yield 'Cup 1'
    yield 'Cup 2'
    yield 'Cup 3'

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))