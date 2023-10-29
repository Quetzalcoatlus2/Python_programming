import time

print("Introduceți un număr de secunde:")
sec = 1
numar=int(input())
while numar != 0:
    print("Mississippi", sec)
    sec += 1
    numar -= 1
    time.sleep(1)
