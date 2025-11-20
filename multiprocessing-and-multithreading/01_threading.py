import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f'Taking order for #{i}')
        time.sleep(10)

def brew_chai():
    for i in range(1, 4):
        print(f'Brewing chai for #{i}')
        time.sleep(12)

# Create thread
t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=brew_chai)

# Start the thread 
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print(f'All orders taken and chai brewed')


# What is happening:
#
#
#
#
#
#
#
#