# Test cases tested
### FASTA or peak file not found
Output:
```
Error: The file [path] is not a valid FASTA file.
```

### FASTA or peak empty
Output:
```
Error: The file [path] is not a valid FASTA file.
```

### peaks out of range in terms of the FASTA file
Output:
```
Warning: Some peaks are bigger than the genome. Check the log.out file

FASTA files generated in [path]

The FASTA files generated ...
```
And a file in the output folder with the peaks not included named "log.out"