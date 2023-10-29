x=25
bitNumber1 = 3
bitNumber2 = 2

#Se afiseaza valoarea bitului indicat
rezultat = 1==(x>>bitNumber1 & 1)
print(rezultat)

print(bin(x))

#Transforma valoarea bitului in True
rezultat = x | (1<<bitNumber1)
print(rezultat)

#Transforma valoarea bitului in False
rezultat = x & ~(1<<bitNumber1)
print(rezultat)

#Aceasta linie transforma starea adica din 0 in 1 si vice-versa
rezultat = x ^ (1<<bitNumber1)
print(rezultat)

#Aceasta linie transforma simultan 2 biti
rezultat = x ^ ((1<<bitNumber1)|(1<<bitNumber2))
print(rezultat)
