"""
Script: main.py

Description:
This script generates FASTA files containing Transcription Factor (TF) sequences extracted from a peak file and a reference genome FASTA file. 
It processes the input files, validates their formats, groups peaks by TF names, and generates separate FASTA files for each TF in the specified output directory.

Usage:
    python main.py -f <fasta_file> -p <peak_file> -o <output_directory>

Arguments:
    -f, --fasta (str, required):
        Path to the reference genome FASTA file. This file should be in valid FASTA format.
    
    -p, --peak (str, required):
        Path to the peak file. This file should contain peak information in a valid format.
    
    -o, --output (str, required):
        Path to the output directory where the generated FASTA files will be saved. If the directory does not exist, it will be created.

Dependencies:
    - argparse: For parsing command-line arguments.
    - os: For handling directory creation and path operations.
    - genome: For reading and processing the genome FASTA file.
    - io_utils: For validating file formats.
    - peaks: For extracting sequences from the peak file and grouping them by TF names.

Author:
    Lopez Ordaz Hector Jesus

Date:
    19/05/2025

"""
from genome import genome_upload
from io_utils import is_valid_file
from peaks import extract_sequence_and_read_peak_file, group_peaks_by_tf, fasta_by_tf_generator
import os
import argparse

def main():
    """
    Main script that manages the logic of execution

    Can use python extract_fasta.py -h to see the options of the script
    """

    # Define a parser to get the arguments from the command line
    parser = argparse.ArgumentParser(description="Creates FASTA files from a peak file to extract the Transcription Factor sequences")
    parser.add_argument('-f', '--fasta', required=True, help="Path to the FASTA file")
    parser.add_argument('-p', '--peak', required=True, help="Path to the peak file")
    parser.add_argument('-o', '--output', required=True, help="Path to the output directory")

    arguments = parser.parse_args()

    # Get the arguments from the command line
    fasta_path = arguments.fasta
    peak_file_path = arguments.peak
    output_path = arguments.output

    # Test if the fasta file is valid
    if not is_valid_file(fasta_path, 1):
        print(f"Error: The file {fasta_path} is not a valid FASTA file.")
        exit(1)
    
    #Test if the peak file is valid
    if not is_valid_file(peak_file_path, 0):
        print(f"Error: The file {peak_file_path} is not a valid peak file.")
        exit(1)
    

    # Check if the output path exists, if not create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Call to the funtions

    linealized_genome = genome_upload(fasta_path)
    list_of_peaks = extract_sequence_and_read_peak_file(peak_file_path, linealized_genome)

    # Group peaks by TF_name
    grouped_peaks = group_peaks_by_tf(list_of_peaks)

    # In the end we get a diccionary that cointains keys (TF names) and values that is a list of diccionaries with key of the TF name and the peak number

    # Generate the FASTA files
    fasta_by_tf_generator(grouped_peaks, output_path)
    print(f"FASTA files generated in {output_path}")
    print("The FASTA files generated ...")

# If the program is run directly execute the main script
if __name__ == "__main__":
    main()