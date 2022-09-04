# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data, header=None):
    """Saves the csv file from a provided file path.
    
    Args:
        csvpath (Path): csv file path
        data (list of lists): Data to include in the csv file
        header (list): A header for the csv file, optional
        
    """
    
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)
    
    return True