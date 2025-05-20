"""
Script: io_utils.py

Description: 
Checks if a file is a valid FASTA file.
This function validates the existence and format of a FASTA file.
It checks if the file exists, is not empty, and contains at least one header line that starts with '>'.
It is designed to be used in the context of processing genomic data, specifically for validating FASTA files before further analysis.

Dependencies:
    - os: For handling directory creation and path operations.

Author:
    Lopez Ordaz Hector Jesus

Date:
    19/05/2025
    
"""

import os

def is_valid_file(file_path, type_file):
    """
    Checks if a file is a valid FASTA file.

    Parameters:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a valid FASTA file, False otherwise.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return False

    # Check if the file is empty
    if not (os.path.getsize(file_path)):
        print(f"Error: The file {file_path} is empty.")
        return False

    if type_file == 1:
        # Check if the file has at least one header line that starts with '>'
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('>'):
                    return True

        print(f"Error: The file {file_path} does not appear to be a valid FASTA file no header found")
        return False
    
    return True