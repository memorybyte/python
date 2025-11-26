chai_menu = {'masala': 30, 'ginger': 40}

# print(chai_menu['elaichi']) # KeyError

try:
    print(chai_menu['elaichi'])
except KeyError:
    print('The key that you are trying to access does not exists')


def serve_chai(flavor):
    try:
        print(f'Preparing {flavor} chai...')
        if flavor == 'unknown':
            raise ValueError('We do not know that falvor')
    except ValueError as e:
        print(f'Error: {e}')
    else: # Exexutes only if there is no exception
        print(f'{flavor} chai is served')
    finally: # Always executes
        print('Next customer please.')

# serve_chai('Masala')
# serve_chai('unknown')


# Example 01

# try:
#     age = int(input('Age: '))
# except ValueError as ex:
#     print(type(ex))
#     print("You didn't enter a valid age.")
#     print('Error: ', ex)
# else: # This block executes if no execption were thrown
#       # Similar to for...else loop, where else block executes if there are no break statement execution
#     print(f'No Exception were thrown')
# print(f'Execution continues')


# Example 02

# try:
#     age = int(input('Age: '))
#     xfactor = 10 / age
# # except ValueError as ex:
# #     # print(type(ex))
# #     # print('Error: ', ex)
# #     print("You didn't enter a valid age.")
# # except ZeroDivisionError:
# #     print('Age can not be zero.')
# except (ValueError, ZeroDivisionError): 
#     print("You didn't enter a valid age.")
# else: # This block executes if no execption were thrown
#       # Similar to for...else loop, where else block executes if there are no break statement execution
#     print(f'No Exception were thrown')
# print(f'Execution continues')


# Example 03

# try:
#     file = open('order.txt', 'w')
#     age = int(input('Age: '))
#     xfactor = 10 / age 
#     # file.close() # will not execute if there is exception, use finally clause
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print('No exception were thrown.')
# finally:
#     print('Closing file...')
#     file.close()
#     print('File closed...')

# print('Execution Continues')



# Example 04: with statement

# If an object has __enter__ and __exit__, 
# then that object supports context management protocol

try:
    with  open('order.txt', 'w') as file:
        print('File opened')

    age = int(input('Age: '))
    xfactor = 10 / age 
    # file.close() # will not execute if there is exception, use finally clause
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print('No exception were thrown.')
finally:
    pass # No need to close file in finally block
         # if we are opening file with 'with' clause

    # print('Closing file...')
    # file.close()
    # print('File closed...')

print('Execution Continues')