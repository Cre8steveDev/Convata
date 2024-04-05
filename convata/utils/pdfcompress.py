"""Merge pdf function handler. Receives the request object and works
With the files the user wants to merge 
"""

from flask import request
from pypdf import PdfWriter, PdfReader
from datetime import datetime
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from os import environ


def handle_compress_pdf(request):
    """This function will handle the pdf merge operation"""
    file1: FileStorage  = request.files["file"]
    
    compression_rate = request.form.get("level", 0)
    compression_rate = int(compression_rate)
    
    file_name = secure_filename(file1.filename)
    
    upload_path = environ["UPLOADS"]
    save_path = environ["DOWNLOADS"]
    
    file1.save(f"{upload_path}/{file_name}")
    
    time_string = datetime.now().strftime("%H-%M-%S-%f")
    final_file_name = f"convata_compressed_{time_string}.pdf"

    # # Instantiate the pdf merger class
    writer = PdfWriter(clone_from=f"{upload_path}/{file_name}")
  
    # # # Iterate through the pages and compress
    for page in writer.pages:
        page.compress_content_streams(level=compression_rate)

    # # # Write out the compressed file to the /tmp directory
    with open(f"{save_path}/{final_file_name}", "wb") as file:
        writer.write(file)
    
    return final_file_name
