## Send Value to Generator:

# How .send(value) works
# 1. .send(value) resumes the generator
# 2. The value becomes the result of the yield expression
# 3. Generator continues until next yield
# 4. Returns the yielded value (if any)

# Rules:
# 1. Must prime first: Call next(gen) before first .send() (except send(None))
# 2. yield is an expression: Can receive and return values
# 3. send(None) is equivalent to next()


def chai_customer():
    print('Welcome ! What chai would you like ?')

    order = yield 'Input: ' # Pauses and waits for a value
    while True:
        print(f'Preparing: {order}')
        order = yield 'Input: '# Pauses and waits for a value

    # while True:
    #     order = yield
    #     print(f'Preparing: {order}')


stall = chai_customer()

print(next(stall)) # Start the generator
print(stall.send('Masala Chai'))
# print(stall.send('Ginger Chai'))
# print(next(stall))
# print(stall.send('Elaichi Chai'))


def demo():
    x = yield "first"
    print(f"Got: {x}")
    y = yield "second"
    print(f"Got: {y}")

# gen = demo()
# print(next(gen))        # "first" (prime)
# print(gen.send(100))    # Prints "Got: 100", returns "second"
# gen.send(200)           # Prints "Got: 200", raises StopIteration

