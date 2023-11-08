def afisareTabla(tabla):
    linieNoua = 0
    for poz in tabla:
        print(poz, end=' ')
        if linieNoua == marimeTabla - 1:
            print()
            linieNoua = -1
        linieNoua += 1
 
def setMarimeTabla() -> int:
    marime = int(input('Marime: '))

    if marime % 2 != 0 and marime >= 3:
        return marime
    else:
        print('Mărimea nu a fost introdusă corect.\nIntroduceți un număr impar mai mare sau egal cu 3.')