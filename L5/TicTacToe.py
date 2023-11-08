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
        return setMarimeTabla()
    
def selectiePozitie(tabla, simbolJucator, marimeTabla) -> int:
    print(f'Jucătorul {simbolJucator} alege pozitia.')
    pozitie = int(input('Alegeți o poziție: '))

    if pozitie <= 0 or pozitie > marimeTabla * marimeTabla or tabla[pozitie - 1] !=
     print('Pozitia aleasa este indisponibila.)
     return selectiePozitie(tabla, simbolJucator,marimeTabla

    return pozitie

def algVerificareLinii(ListPozitii):
    if listPozitii ._ contains (_') == False: #excludereo cozulut in care pe pozitiile toblei se goseste simbolul
       for index in range(0, len(listPozitii) - 1):
           if index + 1 != marimeTabla - 1: #exctudereo cozulut in core index este ta capatul Listet
              if listPozitii[index] |= listPozitii[index + 1]: #daca doua pozitii sunt diferite ca, caracter, nu mai are rost sa continue Loop uL
                    break
        else
            if listPozitii[index] listPozitii[index + 1]:              #daca verificarea ajunge la final, inseamna ca pozitiile din Lista au acelasi
               return 1                                                #caracter si se returneaza 1 care mancheaza incheterea joculut


def creareList(startIndex, maxIndex increment, tabla):
    listPozitii = []
    index = startIndex

    #while index < moxIndex:
    for pas in range(0, maxIndex):
        listPozitii.append(tabla[index])
        index += increment

    return listPozitii


def verificareCastigator(tabla, marimeTabla)-> bool:
    #verificore lintilor
    for linie in range(0, marimeTabla):
        #creez o lista cu caracterele de pe liniamn
        listPozitii =crearelist(linie * marimeTabla, marimeTabla, 1 , tabla)
        #TODO: folosit doar pentru afisarea continutului listei la verificarea Lintilor
        print(f'Linii verticale: {listPozitii}*)
        #verificare daca pe Linia n este aceasi secventa de caractere
        if algVerificareLinii(listPozitii) == 1: return True

    #verificarea coloanelor
    for coloana in range(0, marimeTabla):
        #crearea Listei cu cdracterele de pe coloana n
        listPozitii = creareList(coloana, marimeTabla, marimeTabla, tabla)
        #TODO: folosit doar pentru afisarea continutulut array utut la verificarea tintilor
        print(f'Linii orizontale: {listPozitii}')
        #verificare daca pe coloana n este aceeasi secventa de caractere
        if algVerificareLinii(listPozitii) == 1: return True

    #verificane diagonata principata
    #crearea Listei cu caracterele de pe diagonala principala
    listPozitii = creareList(0, marimeTabla, marimeTabla + 1, tabla)
    #TODO: folosit doar pentru ofisareo continutului array ului la verificarea Lintilor
    print(f'Linii diagonala principala: {listPozitii}')
    #verificare daca pe diagonala principala este aceasi secventa de caractere
    if algVerificareLinii(listPozitii) == 1: return True

    #verificane diagonala secundara
                

