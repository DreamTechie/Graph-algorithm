''' This file will plot 2-d and 3-d points'''
import numpy as np
import matplotlib.pyplot as plt


# drawing lines between given points iteratively

def draw_line(array):
    data = array  # array should be of format [(),(),(),()]


# 2D ploting using matplotlib
def plot_2D(array, size):
    # array should be of format [(),(),(),()]

    data = array
    x, y = zip(*data)
    plt.scatter(x, y, size)
    plt.show()
