from multiprocessing import Process, Value
import time

def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value +=1 


if __name__ == '__main__':
    counter = Value('i', 0) # has inbuilt lock

    processes = [
        Process(target=increment, args=(counter,)) for _ in range(4)
    ]
    [process.start() for process in processes]
    [process.join() for process in processes]

    print(f'Final counter value: {counter.value}')