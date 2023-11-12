def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return b
print("Introduceti numarul:")
n = int(input())
print(fibonacci(n))