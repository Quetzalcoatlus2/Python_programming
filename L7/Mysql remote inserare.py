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
       user = input("user:")
       mesaj = input("mesaj:")


       query = "INSERT INTO python2023 (user, mesaj) VALUES (%s, %s);"
       values = (user, mesaj)
       cursor.execute(query, values)
       connection.commit()
       #record = cursor.fetchone()
       print("You're connected to database!")#, record)


except Error as e:
   print("Error while connecting to MySQL", e)
finally:
   if connection.is_connected():
       cursor.close()
       connection.close()
       print("MySQL connection is closed")