#!/usr/bin/env python3
#
# This script takes a PDF file and inserts a blank page between every
# page in the PDF. Output is written to the containing directory of
# the original PDF.

import os

from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import filedialog

# Use TkInter for a quick and easy UI to get the file path.
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

pdf = PdfFileReader(file_path)
    
pdf_writer = PdfFileWriter()

# Add a blank page after every page in the PDF
for page in range(pdf.getNumPages()):
    pdf_writer.addPage(pdf.getPage(page))
    pdf_writer.addBlankPage()

out_dir = os.path.split(file_path)[0]
file_name = os.path.split(file_path)[1][:-4]

out_path = "".join([out_dir, "/{} with blank pages.pdf".format(file_name)])
out_file_path = open(out_path, 'wb')

pdf_writer.write(out_file_path)

# Quit, because this will be ran primarily in terminal as an executable
quit()
