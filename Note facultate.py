#Vom considera un program care va ține evidența notelor pentru cei șase ani de studii, câte zece discipline în fiecare an pentru o grupă de 30 de studenți.
#Modelați un program care să genereze lista respectivă, să permită introducerea unor note la anumite discipline și la final va determina: câte note de 10 au fost înregistrate?
#câte restanțe se înregistrează pentru fiecare an de studiu în parte?
#mediile pe cei șase ani de studiu pentru fiecare dintre cei 30 de studenți. 
#Hint: 
import random
note = [[[random.randint(1, 10) for h in range(30)] for d in range(10)] for e in range(6)]
print(note)

print("Introduceti anul pentru care vreti sa modificati nota:")
a=int(input())
print("Introduceti materia pentru care vreti sa modificati nota:")
b=int(input())
print("Introduceti studentul pentru care vreti sa modificati nota:")
c=int(input())
print("Introduceti nota:")
d=int(input())
note[a-1][b-1][c-1] = d
print(note)
count=0
restante=0
for i in range(6):
    restante=0
    for j in range(10):
        for k in range(30):
            if note[i][j][k]==10:
                 count+=1
            if note[i][j][k]<5:
                 restante+=1    
    print("Numar note restante pentru anul", i+1,"este",restante)
print("Numar note de 10:",count)


