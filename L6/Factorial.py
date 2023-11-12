def factorial(x):
    for i in range(x, 1, -1):
        x*=(i-1)
    return x

print("Introduceti numarul:")
n = int(input())
print(factorial(n))
 