import mysql.connector

class sql_connector:
    def __init__(self, host_string, user_name, password, database):
        self.connection_strings = mysql.connector.connect(
        host=host_string,
        user=user_name,
        password=password,
        database=database)
    
    def insert_history (self, sql_querry, timestamp, command):
        with self.connection_strings.cursor() as cursor:
            cursor.execute(sql_querry, (timestamp, command, ))
            self.connection_strings.commit()

    def get_max_timeframe(self, sql_query):
        with self.connection_strings.cursor() as cursor:
            cursor.execute(sql_query)
            data = cursor.fetchone()
        return str(data[0])
    
    def get_exists(self, sql_query):
        with self.connection_strings.cursor() as cursor:
            cursor.execute(sql_query)
            exists = cursor.fetchone()[0]
        return exists
