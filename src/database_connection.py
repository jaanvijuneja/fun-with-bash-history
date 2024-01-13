import mysql.connector

def insert_history (host, user, password, database, sql_querry, timestamp, command):
    connection_string = mysql.connector.connect (
        host = host,
        user = user,
        password = password,
        database = database        
        )
    
    with connection_string.cursor() as cursor:
        cursor.execute(sql_querry, (timestamp, command, ))
        connection_string.commit()