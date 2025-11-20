import threading
import time

def prepare_chai(name, wait_time):
    print(f'{name} chai brewing...')
    time.sleep(wait_time)
    print(f'{name} chai: Ready.')

# Create thread
t1 = threading.Thread(target=prepare_chai, args=('Masala', 6))
t2 = threading.Thread(target=prepare_chai, args=('Ginger', 2))

start = time.time()

# Start the thread
t1.start()
t2.start()

# Wait for all thread to finish
t1.join()
t2.join()

end = time.time()

print(f'Total time taken {end - start:.2f}')
