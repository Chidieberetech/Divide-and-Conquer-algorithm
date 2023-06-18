import math

def distance(P1, P2):

    """
    Calculate the distance between two points P1 and P2.
    """
    return math.sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)

def brute_Force(P):
    """
    Brute-force method to get the closest pair of P in a given set.
    def brute_Force(P: {__len__, __getitem__}) -> tuple[float, tuple | tuple[Any, Any]]
    """
    min_DIST = float('inf')
    closest_points = ()

    n = len(P)
    for a in range(n):
        for b in range(a + 1, n):
            dist = distance(P[a], P[b])
            if dist < min_DIST:
                min_DIST = dist
                closest_points = (P[a], P[b])

    return min_DIST, closest_points

def strip_closest(strip_points, min_distance, closest_pair):
    """
    Helper function to find the closest pair of P within the strip
    def strip_closest(strip_points: {__len__, __getitem__},
                  min_distance: Any,
                  closest_pair: Any) -> tuple[float, tuple[Any, Any]].
    """
    n = len(strip_points)
    for a in range(n):
        b = a + 1
        while b < n and strip_points[b][1] - strip_points[a][1] < min_distance:
            dist = distance(strip_points[a], strip_points[b])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (strip_points[a], strip_points[b])
            b += 1

    return min_distance, closest_pair


# noinspection PyGlobalUndefined
def closest_pair(points):
    """
    Divide & Conquer algorithm to find the closest pair of P in a given set.
    def closest_pair(points: {__len__, __getitem__}) -> tuple[float, tuple | tuple[Any, Any]] | tuple[float, tuple[Any, Any]]
    """
    global closest_pair
    n = len(points)

    # Base case: if there are only two or three P, use brute force
    if n <= 3:
        return brute_Force(points)

    # Sort P by x-coordinate
    points_sorted_by_x = sorted(points, key=lambda point: point[0])

    # Divide the bruteForce(P) into two halves
    mid = n // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

    # Recursively find the closest pair in each half
    min_left_dist, closest_left = closest_pair(left_half)
    min_right_dist, closest_right = closest_pair(right_half)

    # Determine the minimum distance and closest pair between the two halves
    if min_left_dist < min_right_dist:
        min_dist = min_left_dist
        closest_pair = closest_left
    else:
        min_dist = min_right_dist
        closest_pair = closest_right

    # Find the P within the strip that are closer than the minimum distance
    strip_points = [point for point in points_sorted_by_x if abs(point[0] - points[mid][0]) < min_dist]
    strip_points_sorted_by_y = sorted(strip_points, key=lambda point: point[1])

    # Check for closer pairs within the strip.
    min_dist, closest_pair = strip_closest(strip_points_sorted_by_y, min_dist, closest_pair)

    # Return the closest pair and its distance
    return min_dist, closest_pair

# Test the algorithm with a sample set of P(points)
points = [(3.5, 9.5), (1, 7), (7, 4),  (6, 130), (10, 40), (13, 9016), (15, 10)]
min_distance, closest_points = closest_pair(points)

print("Closest pair of P(points): ", closest_points)
print("Distance: ", min_distance)
