# Bubble Sort Visualization

n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("After Pass", i + 1, ":", arr)

print("Sorted Array:", arr)
