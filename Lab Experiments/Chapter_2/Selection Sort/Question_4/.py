# Contest Prize Distribution using Selection Sort

n = int(input("Enter number of participants: "))

participants = []

for i in range(n):
    name = input("Enter participant name: ")
    score = int(input("Enter score: "))
    participants.append([name, score])

# Selection Sort (Descending Order)
for i in range(n - 1):
    max_index = i

    for j in range(i + 1, n):
        if participants[j][1] > participants[max_index][1]:
            max_index = j

    participants[i], participants[max_index] = participants[max_index], participants[i]

print("\nPrize Ranking")
for i in range(n):
    print(i + 1, ".", participants[i][0], "-", participants[i][1])
