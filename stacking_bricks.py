import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
import re
import cv2

def main() -> None:
    data = readFile()
    list = []
    for i in range(100):
        list.append((random.random(), random.random(), random.random()))

    plot_brickwall(data)


def readPng() -> None:
    pass
    
    


def plot_brickwall(brick_params):
    # Initial
    single_brick_width = 1
    single_brick_height = 2
    current_x = -single_brick_width / 2
    current_height = 0
    fig, ax = plt.subplots()

    # normalize x
    min_x = min(brick_params, key=lambda x: x[0])[0]
    max_x = max(brick_params, key=lambda x: x[0])[0]

    # Calculate the median z value
    median_z = sorted(brick_params, key=lambda x: x[2])[len(brick_params) // 2][2]

    # Loop through the bricks
    for params in brick_params:
        # Unpack the tuple
        x, y, z = params

        # Decorate the plot with the brick parameters
        offset = (x - min_x) / (max_x - min_x) * (2 / 3)
        thickness = 1
        direction = 1 if z < median_z else -1

        print(f"{offset:.1f}, {thickness:.1f}, {direction:.1f}")

        # Initialize figure and axis

        # Draw each brick
        for _ in range(int(thickness)):
            ax.add_patch(
                Rectangle(
                    (current_x, current_height),
                    single_brick_width,
                    single_brick_height,
                    facecolor="brown",
                    edgecolor="black",
                )
            )
            current_height += single_brick_height
            if current_height > 10:
                current_height = 0
                current_x += 5
        # Update the current position for the next brick
        current_x += offset * direction

    # Set labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Height")
    ax.set_title("Brickwall Stacking Pattern")
    # scale the plot as show all
    ax.autoscale_view()
    plt.axis("equal")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
