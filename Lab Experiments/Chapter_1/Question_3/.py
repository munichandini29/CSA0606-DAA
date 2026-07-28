# Factorial using Iterative and Recursive Methods

def recursive_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_fact(n - 1)

n = int(input("Enter a number: "))

# Iterative
fact = 1
for i in range(1, n + 1):
    fact *= i

print("Iterative Factorial =", fact)
print("Recursive Factorial =", recursive_fact(n))
