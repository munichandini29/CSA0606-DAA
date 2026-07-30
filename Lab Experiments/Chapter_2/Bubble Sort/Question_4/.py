# Compare Plain and Optimized Bubble Sort

n = int(input("Enter number of alerts: "))
arr = []

print("Enter alert levels:")
for i in range(n):
    arr.append(int(input()))

plain = arr.copy()
opt = arr.copy()

plain_comp = 0
opt_comp = 0

# Plain Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        plain_comp += 1
        if plain[j] > plain[j + 1]:
            plain[j], plain[j + 1] = plain[j + 1], plain[j]

# Optimized Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - i - 1):
        opt_comp += 1
        if opt[j] > opt[j + 1]:
            opt[j], opt[j + 1] = opt[j + 1], opt[j]
            swapped = True

    if not swapped:
        break

print("Sorted Alerts:", opt)
print("Plain Comparisons:", plain_comp)
print("Optimized Comparisons:", opt_comp)
