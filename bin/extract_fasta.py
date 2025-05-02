import os
import argparse

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
        exit(1)

    with open(fasta_path, 'r') as fasta_file:
        # Read the file and skip the header lines
        # Usising join to remove new lines and spaces and strip() to remove spaces
        # The generator expresion iterates over each line in the file and checks if it does not start with '>'                                                                                                                                                                Fire giant (NO HIT) *kinda

        linealized_genome = ''.join(line.strip() for line in fasta_file if not line.startswith('>'))

    return linealized_genome
    

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
        exit(1)

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

    # Check if the output path exists, if not create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Call to the funtions

    linealized_genome = genome_upload(fasta_path)
    list_of_peaks = extract_sequence_and_read_peak_file(peak_file_path, linealized_genome)

    # Group peaks by TF_name
    grouped_peaks = {}
    for tfs in list_of_peaks:
        tf_name = tfs['TF_name']
        # If the name is not in the diccionary it needs to be added, but the value empty 
        if tf_name not in grouped_peaks:
            grouped_peaks[tf_name] = []
        # Add the key and value corresponding to the tf name
        grouped_peaks[tf_name].append(tfs)
    # In the end we get a diccionary that cointains keys (TF names) and values that is a list of diccionaries with key of the TF name and the peak number

    # Generate the FASTA files
    fasta_by_tf_generator(grouped_peaks, output_path)
    print(f"FASTA files generated in {output_path}")
    print("The FASTA files generated ...")
    

    


# If the program is run directly execute the main script
if __name__ == "__main__":
    main()

