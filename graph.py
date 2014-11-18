"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in JSON-like
form, visualize in graphs, and plot on Google Maps.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

# Import parse function from parse.py
from parse import parse

MY_FILE = "data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by the day of the week"""

    # grab our parsed data that we parsed earlier

    # make a new variable, 'counter', from iterating though each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week

    # seperate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)

    # with the x-axis data, assign it to a matplotlib plot instance

    # create the amount of ticks needed in our x-axis and assign the labels

    # save the plot!

    # close plot file
