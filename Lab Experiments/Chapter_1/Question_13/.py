# Maximum Subarray Sum using Kadane's Algorithm

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print("Maximum Subarray Sum =", max_sum)
