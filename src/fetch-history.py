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

cleaned_history = []
for item in history:
    cleaned_history.append(item.strip())

history_list = []
        
for i in range(len(cleaned_history)):
    if cleaned_history[i].startswith('#') and len(cleaned_history[i]) == 11:
        inner_list = cleaned_history[i][1:], cleaned_history[i+1]
        history_list.append(inner_list)
sql_querry = f"""
select max(unix_timestamp) from user_history
"""

for timestamp, command in history_list:
    sql_querry = f"""
    insert into user_history (unix_timestamp, command, system_timestamp, user) VALUES (%s, %s, FROM_UNIXTIME(unix_timestamp), 'jaanvi')
    """
    database_connection.insert_history(localhost, username, password, database, sql_querry, timestamp, command)
