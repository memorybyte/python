import threading
import time

def brew_chai():
    print(f'{threading.current_thread().name} started the brewing process...')
    count = 0
    for _ in range(100_000_000):
        count += 1

    print(f'{threading.current_thread().name} finished the brewing process...')

t1 = threading.Thread(target=brew_chai)
t2 = threading.Thread(target=brew_chai)

start = time.time()

t1.start()
t2.start()


t1.join()
t2.join()

end = time.time()

print(f'Total time taken: {end - start:.2f}')