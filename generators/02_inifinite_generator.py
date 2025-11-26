## INIFINITE GENERATOR:
# An infinite generator is a generator that produces values indefinitely without ever stopping. 

# It has no end condition, so it will keep yielding values forever (or until manually stopped).

# Must control consumption: Use break, limits, or conditions to stop iteration

# Memory efficient: Only current value in memory despite being infinite

# Useful for: Streams, events, continuous monitoring, ID generation

## Never convert infinite generators to lists (list(infinite_gen())) - it will run forever and crash.

def infinite_chai():
    count = 1
    while True:
        yield f'Refill #{count}'
        count += 1
    
user1 = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(user1))

for _ in range(10):
    print(next(user1))

# DO NOT RUN THIS: INFINITE 
# for value in user1:
#     print(value)