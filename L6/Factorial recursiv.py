def factorial(x):
    if x < 1:
        return 1
    else:
        return x*factorial(x-1)
 
 
print("Introduceti numarul:")
n = int(input())
print(factorial(n))
