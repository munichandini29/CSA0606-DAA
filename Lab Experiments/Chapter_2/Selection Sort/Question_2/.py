# Selection Sort with Swap Counter

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(float(input()))

swap_count = 0

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swap_count += 1

print("Sorted array:", arr)
print("Number of swaps:", swap_count)
