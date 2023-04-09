Fasta to Structure Converter
Version: 1.0.0

Platform: Cross-platform (Windows, macOS, Linux) with a Windows-built executable available

Description
This application is a converter for FASTA files into Structure format. 
It allows you to select multiple FASTA files, identify variable sites, and convert the sequences into binary format. 
The output will be a concatenated file containing all the processed sequences in Structure format.

Features
Select multiple FASTA files
Identify variable sites in alignments
Convert sequences into binary format
Handle missing sequences by padding with appropriate -9 values
Preview the concatenated results
Save the output in Structure format
Requirements
Python 3.7 or higher
BioPython
tkinter
Installation
Python Script
Install Python 3.7 or higher: https://www.python.org/downloads/
Install the required libraries:
bash
Copy code
pip install biopython
Windows Executable
A pre-built Windows executable is available for download. 
You don't need to install Python or any additional libraries if you use the executable. 
Download the Fasta2Structure.exe file and run it on your Windows system.

Usage
Python Script
Save the script provided in this repository as fasta_to_structure.py
Run the script:
bash
Copy code
python fasta_to_structure.py

Windows Executable
Download the fasta_to_structure.exe file
Run the executable by double-clicking on it
In both cases:

Click on "Select FASTA files" button to open a file dialog and select the FASTA files you want to process
The application will process the files, displaying the progress and a preview of the converted data
Once the conversion is complete, a Structure format file named "Structure.str" will be saved in the same directory as the script or executable

Troubleshooting
If you encounter any issues or errors during the conversion process, please check the console output for more details.

Contributing
Feel free to open an issue or submit a pull request if you would like to improve the application or report a bug.

License
This project is licensed under the MIT License.
