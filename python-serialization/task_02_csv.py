#!/usr/bin/env python3
"""
Module that reads data from CSV and converts it
into another format json using serialisation tehchniques.
"""
import csv
import json


def convert_csv_to_json(csv, filename):
    """
    Convert CSV file to JSON format.

    :param CSV filename: The name of the CSV file to convert.
    :return: JSON data as a string.
    """
    data = []
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file)
        try:
            csv_writer.writeheader()
        except csv.Error:
            # If the CSV file is empty, we cannot write a header
            pass
        for row in csv_writer:
            data.append(row)
            return True

    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        try:
            csv_reader.fieldnames
        except csv.Error:
            # If the CSV file is empty, we cannot read it
            return json.dumps(data, indent=4)
        for row in csv_reader:
            data.append(row)
            return True

    return json.dumps(data, indent=4)
