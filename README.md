Fasta2Structure: A User-Friendly Tool for Converting Multiple Aligned FASTA Files to STRUCTURE Format

The STRUCTURE software has gained popularity as a tool for population structure and genetic analysis. However, tailoring data to meet STRUCTURE's specific requirements can be challenging and prone to errors, particularly when managing multilocus data. Here, I introduce a graphical user interface (GUI) application designed to simplify the process of converting multiple sequence alignments into a single, cohesive file that is compatible with the STRUCTURE software. The application has been developed using Tkinter for the GUI and Biopython for handling FASTA files. It processes the files, identifies variable sites, and converts the sequences into a binary format. Subsequently, the sequences are concatenated and displayed within the graphical interface's text area, enabling users to review and verify the results. Furthermore, the program saves the concatenated results in a file, thereby providing a ready-to-use input for the STRUCTURE software. This application presents an efficient and reliable solution for transforming multiple aligned FASTA files into a concatenated binary format file, which is compatible with the STRUCTURE software. With its user-friendly graphical interface and error-reduction strategy, this tool proves to be invaluable for researchers engaged in population structure and genetic analysis. This program is designed to convert FASTA files into a binary representation that is then used to identify variable sites. This binary representation is then saved in a structure (.str) file. Variable sites are defined as positions in the sequence where the nucleotides differ among the sequences in the alignment. These sites are identified and flagged, and the resulting data is saved in a specific format that can be used for further analysis. The program allows users to select multiple FASTA files at once and performs the conversion of all selected files in the background. During the conversion, progress is indicated via a progress bar and a text label.



Dependencies and Version

This program depends on the following Python libraries, which need to be installed in order for the program to run properly:

Python: The recommended version for this program is Python 3.7 or higher.

Tkinter: This is a standard library for Python 3 and hence its version will be tied to the installed Python version. It should be compatible with Python 3.7 or higher.

Biopython: The recommended version for this program is Biopython 1.78 or higher.

Logging: This too is a standard library for Python 3 and hence its version will be tied to the installed Python version. It should be compatible with Python 3.7 or higher.

OS: This too is a standard library for Python 3 and hence its version will be tied to the installed Python version. It should be compatible with Python 3.7 or higher.

Threading: This too is a standard library for Python 3 and hence its version will be tied to the installed Python version. It should be compatible with Python 3.7 or higher.

Traceback: This too is a standard library for Python 3 and hence its version will be tied to the installed Python version. It should be compatible with Python 3.7 or higher.

You can check the versions of these libraries installed on your system using the pip show <library_name> command. For instance, to check the version of Biopython, you can use the command pip show biopython.

Please note that for Windows users, all these dependencies are already included in the executable file and do not need to be installed separately.

Dependencies Installation

Linux
Open a terminal and execute the following commands:

![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/259ef10a-2569-464d-8972-fba948fd7a73)

macOS
Open a terminal and execute the following commands:

![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/8a5ab18b-746a-4cab-8f8c-c52b6cf304de)


Usage
After the dependencies have been installed, you can run the program from the terminal:

For Linux/macOS:

![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/5f864f99-a1bb-45bb-8c09-3bb432e6cb50)

Replace "YourUsername" with your actual username.

Run the program with the following command:


![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/1733b874-b4ed-45f7-832c-831f7b0b52fe)


A window will open. Click on the "Select FASTA files" button and choose the FASTA files you wish to convert. The program will start processing the files and you will see the progress bar being updated. When the conversion is complete, the result will be shown in the "Preview" area and a .str file will be saved in the current directory named "Structure.str".
![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/85827670-c6db-4463-b625-f4148fa56d3a)


Windows Version

For users running the Windows operating system, there is no need for a separate installation process. The program is delivered as a standalone executable file that can be run by double-clicking the file. This version includes all the necessary dependencies, so you don't need to install anything separately. Simply download the executable file, and you can start using the program by double-clicking on it.

