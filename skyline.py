'''This program will find skyline points from set of points'''
import plot
from random import randint as _rand

small = 4
big = 10


# this function will only generate random interger coordinate
def random_xy_generator(count, x_min, x_max, y_min, y_max):
    data = []
    for i in range(count):
        x = _rand(x_min, x_max)
        y = _rand(y_min, y_max)
        data.append((x, y))

    return data


def skyline_points(array_of_points):
    pass


def skyline_config():
    '''This function will manage all the tasks related to skyline construction i.e from getting points to finding skyline points and
    ploting it as well'''

    # need to get all the points here
    data_points = random_xy_generator(10, 1, 10, 1, 10)
    plot.plot_2D(data_points, big)
    print("all good")
