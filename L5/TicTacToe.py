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

    if pozitie <= 0 or pozitie > marimeTabla * marimeTabla or tabla[pozitie - 1] != '_':
        print('Poziția aleasă este indisponibilă.')
        return selectiePozitie(tabla, simbolJucator, marimeTabla)

    return pozitie

def algVerificareLinii(ListPozitii):
     if listPozitii.__contains__('_') == False: #excluderea cazului în care pe pozițiile tablei se găsește simbolul
        for index in range(0, len(listPozitii) - 1):
            if index + 1 != marimeTabla - 1: #excluderea cazului în care index este la capătul listei
                if listPozitii[index] != listPozitii[index + 1]: #dacă două poziții sunt diferite în ceea ce privește caracterele, nu mai are rost să continue bucla
                    break
            else:
                if listPozitii[index] listPozitii[index + 1]:              #dacă verificarea ajunge la final, înseamnă că pozițiile din listă au acelasi
               return 1                                                    #caracter și se returnează 1 care manchează încheierea jocului


def creareList(startIndex, maxIndex increment, tabla):
    listPozitii = []
    index = startIndex

    #while index < maxIndex:
    for pas in range(0, maxIndex):
        listPozitii.append(tabla[index])
        index += increment

    return listPozitii


def verificareCastigator(tabla, marimeTabla)-> bool:
    #verificarea liniilor
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

    #verificare diagonala secundara
    #crearea Listei cu caracterele de pe diagonata secundana
    listPozitii = creareList(marimeTabla - 1, marimeTabla, marimeTabla - 1, tabla)
    #TODO: folosit doar pentru afisarea continutului array ului la verificarea Lintilor
    print(f'Linii diagonala secundara: {listPozitii}')
    #verificore daca pe diagonala secundara este aceasi secventa de caractere
    if algVerificareLinii(listPozitii) == 1; return True

################################# DE AICI INCEPE JOCUL ###########################################0#
caracterTablaGoala = "_"
tabla = []

print('Marime decomandata: 3, 5, 7')
#initalizare marimea tablei
print('Specificati marimea tablei.")
marimeTabla = setMarimeTabla()

#Initializare tabla goala si afisarea ei
countPozitii = 0
for pozitie in range(0, marimeTabla * marimeTabla):
    print(caracterTablaGoala, end=" ")
    #ereorea orray ului pentru stocarea continututui toblet de joc
    tabla += caracterTablaGoala
    countPozitii += 1
    if(countPozitii == marimeTabla)
        print()
        countPozitii = 0

##stant jocm##
#progresloc = folosit sa numar etopele de joc
progresJoc = 0
jucator = ''
while progresJoc != marimeTabla * marimeTabla
    #alegereo pozititlor de catre jucatori
    if progresJoc % 2 == 0:
        #randul jucatorului x
        jucator = X'
        pozitie =selectiePozitie(tabla, jucator, marimeTabla)
        tabla[pozitie-1] = jucator

    else:
        #randul jucatorulut 0
        jucator = 0
        pozitie =selectiePozitie(tabla, jucator, marimeTabla)
        tabla[pozitie-1] = jucator

    #randore tabla de joc
    afisareTabla(tabla)

    #vertficare castigator
    if verificareCastigator(tabla, marimeTabla) == True:
        print(f'Felicitari! Jucatorul {jucator} a castigat.')
        break

progresJoc += 1

if progresJoc == marimeTabla * marimeTabla:
    print('Din păcate, nu a câștigat nimeni.')

