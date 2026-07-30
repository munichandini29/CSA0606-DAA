# Real-Time Stock Price Feed using Insertion Sort

n = int(input("Enter number of stock prices: "))
prices = []

print("Enter stock prices:")
for i in range(n):
    prices.append(float(input()))

for i in range(1, n):
    key = prices[i]
    j = i - 1

    while j >= 0 and prices[j] > key:
        prices[j + 1] = prices[j]
        j -= 1

    prices[j + 1] = key

print("Sorted Stock Prices:", prices)
print("Minimum Price:", prices[0])
print("Maximum Price:", prices[-1])
