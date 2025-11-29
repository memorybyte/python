"""Running external programs"""

import subprocess

# The subprocess module in Python allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. 
# It is used to run external commands or programs from within a Python script.

# completed = subprocess.run(['ls', '-la'])
# # ls is the command, -la is the arguments to the ls

# print(f'Type: {type(completed)}')
# print(f'Args: {completed.args}')
# print(f'stderr: {completed.stderr}') # 0: success, any non-zero value indicates error
# print(f'stdout: {completed.stdout}') # we are not capturing the output, it is directly printed on the terminal
# print(f'returncode: {completed.returncode}')


# completed = subprocess.run(['ls', '-la'], capture_output=True, text=True)
# # capture_output = True -> output is available in stdout
# # output that is captured is in binary format
# # text = True -> indicates that the output should be in text format
# print(f'Args: {completed.args}')
# print(f'stderr: {completed.stderr}')
# print(f'returncode: {completed.returncode}')
# print(f'\nstdout: {completed.stdout}\n')


## Run another python script
# completed = subprocess.run(['python3', 'other.py'], capture_output=True, text=True)
# completed = subprocess.run(['python', 'other.py'], capture_output=True, text=True)
# print(f'Args: {completed.args}')
# print(f'stderr: {completed.stderr}')
# print(f'returncode: {completed.returncode}')
# print(f'\nstdout: {completed.stdout}\n')



## If there is an error while running commands or scripts
try:
    completed = subprocess.run(['false'], 
                               capture_output=True, 
                               text=True,
                               check=True # raises exception if subprocess there is an error, returncode is not 0.
                               )
    print(f'Args: {completed.args}')
    print(f'stderr: {completed.stderr}')
    print(f'returncode: {completed.returncode}')
    print(f'\nstdout: {completed.stdout}\n')
except subprocess.CalledProcessError as ex:
    print(ex)