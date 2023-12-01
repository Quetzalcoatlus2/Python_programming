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
       #cursor.execute("select database();")
       query = """SELECT * FROM noteTAD;"""
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
print("MySQL connection is closed")