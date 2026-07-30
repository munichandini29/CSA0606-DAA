# Card Sorting While Playing using Insertion Sort

n = int(input("Enter number of cards: "))
cards = []

print("Enter card values:")
for i in range(n):
    cards.append(int(input()))

for i in range(1, n):
    key = cards[i]
    j = i - 1

    while j >= 0 and cards[j] > key:
        cards[j + 1] = cards[j]
        j -= 1

    cards[j + 1] = key

print("Sorted Cards:", cards)
