def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Introduceti numarul:")
n = int(input())
print(fibonacci(n))