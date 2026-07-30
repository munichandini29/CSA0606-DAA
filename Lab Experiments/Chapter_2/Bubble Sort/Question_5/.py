# Card Game Hand Sorting

n = int(input("Enter number of cards: "))
cards = []

print("Enter card values:")
for i in range(n):
    cards.append(int(input()))

passes = 0

for i in range(n - 1):
    swapped = False
    passes += 1

    for j in range(n - i - 1):
        if cards[j] > cards[j + 1]:
            cards[j], cards[j + 1] = cards[j + 1], cards[j]
            swapped = True

    if not swapped:
        break

print("Sorted Cards:", cards)
print("Number of Passes:", passes)
