import threading
import time

def boil_milk():
    print(f'Boiling milk...')
    time.sleep(2)
    print(f'Milk boiled...')

def toast_bun():
    print(f'Toasting bun...')
    time.sleep(3)
    print(f'Done with bun toast...')

# Here, we have one single thread 'main'.
# First boil_milk() is run
# Then toast_bun() is run
# boil_milk()
# toast_bun()

# Create thread
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)
# Here, we just created the thread

start = time.time()

# Start the thread
t1.start()
t2.start()

# Wait for all thread to finish
t1.join()
t2.join()

end = time.time()

print(f'Breakfast is ready in {end - start:.2f}')