Remember that the use remains the same: upon opening, a window will appear where you can click on the "Select FASTA files" button and choose the FASTA files you wish to convert. Progress will be displayed in the same way as described above.

Output Examples
Here are some examples of outputs you can expect when using this program.

For the FASTA input:

![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/284fb7e3-9389-417c-b6b9-71d3e2e8db11)

Example files that you can use to test this program are provided in the "Example_data" folder. These files are in FASTA format and can be used to observe how the program functions and to understand the output it generates.

The output will be:

![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/1ba14991-06de-4613-a0bf-f3e2e878b4b3)


Post-Processing Instructions

Once you have used the Fasta to Structure Conversion Tool to process your FASTA files, there's a crucial manual step you need to carry out to complete the data preparation for population genetic analysis. This step involves adding a "Pop ID" to each sample in the output "Structure.str" file.

Understanding Pop ID

A "Pop ID" is a unique identifier given to each sample that indicates which population the sample belongs to. This information is vital for population genetics studies as it allows the software to distinguish between samples from different populations.

The concept of a population is based on the specific research questions and can be influenced by various biological and geographical factors. Populations can be differentiated by criteria such as:

Geographic location: Different populations might be sampled from distinct locations.

Phenotypic characteristics: Observable traits might define different groups within the studied species.

Genetic lineage: Genetic data might suggest distinct lineages that are treated as separate populations.

Ecological niches: Populations might be adapted to different ecological conditions.

Since these criteria are highly specific to the context of each study, the tool leaves the assignment of Pop IDs to the researcher.

Adding Pop IDs Manually
To assign Pop IDs to your data in the "Structure.str" file, you'll need to follow these steps:

Open the Output File:

Open "Structure.str" using a text editor for simple formats or spreadsheet software like Microsoft Excel or Google Sheets for a more tabular format.
Review Your Criteria for Population Assignment:

Before you start editing the file, have a clear understanding of your criteria for defining populations.

Insert Pop IDs:

Add a new column or prepend each line with the Pop ID corresponding to each sample. Ensure that this identifier is consistent for all samples belonging to the same population.

Save Your Changes:

After inserting all Pop IDs, save the file (see Example_data/Results/Structure.str)

For more information on the STRUCTURE software format, please refer to the following link: https://web.stanford.edu/group/pritchardlab/structure.html.

Log File

The program logs information about the conversion process in a log file called log.log. This file logs the variable sites for each processed FASTA file and any errors that may have occurred during the conversion. You can check this file for more information if something goes wrong. The entries in the log file follow the format %(name)s - %(levelname)s - %(message)s and are written at the INFO logging level. This means that all messages at the INFO, WARNING, ERROR, and CRITICAL levels will be logged.

Example of a log file entry:

![image](https://github.com/AdamBessa/Fasta2Structure/assets/16911690/b10b922b-ed42-481b-afd8-7e035c760732)


Maintenance

1.	Program Maintenance: 

• Bug Fixes: 

Any bugs reported by users or identified by the program developer will be investigated and resolved by the developer. The frequency of bug fixes will be determined by the severity of the bug and its impact on the program's functionality. 

• Updates and Enhancements: 

Updates will be carried out as necessary to maintain the program's efficiency. Enhancements may include adding new features, performance upgrades, and user interface updates. 

• Dependencies: 

This program relies on the BioPython module and the Tkinter library for Python. These dependencies will be monitored for any updates. If these libraries are updated, the program will be tested with the new versions to ensure compatibility.

2.	User Feedback: 

• User feedback is crucial for the continuous improvement of the program. A forum will be established on Google Groups (https://groups.google.com/g/fasta2structure) to facilitate communication with users. The developer will monitor this forum and consider inquiries and suggestions for program improvement.

4.	Documentation: 

•The program's documentation will be maintained and updated as necessary.

5.	Testing: 

•After each update or bug fix, tests will be conducted to ensure that the program is still functioning as expected. The tests will include basic functionality, usability testing, and stress testing.

These maintenance procedures will be reviewed and updated as necessary to ensure continuous and efficient functionality.





