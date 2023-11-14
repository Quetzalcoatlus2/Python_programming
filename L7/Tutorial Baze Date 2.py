import sqlite3


#conn = None
conn = sqlite3.connect(r"C:\Users\teodo\Desktop\SQLite\db1.db")
      


cursor=conn.cursor()
cursor.execute("select * from users;")
rezultat = cursor.fetchall()




listaUseri = []
for row in rezultat:
   listaUseri.append(row[1])




print(listaUseri)


account = input("username:")


#verific daca usernameul exista
if account not in listaUseri:
   print("error")
else:
   password = input("pass:")




conn.close()
