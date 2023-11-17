import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                         database='sql11662854',
                                         user='sql11662854',
                                         password='USx5upjQ3R')
   if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL Server version ", db_Info)
       cursor = connection.cursor()
       #cursor.execute("select database();")
       query = """SELECT * FROM python2023;"""
       cursor.execute(query)
       record = cursor.fetchall()
       print(record)
       for row in record:
           print(row[1],(row[3] + row[4])/2)


except Error as e:
   print("Error while connecting to MySQL", e)
finally:
   if connection.is_connected():
       cursor.close()
       connection.close()