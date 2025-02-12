#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format and save to data.json
    
    Args:
        csv_filename: Name of the input CSV file
    
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        # Write to JSON file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except Exception:
        return False
