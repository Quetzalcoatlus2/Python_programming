def factorial(x):
    if x < 1:
        return 1
    else:
        return x*factorial(x-1)

print("Introduceti numarul:")
n = int(input())
for i in range(n, 1, -1):
    n*=(i-1)
print(n)
 