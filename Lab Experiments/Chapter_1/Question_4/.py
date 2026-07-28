# Fibonacci Series using Iterative and Recursive Methods

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))

# Iterative Method
print("Iterative:")
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\nRecursive:")
for i in range(n):
    print(fibonacci(i), end=" ")
