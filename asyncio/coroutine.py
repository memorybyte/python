import asyncio

# Define the coroutine function
# When we call coroutine function, it returns a coroutine object
async def main():
    await asyncio.sleep(10)
    print('Start of main coroutine')

# Simply calling the async function does not give the result.
# When we simply call main(), it generates a coroutine object, which is to be awaited to generate to get the result of its execution. 
# It has to be awaited.

# print(main()) # returns a coroutine object

# await keyword:
# It is used inside an async function to pause the execution of the coroutine until the awaited coroutine or awaitable completes.
# When you use await inside an async function, the function stops running at that point and waits for the thing you are awaiting (like another coroutine or an async operation) to finish.
# While waiting, the event loop can run other tasks.
# Once the awaited operation is done, the function continues from where it paused.

# Where to use await keyword:
# You should use the await keyword whenever you call a function that is asynchronous (an async def function) or returns an awaitable object.
# If a function is defined with async def, you must use await when calling it (inside another async function).
# If a function returns an awaitable (like asyncio.sleep(), asyncio.gather(), or an async HTTP request), use await.
# Do not use await with regular (non-async) functions.


# awaitable object:
# An awaitable object is anything that can be used with the await keyword in an async function.
# There are three main types of awaitable objects in Python:
#   1. Coroutines: Functions defined with async def and called (e.g., main()).
#   2. Tasks: Objects created by scheduling coroutines (e.g., with asyncio.create_task()).
#   3. Futures: Low-level objects representing a result that may not be available yet (e.g., asyncio.Future).

# Run the main coroutine
# asyncio.run(main())

# The run() method expects a coroutine object
# We get a coroutine object by calling an async function, but not awaiting it. Example: main(), not await main()
# We do not get a coroutine object by just referencing it (main), we must call it (main())

# asyncio.run() does the following:
# 1. It creates a new event loop: it sets up a fresh asyncio loop.
# 2. Schedules the coroutine: it schedules the main() coroutine to run on that event loop.
# 3. Runs the event loop: It starts the event loop and runs it until the main() coroutine completes.
# 4. Closes the event loop: After the coroutine finishes, it closes the event  loop and cleans up resources.

# If we don't pass anything to asyncio.run(), we will get a TypeError(). run() requires a coroutine object.
# run() accepts only single coroutine object.
# To run multiple coroutines, we should use asyncio.gather() inside the main coroutine and the main coroutine object has to be passes to the asyncio.run()


# Example:
async def task1():
    print('Task 1')
    await asyncio.sleep(4)
    return 'Completed task 1'

async def task2():
    print('Task 2')
    await asyncio.sleep(2)
    return 'Completed task 2'

async def collector():
    results = await asyncio.gather(task1(), task2())
    # results = await asyncio.gather(*[task1(), task2()])

    for result in results:
        print(result)

# asyncio.gather():
# It is used to run multiple coroutine objects concurrently
# It schedules all the given coroutines to run at the same time and waits until all of them are finished.
# It returns the results of all coroutines as a list in the order they were passes.

# results = asyncio.run(collector())


# Note:
# If we write multiple asyncio.run() calls (each with a coroutine object), they will run sychronously, one after another.
# For example:
#   asyncio.run(coro1())
#   asyncio.run(coro2())
# Here, coro1() will finish completely before coro2() starts.
# Each, asyncio.run() creates and closes its own event loop, so they do not run concurrently.


## AWAIT
# Examples with await

# Example 01
# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print('Fetching data...')
    await asyncio.sleep(delay) # Simulate an I/O operation with sleep
    print('Data fetched')
    return {'data': 'some data'} # return some data

# Define another coroutine that calls the first coroutine
async def main2():
    print('Start of main coroutine')
    task = fetch_data(2) # coroutine object, it has to be awaited. It is not executed yet. It is executed only when it is awaited
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print(f'Received data: {result}')
    print('End of main coroutine')

# Run the main coroutine
# asyncio.run(main2())

# Example 02
# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f'Fetching data... id:{id}')
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print(f'Data fetched... id:{id}')
    return {'data': 'Some data', 'id': id} # Return some data

# Define another coroutine that calls 
async def main3():
    task1 = fetch_data(2, 1) # Returned a coroutine object, it has to be awaited to execute
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f'Received result: {result1}')

    result2 = await task2
    print(f'Received result: {result2}')

