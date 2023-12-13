import numpy as np
import matplotlib.pyplot as plt


def scatter_show():
    X_data = np.random.random(100) * 100
    Y_data = np.random.random(100) * 100

    for points in range(100):
        print(f"Point number {points}:", X_data[points], Y_data[points])

    plt.scatter(X_data, Y_data, c="#000", s=150, alpha=0.5)
    # Create a scatter plot:
    # with black (c=color)
    # stars (marker=*)
    # with size 150 (s=size)
    # with opacity 50% (alpha=0.5)

    plt.show()  # Show the graph

def line_plot_show():
    years = [2006 + i for i in range(16)]
    weights = [3, 5, 9, 15, 20, 25, 30, 35, 40, 45, 50, 53, 54, 55, 56, 55.6]

    plt.plot(years, weights)
    plt.show()

line_plot_show()
