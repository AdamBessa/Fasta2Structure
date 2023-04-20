Fasta2Structure

This program is a simple graphical user interface (GUI) tool that allows you to concatenate and convert multiple FASTA files into a Structure format file. It is useful for researchers working with DNA alignments who want to perform population genetics analyses using the Structure software. The program is compatible with different platforms, including Windows, macOS, and Linux. This README provides instructions for running the tool on Windows.

Link to Windows version: https://1drv.ms/u/s!Akxz__NDrSavhe9nDlYPCYg70mMcww?e=2JtsDu

Dependencies
To run the script, you need Python 3.6 or higher and the Biopython library. You can install Biopython via pip:

pip install biopython
Preparing Multiple DNA Alignments
Before using this tool, make sure your DNA alignment files are in the FASTA format. Each file should contain aligned sequences of the same loci for different individuals or populations. The program will identify variable sites in each alignment and concatenate them into a single output file in Structure format.

For the concatenation process to work correctly, make sure the sequence names (identifiers) are consistent across all input FASTA files. The sequence names should be the same for the same individual or population in each file.

Here is an example of correctly formatted FASTA files:

Alignment 1:
>Sample1
ATGCATGCATGCTAGCTAGCTAGCTAG
>Sample2
ATGCATGCATGCTAGCTAGCTAGCTAG
>Sample3
ATGCATGCATGCTAGCTAGCTAGCTAG
File 2:

Alignment 2:
>Sample1
CGTACGTACGTACGTACGTACGTACGTA
>Sample2
CGTACGTACGTACGTACGTACGTACGTA
>Sample3
CGTACGTACGTACGTACGTACGTACGTA

Make sure your alignments do not have any extra characters or incorrect formatting, as this may cause errors during processing.

Running the Script
To run the script, simply use the Python interpreter (version 3.6 or higher):


python fasta_to_structure.py
This will open the GUI, where you can interact with the program and convert FASTA files to Structure format.

Usage
Click the "Select FASTA files" button to open a file dialog and select multiple FASTA files containing your DNA alignments.
The program will process each selected FASTA file, extracting variable sites and converting them to binary format. 
The progress is shown on a progress bar and a progress label.
After processing all files, the program pads missing sequences with "-9" to align the sequences in the output file.
The final concatenated results are displayed in a text box, and the output is saved in a file named "Structure.str".

You can now use the generated "Structure.str" file as input for the Structure software to perform population genetics analyses.
