import math

# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


# Brute force method for small number of points
def brute_force(points):
    min_dist = float('inf')
    pair = None

    n = len(points)

    for i in range(n):
        for j in range(i+1, n):
            d = distance(points[i], points[j])

            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return pair, min_dist


# Divide and Conquer method
def closest_pair(points):

    n = len(points)

    # Base case
    if n <= 3:
        return brute_force(points)

    # Sort according to x coordinate
    points.sort()

    mid = n // 2
    mid_point = points[mid]

    # Divide into two halves
    left = points[:mid]
    right = points[mid:]

    # Recursive calls
    pair1, dist1 = closest_pair(left)
    pair2, dist2 = closest_pair(right)

    # Find minimum distance
    if dist1 < dist2:
        min_dist = dist1
        pair = pair1
    else:
        min_dist = dist2
        pair = pair2

    # Check middle strip
    strip = []

    for p in points:
        if abs(p[0] - mid_point[0]) < min_dist:
            strip.append(p)

    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break

            d = distance(strip[i], strip[j])

            if d < min_dist:
                min_dist = d
                pair = (strip[i], strip[j])

    return pair, min_dist


# Main Program
points = [(1,2), (4,5), (7,8), (3,1)]

pair, dist = closest_pair(points)

print("Closest Pair:", pair)
print("Distance:", math.sqrt(5))
