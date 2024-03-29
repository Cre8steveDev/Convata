"""Merge pdf function handler. Receives the request object and works
With the files the user wants to merge 
"""

from flask import request
from pypdf import PdfWriter, PdfReader
from datetime import datetime
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def handle_image_to_pdf(request):
    """This function will handle the pdf merge operation"""
    file1: FileStorage  = request.files["file"]
    
    desired_filename = request.form.get("filename", "convata")
    desired_filename = secure_filename(desired_filename)
    
    file1.save(f"/tmp/{desired_filename}")
    
    time_string = datetime.now().strftime("%H-%M-%S-%f")
    final_file_name = f"convata_compressed_{time_string}.pdf"
    
    # # Instantiate the pdf merger class
    writer = PdfWriter(clone_from=f"/tmp/{file_name}")
  
    # # # Iterate through the pages and compress
    for page in writer.pages:
        page.compress_content_streams(level=compression_rate)
            
    # # # Write out the compressed file to the /tmp directory
    with open(f"/tmp/{final_file_name}", "wb") as file:
        writer.write(file)
    
    return final_file_name
