#!/usr/bin/env python3
"""
Module that reads data from CSV and converts it
into another format json using serialisation tehchniques.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert CSV file to JSON format.

    :param CSV filename: The name of the CSV file to convert.
    :return: JSON data as a string.
    """
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
