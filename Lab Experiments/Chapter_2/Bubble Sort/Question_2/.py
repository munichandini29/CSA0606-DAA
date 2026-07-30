# Bubble Sort - Traffic Signal Priority Queue

priority = {
    "ambulance": 1,
    "bus": 2,
    "car": 3
}

n = int(input("Enter number of vehicles: "))

queue = []

print("Enter vehicles (ambulance/bus/car):")
for i in range(n):
    queue.append(input().lower())

for i in range(n - 1):
    for j in range(n - i - 1):
        if priority[queue[j]] > priority[queue[j + 1]]:
            queue[j], queue[j + 1] = queue[j + 1], queue[j]

print("Priority Queue:", queue)
