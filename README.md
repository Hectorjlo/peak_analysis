**Developer**: Lopez Ordaz Hector jesus
**Email**: <hectorjl@lcg.unam.mx> 
**Date**: [29/05/2025]
 # Peak Analysis 
  
## Description

  
This project is designed to automate the process of identifying the exact binding site of transcriptional regulators of transcription factors (TFs) given a whole genome and a peak file obtained by ChIP-seq.

## Table of Contents

-  [Installation](#installation)
-  [Use](#use)
-  [Project structure](#project-structure)
-  [Dependencies](#dependencies)
-  [License](#license)
  
## Installation

1. Clone this repository:

```bash
git  clone  https://github.com/Hectorjlo/peak_analysis.git
cd  peak_analysis
```

2. Create a virtual environment (recommended):

```bash
python  -m  venv  venv  venv
source  venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. Required dependencies:

```bash
pandas
argparser
os
```
  
## Usage  

To run the main, you can use the following command:
```bash
python  main.py  -f [PATH] -p [PATH] -f [PATH]
```

## Project structure

```
peak_analysis/
│
├── data/
| 	├── E_coli_K12_MG1655_U00096.3.fasta
| 	├── U00096.3.bfile
| 	└── union_peaks_file. tsv
│
├── bin/ # Main project source code
│ 	└── sequence_extractor/
|	├── genome.py
| 	├── io_utils.py
| 	├── main.py
| 	└── peaks.py
│
│
├── .gitignore
├── LICENSE
└── README.md
```

## Dependencies 

The main dependencies of this project are: 

* Python 3
* Pandas
* Argparser
* Os
 

## License

This project is licensed under the "BSD 3-Clause License". See the `LICENSE` file for more details.
