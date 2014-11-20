"""
Data Visualization Project

Take the data we parsed earlier and create a different format
fir rendering a map. Here we parse through each line item of the
CSV file and create a geojson object, to be collected into one geojson
file for uploading to git
"""

from geojson import dumps
import geojson as g

from parse import parse, MY_FILE
import parse as p

print MY_FILE

def create_map(data_file):
    # Define type of GeoJSON we're creating
    geo_map = {"type": "FeatureCollection"}

    # Define empty list to collect each point to graph
    item_list = []

    # Iterate oveer out data to create GeoJSON document
    # We're using enumerate() so we fet the line, as well
    # the index, which is the line number.
    for index, line in enumerate(data_file):

        # Skip any zero coordinates as this will through off
        # our map.
        if line['X'] == '0' or line['Y'] == '0':
            continue

        # Setup a new dictionary for each iteration
        data = {}

        # Assign line items to appropriate GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'].
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # Add data dictionary to our item_list







