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
    """Visualize data by day of week"""
    data_file = parse(MY_FILE, ",")
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot!
    plt.savefig("pictures/Days.png")

    # Close figure
    plt.clf()

def visualize_type():
    """Visualize data by catagory in a bar graph"""

    # grab our parsed data
    data_file = parse(MY_FILE, ",")

    # Same as before, this returns a dict where it sums the
    # total incidents per Catagory
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter
    # Since order doesn't matter, we can just use counter.keys()
    labels = tuple(counter.keys())

    # Set where the labels hit the axis
    xlocations = np.array(range(len(labels))) + 0.5 # Changed na to np

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick locations to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation = 90)

    # Give some more roomso the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the plot
    plt.savefig("pictures/Type.png")

    # Close figure
    plt.clf()
                
def main():
    visualize_type()

if __name__=="__main__":
    main()
