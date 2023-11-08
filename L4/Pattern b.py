print("Introduceți un numar:")
nr = int(input())
nr_rez = nr
str = " "
while nr != 0:
    rez = nr 
    while rez != 0:
        str = str + "# "
        rez -= 1
    else:
        print(str)
        nr -= 1
        str = " "