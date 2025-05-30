"""
Script: peaks.py

Description:
This script processes peak files to extract sequences associated with Transcription Factors (TFs) from a linearized genome. 
It groups peaks by TF names and generates separate FASTA files for each TF in the specified output directory. 
The script is designed to handle peak files in tab-separated format and assumes that the genome is provided as a linearized string.

Dependencies:
    - os: For handling file paths and directory operations.
    - pandas: For handling tabular data manipulation.
    - Assumed availability of a linearized genome sequence (produced by another function or script).

Author:
    Lopez Ordaz Hector Jesus

Date:
    19/05/2025
"""

import os
import pandas as pd


def extract_sequence_and_read_peak_file(peak_file_path, linealized_genome, output_path):
    """
    Given a peak file returns a list of dictionaries with TF_name, peak_number and sequence
    
    Parameters:
        peak_file_path: path of a peak file
        linealized_genome: a str linealized that contains the genome
        output_path: path to the output directory

    Returns:
        list_of_peaks (list): List of dictionaries with TF_name, peak_number and sequence
    
    """

    # Check if the path exists
    if not os.path.exists(peak_file_path):
        raise FileNotFoundError(f"The file {peak_file_path} does not exist")
    
    # Read the peak file using pandas
    try:
        df = pd.read_csv(peak_file_path, sep='\t')
    except Exception:
        raise ValueError("Error reading peak file")
    
    # Check if required columns exist
    required_columns = ['TF_name', 'Peak_start', 'Peak_end', 'Peak_number']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Convert columns to numeric, handling potential float values
    df['Peak_start'] = pd.to_numeric(df['Peak_start'], errors='coerce').astype(int)
    df['Peak_end'] = pd.to_numeric(df['Peak_end'], errors='coerce').astype(int) 
    df['Peak_number'] = pd.to_numeric(df['Peak_number'], errors='coerce').astype(int)
    
    # Check if the peaks are not outside range
    genome_length = len(linealized_genome)
    
    # Filter out-of-range peaks and create log
    out_of_range_mask = (df['Peak_start'] < 1) | (df['Peak_end'] > genome_length)
    out_of_range_df = df[out_of_range_mask]
    valid_df = df[~out_of_range_mask]
    
    # Handle out-of-range peaks logging
    if not out_of_range_df.empty:
        log_out = os.path.join(output_path, 'log.out')
        with open(log_out, 'w') as log_file:
            log_file.write('Peaks out of genome range:\n')
            for i, row in out_of_range_df.iterrows():
                log_file.write(f"TF: {row['TF_name']}, Start: {row['Peak_start']}, End: {row['Peak_end']}, Peak_number: {row['Peak_number']}\n")
        print('Warning: Some peaks are bigger than the genome. Check the log.out file')
    
    # Extract sequences and create list of dictionaries
    list_of_peaks = []
    for i, row in valid_df.iterrows():
        peak_start = row['Peak_start']
        peak_end = row['Peak_end']
        sequence = linealized_genome[peak_start-1 : peak_end]
        
        list_of_peaks.append({
            'TF_name': row['TF_name'],
            'sequence': sequence,
            'peak_number': row['Peak_number']
        })
    
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
    # Convert list of dictionaries to DataFrame for easier manipulation
    df = pd.DataFrame(peaks)
    
    # Group by TF_name and convert back to the expected format
    grouped_peaks = {}
    for tf_name, group in df.groupby('TF_name'):
        grouped_peaks[tf_name] = group.to_dict('records')
    
    return grouped_peaks