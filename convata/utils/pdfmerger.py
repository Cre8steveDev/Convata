"""Merge pdf function handler. Receives the request object and works
With the files the user wants to merge 
"""

from flask import request
from pypdf import PdfWriter
from datetime import datetime

def pdf_merger(file_array: list):
    """Merges files received from the file path"""
    pass

def handle_merge_pdf(request):
    """This function will handle the pdf merge operation"""
    file1 = request.files["first"]
    file2 = request.files["second"]
    file3 = request.files["third"]
    
    files_array: list = []
    files_array.append(file1)
    files_array.append(file2)
    
    if file3.filename != "":
        files_array.append(file3)
    
    # Instantiate the pdf merger class
    merger = PdfWriter()
    
    for pdf in files_array:
        merger.append(pdf)
    
    # Write merged file to /tmp/ directory
    time_string = datetime.now().strftime("%H-%M-%S-%f")
    filename = f"convata_merged-pdf_{time_string}.pdf"
    
    merger.write("/tmp/" + filename)
    merger.close()
    
    return filename
