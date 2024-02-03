# x, y, z input area
coordinates: list[tuple[int, int, int]] = [
    (15, 51, 58),
    (1, 1, 1),
    (11, 35, 53),
    (36, 54, 6),
    (19, 47, 9),
    (21, 58, 9),
]
view_angle: tuple[int, int] = (45, 45)
show_axes: bool = True

import matplotlib.pyplot as plt


def main() -> None:
    """
    Sorts the given list of 3D coordinates by their distance from the origin and plots them in a 3D plot.

    Args:
        args (list[tuple[int, int, int]]): The list of 3D coordinates to be sorted and plotted.

    Returns:
        None
    """
    # sort points by distance from origin
    sorted_coordinates = sorted(coordinates, key=distance_from_origin)

    # print coordinates & formatted distance from origin to 2 decimal places
    print("Inputs:")
    print("(x, y, z) | distance from origin")
    for point in coordinates:
        print(f"{distance_from_origin(point):.2f} | {point}")
    print("Sorted coordinates:")
    for point in sorted_coordinates:
        print(f"{distance_from_origin(point):.2f} | {point}")

    # plot the sorted coordinates in interactive 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Extract x, y, and z coordinates from the sorted list
    x_points, y_points, z_points = zip(*sorted_coordinates)

    # Use the plot function to connect the points in order
    ax.plot(x_points, y_points, z_points)

    # Add a red dot at the first point
    ax.plot(x_points[0], y_points[0], z_points[0], marker="o", color="red")

    # remove the "#" in next line to remove all axes
    if show_axes is False:
        plt.axis("off")

    # set view angle
    ax.view_init(view_angle[0], view_angle[1])

    plt.show()


def distance_from_origin(coord: tuple[int, int, int]) -> float:
    """
    Calculate the distance from the origin to a given coordinate.

    Args:
        coord (tuple[int, int, int]): The coordinate in 3D space.

    Returns:
        float: The distance from the origin to the coordinate.
    """
    x, y, z = coord
    return (x**2 + y**2 + z**2) ** 0.5


if __name__ == "__main__":
    main()
