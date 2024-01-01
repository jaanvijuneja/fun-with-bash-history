import os

history_file_path = os.path.expanduser('~/.bash_history')

if os.path.exists(history_file_path):
    with open(history_file_path, 'r') as file:
        history = file.readlines()



for data in history:
    print(data)
