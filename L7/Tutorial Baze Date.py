import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(sqlite3.version)
       cursor=conn.cursor()
       cursor.execute("select * from users;")
       print(__name__)
       print(cursor.fetchall())

   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()


if __name__ == '__main__':
   create_connection(r"C:\Users\teodo\Desktop\SQLite\db1.db")







