"""
Script: peaks.py

Description:
This script processes peak files to extract sequences associated with Transcription Factors (TFs) from a linearized genome. 
It groups peaks by TF names and generates separate FASTA files for each TF in the specified output directory. 
The script is designed to handle peak files in tab-separated format and assumes that the genome is provided as a linearized string.

Dependencies:
    - os: For handling file paths and directory operations.
    - Assumed availability of a linearized genome sequence (produced by another function or script).

Author:
    Lopez Ordaz Hector Jesus

Date:
    19/05/2025
"""

import os


def extract_sequence_and_read_peak_file(peak_file_path, linealized_genome):
    """
    Given a peak file returns a list of dictionaries with TF_name, peak_number and squence
    
    Parameters:
        peak_file_path: path of a peak file
        linealized_genome: a str linealized that cointains the genome

    Returns:
        list_of_peaks (list): List of dictionaries with TF_name, peak_number and sequence
    
    """

    # Check if the path exists
    if not os.path.exists(peak_file_path):
        print(f"The file {peak_file_path} does not exist")
        return FileNotFoundError

    # Create a list of the TF_name, peak_start and peak_end
    list_of_peaks = []
    with open(peak_file_path, 'r') as peak_file:
        # Skip the first line of the file of the peak file, that is the header
        next(peak_file)  

        # Read each line and split it by tab
        for line in peak_file:
            columns = line.strip().split('\t')
            # TF_name is in the third column, peak_start in the fourth and peak_end in the fifth (counting form 1)
            # The positions can have .0, that int can't convert, so first is converted in a float and then in a int
            tf_name = columns[2]  
            peak_start = int(float(columns[3]))
            peak_end = int(float(columns[4]))
            peak_number = int(float(columns[6]))
            list_of_peaks.append({
                'TF_name': tf_name, 
                'sequence': linealized_genome[peak_start-1 : peak_end], 
                'peak_number': peak_number})
    
    return list_of_peaks


    


def fasta_by_tf_generator(list_of_peaks, output_path):
    """
    Generates FASTA files for each TF_name
    
    Parameters:
       linealized_genome: a str linealized that cointains the genome 
       tf_peaks_list: list of dicctonaries of the tf obtained

    Returns:
        Files generated in the given output path 
    
    """
    # With the list of dictionaries create a fasta file for each TF_name
    for tf_name, tf_peaks in list_of_peaks.items():
        # Create the output file name
        output_file_name = os.path.join(output_path, f"{tf_name}.fasta")
        with open(output_file_name, 'w') as output_file:
            # Write the header and the sequence below it
            for peak in tf_peaks:
                output_file.write(f">{peak['TF_name']}_{peak['peak_number']}\n")
                sequence = peak['sequence']
                # Wrap the sequence to 75 characters per line
                for i in range(0, len(sequence), 75):
                    output_file.write(sequence[i : i+75] + '\n')
            output_file.write('\n')
            

def group_peaks_by_tf(peaks):
    """
    Groups peaks by their TF_name.

    Parameters:
        peaks (list): List of dictionaries containing peak information.

    Returns:
        dict: A dictionary where keys are TF_names and values are lists of peaks.
    """
    grouped_peaks = {}
    for tfs in peaks:
        tf_name = tfs['TF_name']
        if tf_name not in grouped_peaks:
            grouped_peaks[tf_name] = []
        grouped_peaks[tf_name].append(tfs)
    return grouped_peaks