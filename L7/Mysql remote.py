import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                         database='sql11405875',
                                         user='sql11405875',
                                         password='GcWhwdfA6a')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        query = '''CREATE TABLE noteTAD (
        id  INTEGER NOT NULL PRIMARY KEY UNIQUE,
        nume    TEXT,
        prenume TEXT,
        n1  INTEGER,
        n2  INTEGER
        );'''
        cursor.execute(query)
        print("Table created successfully.")
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed") 