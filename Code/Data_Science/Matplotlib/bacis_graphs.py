import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


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

    plt.plot(years, weights, lw=3, color="#000")
    # Create a line plot:
    # with line weight 3 (lw=3)

    plt.show()


def bar_plot_show():
    x = ["C++", "C#", "Java", "Python", "JavaScript", "PHP"]
    y = [20, 50, 60, 40, 30, 10]

    plt.bar(x, y, color="#000", align="edge", width=0.5)
    # Create a bar plot:
    # with align edge (align="edge")
    # with width 0.5 (width=0.5)
    plt.show()


def histograms_plot_show():
    ages = np.random.normal(20, 1.5, 1000)

    plt.hist(ages, bins=20)
    plt.show()


def pie_plot_show():
    languages = ["C++", "C#", "Java", "Python", "JavaScript", "PHP"]
    votes = [20, 50, 60, 40, 30, 10]

    plt.pie(votes, labels=languages, autopct="%1.1f%%", explode=[0, 0, 0, 0.1, 0, 0])
    # Create a bar plot:
    # with labels (labels=languages)
    # with auto percentage (autopct="%1.1f%%")
    # with explode (explode=[0, 0, 0, 0.1, 0, 0])
    plt.show()


def plot_customization_show():
    year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    income = [55, 54, 60, 120, 151, 350, 549, 648]

    plt.plot(year, income)
    plt.title("Income per year")
    plt.xlabel("Year")
    plt.ylabel("Income")
    plt.show()


def multiple_plots_show():
    year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    income = [55, 54, 60, 120, 151, 350, 549, 648]
    expenses = [50, 60, 70, 80, 90, 100, 110, 120]

    plt.plot(year, income)
    plt.plot(year, expenses)
    plt.title("Income and expenses per year")
    plt.xlabel("Year")
    plt.ylabel("Income and expenses")
    plt.legend(["Income", "Expenses"])
    plt.show()


def three_d_plot_show():
    ax = plt.axes(projection='3d')
    x = np.random.random(100)
    y = np.random.random(100)
    z = np.random.random(100)

    ax.scatter(x, y, z)
    plt.show()


def animation_plot_show():
    head_tails = [0, 0]
    for i in range(100):
        head_tails[random.randint(0, 1)] += 1
        plt.bar(["Head", "Tail"], head_tails, color=["red", "blue"])
        plt.pause(0.05)
    plt.show()


def image_show():
    img = Image.open("image_coder_colored.png")
    plt.imshow(img)
    plt.show()


image_show()
