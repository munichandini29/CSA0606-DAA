# Optimized Bubble Sort

n = int(input("Enter number of roll numbers: "))
arr = []

print("Enter roll numbers:")
for i in range(n):
    arr.append(int(input()))

passes = 0

for i in range(n - 1):
    swapped = False
    passes += 1

    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

print("Sorted Roll Numbers:", arr)
print("Number of Passes:", passes)
