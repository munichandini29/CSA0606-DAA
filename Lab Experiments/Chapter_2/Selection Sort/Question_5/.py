# Selection Sort with Execution Time

import time

n = int(input("Enter number of products: "))

prices = []

print("Enter product prices:")
for i in range(n):
    prices.append(int(input()))

start = time.time()

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if prices[j] < prices[min_index]:
            min_index = j

    prices[i], prices[min_index] = prices[min_index], prices[i]

end = time.time()

print("Sorted Prices:", prices)
print("Execution Time:", end - start, "seconds")
