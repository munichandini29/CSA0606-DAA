# Counting Inversions using Merge Sort

def merge(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge(arr[:mid])
    right, inv_right = merge(arr[mid:])

    result = []
    i = j = inv = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv += len(left) - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, inv + inv_left + inv_right


n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

sorted_arr, inversions = merge(arr)

print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)
