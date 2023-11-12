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
     if ListPozitii.__contains__('_') == False: #excluderea cazului în care pe pozițiile tablei se găsește simbolul
        for index in range(0, len(ListPozitii) - 1):
            if index + 1 != marimeTabla - 1: #excluderea cazului în care index este la capătul listei
                if ListPozitii[index] != ListPozitii[index + 1]: #dacă două poziții sunt diferite în ceea ce privește caracterele, nu mai are rost să continue bucla
                    break
            else:
                if ListPozitii[index] == ListPozitii[index + 1]:              #dacă verificarea ajunge la final, înseamnă că pozițiile din listă au acelasi
                    return 1                                                    #caracter și se returnează 1 care manchează încheierea jocului


def creareList(startIndex, maxIndex, increment, tabla):
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
        #creez o listă cu caracterele de pe linia n
        listPozitii = creareList(linie * marimeTabla, marimeTabla, 1 , tabla)
        #TODO: folosit doar pentru afișarea conținutului listei la verificarea liniilor
        print(f'Linii verticale: {listPozitii}')
        #verificare dacă pe linia n este aceeași secvență de caractere
        if algVerificareLinii(listPozitii) == 1: return True

    #verificarea coloanelor
    for coloana in range(0, marimeTabla):
        #crearea listei cu cdracterele de pe coloana n
        listPozitii = creareList(coloana, marimeTabla, marimeTabla, tabla)
        #TODO: folosit doar pentru afișarea conținutului array-ului la verificarea liniilor
        print(f'Linii orizontale: {listPozitii}')
        #verificare dacă pe coloana n este aceeași secvență de caractere
        if algVerificareLinii(listPozitii) == 1: return True

    #verificare diagonală principală
    #crearea listei cu caracterele de pe diagonala principală
    listPozitii = creareList(0, marimeTabla, marimeTabla + 1, tabla)
    #TODO: folosit doar pentru afișarea conținutului array-ului la verificarea liniilor
    print(f'Linii diagonala principala: {listPozitii}')
    #verificare dacă pe diagonala principală este aceeași secvență de caractere
    if algVerificareLinii(listPozitii) == 1: return True

    #verificare diagonală secundară
    #crearea listei cu caracterele de pe diagonala secundară
    listPozitii = creareList(marimeTabla - 1, marimeTabla, marimeTabla - 1, tabla)
    #TODO: folosit doar pentru afișarea conținutului array-ului la verificarea liniilor
    print(f'Linii diagonală secundară: {listPozitii}')
    #verificore daca pe diagonala secundara este aceasi secventa de caractere
    if algVerificareLinii(listPozitii) == 1: return True

################################# DE AICI INCEPE JOCUL ###########################################0#
caracterTablaGoala = "_"
tabla = []

print('Marime decomandata: 3, 5, 7')
#Inițializare mărime tablă
print('Specificați mărimea tablei:')
marimeTabla = setMarimeTabla()

#Inițializare tablă goală și afișarea ei
countPozitii = 0
for pozitie in range(0, marimeTabla * marimeTabla):
    print(caracterTablaGoala, end=" ")
    #crearea array-ului pentru stocarea conținutului tablei de joc
    tabla += caracterTablaGoala
    countPozitii += 1
    if(countPozitii == marimeTabla):
        print()
        countPozitii = 0

##Start joc###
#progresJoc = folosit să număr etapele de joc
progresJoc = 0
jucator = ''
while progresJoc != marimeTabla * marimeTabla:
    #alegerea pozițiilor de către jucatori
    if progresJoc % 2 == 0:
        #rândul jucătorului x
        jucator = 'X'
        pozitie =selectiePozitie(tabla, jucator, marimeTabla)
        tabla[pozitie-1] = jucator
        progresJoc += 1

    else:
        #rândul jucătoruluti 0
        jucator = '0'
        pozitie =selectiePozitie(tabla, jucator, marimeTabla)
        tabla[pozitie-1] = jucator 
        progresJoc += 1




        

    #randare tabla de joc
    afisareTabla(tabla)

    #verificare câștigător
    if verificareCastigator(tabla, marimeTabla) == True:
        print(f'Felicitări! Jucătorul {jucator} a câștigat.')
        break

progresJoc += 1

if progresJoc == marimeTabla * marimeTabla:
    print('Din păcate, nu a câștigat nimeni.')

