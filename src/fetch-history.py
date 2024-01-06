import os
import database_connection

localhost = '127.0.0.1'
username = 'root'
password = 'Secret55'
database = 'store_history_bash'

history_file_path = os.path.expanduser('~/.bash_history')

if os.path.exists(history_file_path):
    with open(history_file_path, 'r') as file:
        history = file.readlines()



for data in history:
    sql_querry = f"""
    insert into user_history (history, user) VALUES (%s, 'jaanvi')
    """
    database_connection.insert_history(localhost, username, password, database, sql_querry, data)