# Run the main coroutine
# asyncio.run(main())

# In the above program, first task1 is executed, then task2 is executed.
# It is because, when await keyword is encountered, execution stops.
# Once task1 completes its task, then only task2 continues.
# So in total it takes 4 secs. Although these two tasks are asynchronous, these are not started simultaneously. One finishesm then next one starts.


# TASKS
# We can use asyncio.create_task()
# When we call asyncio.create_task() with a coroutine object, we are scheduling the coroutine to run as a Task on the event loop IMMEDIATELY. Unlike the previous code, where one task waits for previous one to complete.

# Benefits of using create_task()
# 1. Concurrency: Multiple coroutines can run at the same time, making better use of waiting periods (like I/O or sleep).
# 2. Immediate scheduling: Tasks start running as soon as they are created, even before you await them.
# 3. Control: You get a Task object, which you can await later, cancel, or check its status.

# Example: 03

async def fetch_data2(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data.')
    await asyncio.sleep(sleep_time)
    # my_input = input(f'Input for {id}: ')
    return {'id': id, 'data': f'Sample data from coroutine {id}'}

async def main3():
    # Create task for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data2(1, 5))
    task2 = asyncio.create_task(fetch_data2(2, 1))
    task3 = asyncio.create_task(fetch_data2(3, 5))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

# asyncio.run(main3())

# In the above code, BTS (Behind the scene):
# 1. All the three tasks task1, task2 and task3 start running concurrently as soon as they are created.
# 2. The event loop manages these tasks, switching between them as they await (for example during await asyncio.sleep(delay))

# One thing to note that, the tasks start executing as soon as they are created using create_task(), even before we await them.

# So, all three starts executing
# Next, the line result1 = await tasks1 is encountered. It waits there until the execution of task1 finishes. It may happen that task1 finishes last. Even if task2 and task3 finishes earlier, it waits at result1 to  get the results and after getting the result it goes to next line which is result2 = await task2, and so on. 
# Only after all three results are available does the code reach last line which is print(result1, result2, result3)

# So if we alter the order of the statements, it may become synchronous for few tasks( i.e. one or sets of tasks completes then another sets of tasks executes)
# For example:
async def collector2():
    # Create task for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data2(1, 5))
    task2 = asyncio.create_task(fetch_data2(2, 1))

    result1 = await task1
    result2 = await task2

    # Here, first two tasks task1 and task2 executes and finishes
    # Then only task3 is schedules.
    # It is because the task3 is created below and program execution halts at result1 = await task1 and does not proceed until task1 finishes and then task2

    task3 = asyncio.create_task(fetch_data2(3, 5))

    result3 = await task3

    print(result1, result2, result3)


# GATHER:
# asyncio.gather()
# It  runs multiple coroutine objects concurrently.
# It schedules all the given coroutines to run at the same time and waits until all of them are finished.
# It returns a list of results, in the same order as the coroutines were passed. 

# Use create_task() to start a coroutine and get a Task object for more control.
# Use gather() to run several coroutines concurrently and collect their results easily.

# or 
# You can use them together:
# Often, you use create_task() to start tasks, then gather() to wait for all of them:

# Example of gather
async def main4():
    # Run coroutines concurrently and gather their retrun values
    results = await asyncio.gather(
        fetch_data2(1, 3),
        fetch_data2(2, 1),
        fetch_data2(3, 2),
    )

    # Another approach: first create tasks and then use gather
    # task1 = asyncio.create_task(fetch_data2(1, 3))
    # task2 = asyncio.create_task(fetch_data2(2, 1))
    # task3 = asyncio.create_task(fetch_data2(3, 2))
    # results = await asyncio.gather(task1, task2, task3)

    # Process the result
    for result in results:
        print(f'Received result: {result}')

# Run the main coroutine
# asyncio.run(main4())

# One thing note that:
# If any of the coroutine fails, other coroutine still executes.
# If some situations, this may not be intended as the state of the application may become unstable.
# gather() does not provide error handling 


# TASKGROUP
# asyncio.TaskGroup()
# It provides a structured way to manage and run multiple asynchronous tasks together.
# It allows you to start, monitor, and wait for a group of tasks as a single unit.
# If any task in the group fails (raises an exception), the TaskGroup will cancel all other running tasks in the group.
# It helps write safer and cleaner concurrent code, especially for error handling.

# Use TaskGroup when you want to manage a set of related tasks together, with automatic cleanup and error handling.

async def main5():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data2(i, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f'Received result: {result}')

# asyncio.run(main5())

# async with:
# The async with statement is used to work with asynchronous context managers in Python.

# What does it do:
# It enters an asynchronous context manager (an object that defines __aenter__ and __aexit__ methods).
# It allows you to perform setup and cleanup actions asynchronously.
# The code inside the async with block can use await and other async features.

# Why use async with  with TaskGroup:
# It ensures that all tasks created inside the block are properly managed.
# When the block exits, it waits for all tasks to finish and handles exceptions or cancellations as needed.
# It provides structured concurrency: if any task fails, all others are cancelled automatically.


# Futures:
# Futures are low-level awaitable objects in Python’s asyncio library that represent a result that may not be available yet.
# A Future acts as a placeholder for a value that will be set at some point in the future, usually by another coroutine or callback.
# You can await a Future to pause execution until its result is available.
# Futures are mostly used internally by asyncio, but you can create and use them for advanced asynchronous patterns.

# Example

async def set_future_result(future, value):
    await asyncio.sleep(2)

    # Set the result of the future
    future.set_result(value)
    print(f'Set the future"s result to: {value}')

async def main6():
    # Create a future object
    loop = asyncio.get_running_loop() # Get the current event loop
    future = loop.create_future() # Create a Future object (a placeholder for a result that will be set later.)

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, 'Future result is ready'))
    # Schedules the set_future_result coroutine to run in the background, which will set the future's result after 2 seconds.

    # Wait for the future's result
    result = await future # Waits (pauses) until the Future's result is set by
    print(f'Received the future"s result: {result}')

