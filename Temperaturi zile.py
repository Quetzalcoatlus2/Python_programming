#Vom considera un program care va prelucra temperaturile medii pentru fiecare oră din cele 31 de zile ale unei luni.
#Se va crea o matrice cu 31 linii și 24 coloane.
#Considerăm că temperaturile sunt scrise de către un alt proces care măsoară temperaturile respective.
#temps = [[0.0 for h in range(24)] for d in range(31)]
#prima cerință este să determinați temperatura medie de la prânz pentru întreaga lună
#determinați cea mai înaltă temperatură medie pentru întreaga lună
#numărați câte zile au avut temperatura medie peste 20 de grade  
import random

temps = [[random.randint(0, 35) for h in range(24)] for d in range(31)]

print(temps)

for i in range(31):
    print("Temperatura medie de la pranz pentru ziua", i+1, "este", temps[i][11])
max=10
for i in range(31):
    for j in range(24):
        if temps[i][j] > max:
            max= temps[i][j]

print(max)
temp=0
count=0
for i in range(31):
    for j in range(24):
        temp+=temps[i][j]
    temp/=24
    if temp>20:
        count+=1
    temp=0

print(count)