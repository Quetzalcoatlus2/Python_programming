x=25
bitNumber = 2
rezultat = 1==(x>>bitNumber & 1)
print(rezultat)

print(bin(x))

rezultat = x | (1<<bitNumber)
print(rezultat)
rezultat = x & ~(1<<bitNumber)
print(rezultat)