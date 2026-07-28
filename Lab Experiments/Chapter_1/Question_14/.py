# Exponentiation using Divide and Conquer

def power(a, n):
    if n == 0:
        return 1

    half = power(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return a * half * half


a = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Result =", power(a, n))