# asyncio.run(main6())

# This pattern is useful for advanced coordination between coroutines, where one coroutine waits for another to provide a result at some point in the future.

# why are we awaiting on the future
"""
 you are awaiting on the future instead of the task because the future acts as a placeholder for a result that will be set by another coroutine (set_future_result).

Here's what's happening:

You create a Future object (future = loop.create_future()).
You schedule a coroutine (set_future_result) that will set the result of this future after some time.
In your main coroutine, you await future, which pauses execution until the future's result is set (by future.set_result(value) in the other coroutine).
The task created by asyncio.create_task(set_future_result(...)) runs in the background and, after a delay, sets the result on the future.
Why not await the task?
If you awaited the task, you would get the return value of set_future_result (which is None), not the value set on the future.
By awaiting the future, you are waiting for the specific value that another coroutine will provide, which is useful for advanced coordination between coroutines.
"""


# SYNCHRONIZATION

# 1. Using Lock
shared_resource = 0

# An asyncio Lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical Section Starts
        print(f'Resource before initialization: {shared_resource}')
        shared_resource += 1 # Modify the shared resource
        await asyncio.sleep(1) # Simulate an IO Operation
        print(f'Resource after modification: {shared_resource}')
        # Critical Section Ends

async def main7():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

# asyncio.run(main7())
# 
# 

# 2. Using Semaphore: allows multiple coroutines to have access to the same object at the same time

async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f'Accessing resource {resource_id}')
        await asyncio.sleep(1) # Simulate work with the resource
        print(f'Releasing resource {resource_id}')

async def main8():
    semaphore = asyncio.Semaphore(2) # Allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

# asyncio.run(main8())

# 3. Event
# This pattern is useful for coordinating coroutines—waiter waits for a signal from setter before continuing.
async def waiter(event):
    print('Waiting for the event to be set')
    await event.wait()
    print('Event has been set, continuing execution.')

async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print('Event has been set!')

async def main9():
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event),
        setter(event)
    )


"""
async def waiter(event):

Prints "Waiting for the event to be set".
await event.wait() pauses until the event is set by another coroutine.
After the event is set, prints "Event has been set, continuing execution."

async def setter(event):

Waits 2 seconds (await asyncio.sleep(2)) to simulate some work.
Calls event.set(), which unblocks any coroutines waiting on the event.
"""

asyncio.run(main9())