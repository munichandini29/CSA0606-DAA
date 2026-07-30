# Library Book Reordering using Selection Sort

n = int(input("Enter number of books: "))

books = []

print("Enter Book IDs:")
for i in range(n):
    books.append(int(input()))

moves = 0

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if books[j] < books[min_index]:
            min_index = j

    if min_index != i:
        books[i], books[min_index] = books[min_index], books[i]
        moves += 1

print("Sorted Book IDs:", books)
print("Physical Moves:", moves)
