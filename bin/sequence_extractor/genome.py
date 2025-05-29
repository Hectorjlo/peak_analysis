"""
Script: genome.py

Description: 
Reads a FASTA file and returns its genomic sequence as a single linearized string.
This function processes a FASTA file by removing header lines (lines starting with '>') 
and concatenating the remaining sequence lines into a single continuous string. 
It also ensures that all newline characters and spaces are removed from the sequence.

Dependencies:
    - os: For handling directory creation and path operations.

Author:
    Lopez Ordaz Hector Jesus

Date:
    19/05/2025
    
"""
import os

def genome_upload(fasta_path):
    """
    Given a FASTA file returns a single string or text
    
    Parameters:
        fasta_path: path of a FASTA file

    Returns:
        linealized_genome (str): 
    
    """
    # Check if the path exists
    if not os.path.exists(fasta_path):
        print(f"The file {fasta_path} does not exist")
        return 0

    with open(fasta_path, 'r') as fasta_file:
        # Read the file and skip the header lines
        # Usising join to remove new lines and spaces and strip() to remove spaces
        # The generator expresion iterates over each line in the file and checks if it does not start with '>'                                                                                                                                                                Fire giant (NO HIT) *kinda

        linealized_genome = ''.join(line.strip() for line in fasta_file if not line.startswith('>'))

    return linealized_genome