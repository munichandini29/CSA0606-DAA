# Selection Sort - Top K Scores

scores = list(map(int, input("Enter scores: ").split()))
k = int(input("Enter Top K value: "))

n = len(scores)

for i in range(min(k, n)):
    max_index = i

    for j in range(i + 1, n):
        if scores[j] > scores[max_index]:
            max_index = j

    scores[i], scores[max_index] = scores[max_index], scores[i]

print("Top", k, "Scores:", scores[:k])
