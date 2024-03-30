"""Merge pdf function handler. Receives the request object and works
With the files the user wants to merge 
"""

from datetime import datetime
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from os import environ

from PIL import Image


def handle_image_to_pdf(request):
    """This function will handle the pdf merge operation"""
    file1: FileStorage  = request.files["file"]
    
    desired_filename = request.form.get("filename", "convata")
    desired_filename = secure_filename(desired_filename)
    
    upload_path = environ["UPLOADS"]
    save_path = environ["DOWNLOADS"]
    
    file1.save(f"{upload_path}/{file1.filename}")
    
    time_string = datetime.now().strftime("%H-%M-%S")
    final_file_name = f"{desired_filename}_{time_string}.pdf"
    
    image_conv = Image.open(f"{upload_path}/{file1.filename}")
    new_image = image_conv.convert("RGB")
    
    new_image.save(f"{save_path}/{final_file_name}")
    
    return final_file_name
