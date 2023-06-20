Fasta2Structure: A User-Friendly Tool for Converting Multiple Aligned FASTA Files to STRUCTURE Format

Fasta@Structure is a bioinformatics tool designed to facilitate the manipulation of genomic sequence data. It converts FASTA files into a binary structure, highlighting variable sites within multiple sequences.

Dependencies
Python 3.7 or higher
tkinter (usually comes pre-installed with Python)
BioPython 1.78 or higher
Installation

Linux
Update the system and install Python and pip:
sudo apt-get update
sudo apt-get install python3.8
sudo apt-get install python3-pip

Install Biopython:
pip3 install biopython

Mac
Install Homebrew:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Install Python and pip:
brew install python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

Install Biopython:
pip3 install biopython

Usage
To run the program, navigate to the directory containing the python script and run the following command in the terminal:
python3 fasta_to_structure.py

In the graphical interface that appears, click on the "Select FASTA files" button to select the FASTA files you wish to convert. The result will be displayed in the "Preview" area and saved as "Structure.str" in the same directory.


![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/85827670-c6db-4463-b625-f4148fa56d3a)


The variable sites and any errors that occur during processing are logged to a log file (log.log).

Data Preparation
The input data for this program are FASTA files. Each FASTA file should contain a sequence alignment, meaning all sequences in the file have the same length.

Example of a FASTA file:

shell
Copy code
>seq1
ATGCATGCATGC
>seq2
ATGCATGCATGT
>seq3
ATGAATGCATGC
>
Outputs
After running the program, the results are displayed in the "Preview" area of the graphical user interface and also saved to a file called "Structure.str" in the same directory as the Python script.

Example of output:
seq1 0 0 
seq2 0 1 
seq3 2 0 

Processing activities, including the identified variable sites and any errors that occurred during processing, are logged to a file called "log".

Tests
Check the functionality of the program using sample FASTA files. Observe the results in the "Preview" area and the "Structure.str" output file, and check if they are consistent with the expected.

Maintenance
1.	Program Maintenance: 
• Bug Fixes: Any bugs reported by users or identified by the program developer will be investigated and resolved by the developer. The frequency of bug fixes will be determined by the severity of the bug and its impact on the program's functionality. 
• Updates and Enhancements: Updates will be carried out as necessary to maintain the program's efficiency. Enhancements may include adding new features, performance upgrades, and user interface updates. 
• Dependencies: This program relies on the BioPython module and the Tkinter library for Python. These dependencies will be monitored for any updates. If these libraries are updated, the program will be tested with the new versions to ensure compatibility.

2.	User Feedback: 
• User feedback is crucial for the continuous improvement of the program. A forum will be established on Google Groups (https://groups.google.com/g/fasta2structure) to facilitate communication with users. The developer will monitor this forum and consider inquiries and suggestions for program improvement.

4.	Documentation: 
•The program's documentation will be maintained and updated as necessary.

5.	Testing: 
•After each update or bug fix, tests will be conducted to ensure that the program is still functioning as expected. The tests will include basic functionality, usability testing, and stress testing.

These maintenance procedures will be reviewed and updated as necessary to ensure continuous and efficient functionality.





