print("Introduceți latura tablei (3, 5 sau 7):")
nr = int(input())
nr_rez = nr
str = " "
print("Ați selectat tabla de joc de dimensiuni", nr, "X", nr)
while nr != 0:
    rez = nr_rez
    while rez != 0:
        str = str + "0 "
        rez -= 1
    else:
        print(str)
        nr -= 1
        str = " "