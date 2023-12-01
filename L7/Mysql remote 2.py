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
       nume = input("numele:")
       prenume = input("prenumele:")
       nota1 = int(input("nota1: "))
       nota2 = int(input("nota2: "))


       query = "INSERT INTO noteTAD (nume, prenume, n1, n2) VALUES (%s, %s, %s, %s);"
       values = (nume, prenume, nota1, nota2)
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