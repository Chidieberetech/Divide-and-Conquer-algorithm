import random

def generate_random_points(size, x_range, y_range):
    """
    Generate a set of random points within the specified ranges.

    Args:
        size (int): Number of points to generate.
        x_range (tuple): Range of x-values (min_x, max_x).
        y_range (tuple): Range of y-values (min_y, max_y).

    Returns:
        list: List of randomly generated points.
    """
    points = []
    _generate_points(points, size, x_range, y_range)
    return points

def _generate_points(points, size, x_range, y_range):
    """
    Recursively generates random points within the specified ranges.

    Args:
        points (list): List to store the generated points.
        size (int): Number of points to generate.
        x_range (tuple): Range of x-values (min_x, max_x).
        y_range (tuple): Range of y-values (min_y, max_y).
    """
    if size <= 0:
        return

    # Divide the ranges into smaller sub-ranges
    x_mid = (x_range[0] + x_range[1]) / 2
    y_mid = (y_range[0] + y_range[1]) / 2

    # Generate points within the sub-ranges
    _generate_points(points, size // 4, (x_range[0], x_mid), (y_range[0], y_mid))
    _generate_points(points, size // 4, (x_range[0], x_mid), (y_mid, y_range[1]))
    _generate_points(points, size // 4, (x_mid, x_range[1]), (y_range[0], y_mid))
    _generate_points(points, size // 4, (x_mid, x_range[1]), (y_mid, y_range[1]))

    # Generate points within the current subrange
    for _ in range(size):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        points.append((x, y))

def main():
    # Define the range of x-values and y-values for the points
    x_range = (0, 10)
    y_range = (0, 10)

    # Generate a set of 10 random points within the specified ranges
    points = generate_random_points(10, x_range, y_range)

    # Print the generated points
    for point in points:
        print(point)

if __name__ == "__main__":
    main()
