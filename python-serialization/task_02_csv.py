#!/usr/bin/env python3
"""
Module that reads data from CSV and converts it into JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert CSV file to JSON format.
    Param CSV filename: The name of the CSV file to convert.
    Return: JSON data as a string.
    """
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                row['age'] = int(row['age'])
                data.append(row)
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
        return False

    try:
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        return False
