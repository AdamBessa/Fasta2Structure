import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from Bio import AlignIO
import os
import threading
import traceback


def convert_to_binary(sequence):
    binary_mapping = {'A': '0 ', 'T': '1 ', 'C': '2 ', 'G': '3 ', '-': '-9 ', '?': '-9 '}
    return ' '.join([binary_mapping.get(base, '-9') for base in sequence])


def get_variable_sites(alignment):
    variable_sites = []
    for i in range(alignment.get_alignment_length()):
        column = alignment[:, i]
        if len(set(column)) > 1:
            variable_sites.append(i)
    return variable_sites


def process_fasta_file(filepath, sequence_dict, file_count, progress_callback):
    try:
        alignment = AlignIO.read(filepath, "fasta")
        variable_sites = get_variable_sites(alignment)

        for record in alignment:
            variable_site_sequence = ''.join([record.seq[i] for i in variable_sites])
            binary_sequence = convert_to_binary(variable_site_sequence)
            if record.id in sequence_dict:
                sequence_dict[record.id][0] += " " + binary_sequence
                sequence_dict[record.id][1] += 1
            else:
                sequence_dict[record.id] = [binary_sequence, 1]

        variable_sites_count = len(variable_sites)
        progress_callback(variable_sites_count)
        return variable_sites_count
    except:
        traceback.print_exc()
        progress_callback(0)
        return 0


def pad_missing_sequences(sequence_dict, file_count, variable_sites_per_file):
    for seq_id, (binary_sequence, count) in sequence_dict.items():
        missing_count = file_count - count
        if missing_count > 0:
            total_sites = sum(variable_sites_per_file)
            present_sites = sum(variable_sites_per_file[-count:])
            pad_length = total_sites - present_sites
            pad_string = " ".join(["-9"] * pad_length) + " "
            sequence_dict[seq_id][0] += pad_string


def concatenate_results(sequence_dict):
    concatenated_results = []
    for seq_id, (binary_sequence, _) in sequence_dict.items():
        concatenated_results.append(f"{seq_id} {binary_sequence}\n")
    return ''.join(concatenated_results)


def browse_files():
    filepaths = filedialog.askopenfilenames(initialdir=os.getcwd(),
                                            title="Select FASTA file",
                                            filetypes=(("FASTA file", "*.fas"), ("All files", "*.*")))

    if not filepaths:
        return

    sequence_dict = {}
    variable_sites_per_file = []
    progress_value = tk.DoubleVar()
    progress_bar = tk.ttk.Progressbar(root, variable=progress_value, maximum=len(filepaths), mode='determinate')
    progress_bar.pack(pady=10, fill='x')
    progress_label = tk.Label(root, text="")
    progress_label.pack(pady=5)

    def process_files():
        try:
            for i, filepath in enumerate(filepaths):
                variable_sites_count = process_fasta_file(filepath, sequence_dict, len(filepaths),
                                                          lambda value: progress_value.set(i + 1) or progress_label.configure(
                                                              text=f"Processing file {i + 1}/{len(filepaths)} ({value} variable sites)"))
                variable_sites_per_file.append(variable_sites_count)

            pad_missing_sequences(sequence_dict, len(filepaths), variable_sites_per_file)
            concatenated_results = concatenate_results(sequence_dict)

            preview_textbox.configure(state='normal')
            preview_textbox.delete('1.0', tk.END)
            preview_textbox.insert(tk.END, concatenated_results)
            preview_textbox.configure(state='disabled')

            output_filename = "Structure.str"

            with open(output_filename, "w") as output_file:
                output_file.write(concatenated_results)

            output_label.configure(text=f"Converted files saved as: {output_filename}")
            progress_label.configure(text="Conversion completed successfully!")
        except:
            traceback.print_exc()
            progress_label.configure(text="An error occurred during the conversion process.")

    threading.Thread(target=process_files).start()

root = tk.Tk()
root.title("Fasta to Structure")

browse_button = tk.Button(root, text="Select FASTA files", command=browse_files)
browse_button.pack(pady=20)

preview_label = tk.Label(root, text="Preview:")
preview_label.pack()

preview_textbox = ScrolledText(root, height=10)
preview_textbox.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()
