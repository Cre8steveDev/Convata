"""Utility Functions for Converting files"""
from flask import redirect
from werkzeug.utils import secure_filename
from pdf2docx import Converter


def pdf_to_docx(request):
    """Convert pdf to docx and return the file name"""
    try: 
        # Retrieve the file from the upload
        file = request.files['upload_pdf']
        
        if file.filename.split(".")[-1] != 'pdf':
            return {"response_code": 401, "status": "PDF Files only"}, 401
        
        filename = secure_filename(file.filename)
        
        # Save the pdf to a temporary location
        pdf_path = "/tmp/" + filename
        file.save(pdf_path)

        # Get the start and end points from the form data
        start = int(request.form.get('start', 0))
        end = request.form.get('end')
        
        if end:
            end = int(end)

        # Convert the saved pdf to a docx
        docx_filename = filename.rsplit('.', 1)[0] + '.docx'
        docx_path = "/tmp/" + docx_filename
        
        conv = Converter(pdf_path)
        conv.convert(docx_path, start=start, end=end)
        conv.close()        
        
        return docx_filename
        
    except Exception as e:
        return None