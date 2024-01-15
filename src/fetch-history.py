import os
from database_connection import sql_connector

localhost = '127.0.0.1'
username = 'root'
password = 'Secret55'
database = 'store_history_bash'

mysql_connector = sql_connector(localhost, username, password, database)

history_file_path = os.path.expanduser('~/.bash_history')

if os.path.exists(history_file_path):
    with open(history_file_path, 'r') as file:
        history = file.readlines()

cleaned_history = []
for item in history:
    cleaned_history.append(item.strip())

history_list = []

sql_querry_to_check_table = f"""
select EXISTS(select id FROM user_history LIMIT 1);
"""

exists = mysql_connector.get_exists(sql_querry_to_check_table)

if exists:

    sql_querry_max_timestamp = f"""
    select max(unix_timestamp) from user_history
    """
    
    result_max_timestamp = mysql_connector.get_max_timeframe(sql_querry_max_timestamp)
    
    max_timestamp = "#" + result_max_timestamp


    for i in range(len(cleaned_history)):
        if max_timestamp == cleaned_history[i]:
            if cleaned_history[i].startswith('#') and len(cleaned_history[i]) == 11:
                inner_list = cleaned_history[i][1:], cleaned_history[i+1]
                history_list.append(inner_list)

else:
        for i in range(len(cleaned_history)):
            if cleaned_history[i].startswith('#') and len(cleaned_history[i]) == 11:
                inner_list = cleaned_history[i][1:], cleaned_history[i+1]
                history_list.append(inner_list)



for timestamp, command in history_list:
    sql_querry = f"""
    insert into user_history (unix_timestamp, command, system_timestamp, user) VALUES (%s, %s, FROM_UNIXTIME(unix_timestamp), 'jaanvi')
    """
    mysql_connector.insert_history(sql_querry, timestamp, command)
