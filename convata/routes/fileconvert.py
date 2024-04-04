"""Definition of routes to separate the logic into multiple files"""

import json
from time import sleep
from flask import Blueprint, request, render_template, redirect, url_for
from flask import session, send_from_directory

from ..utils.pdftodocx import pdf_to_docx
from ..utils.pdfmerger import handle_merge_pdf
from ..utils.pdfcompress import handle_compress_pdf
from ..utils.imagetopdf import handle_image_to_pdf

from ..utils.vars import TOOLS, FEATURES

from os import environ


# Create an instance of the blueprint that will be used 
# In defining your routes 

# The name you give the blueprint is how you will refer to the 
# functions when you use url_for("name_of_function") instead of 
# the route itself
convata_views = Blueprint("convata1", __name__)


# Create route for the home page
@convata_views.route("/", strict_slashes=False)
def index():
    """Home Page View"""
    
    return render_template("index.html", tools=TOOLS, features=FEATURES)


# Create route for PDF To Docx Conversion
@convata_views.route("/convert/pdf-docx", strict_slashes=False, methods=["POST", "GET"])
def conv_pdf_docx():
    """Upload file and convert to pdf"""
    # Check if method is GET, then send the form
    if request.method == "GET":
        return render_template("pdftodocx.html")
    
    # At this point, it must be a POST Request for the form
    document_filename = pdf_to_docx(request)
    
    if not document_filename:
        return redirect("/convert/pdf-docx")
    
    # Store the service name for the header on the session object
    session["service_name"] = "Your PDF File has been Converted to Docx!"
    session["description"] = "Thanks for using our free tool. You can download the file to your device by clicking the Download Button Below! ✅"
    
    return redirect("/download/" + document_filename)


# Create route for the Merging of Multiple PDF Files
@convata_views.route("/convert/merge-pdf", strict_slashes=False, methods=["POST", "GET"])
def merge_pdf():
    """Receive the files and save to PDF"""
    
    if request.method == "GET":
        return render_template("mergepdf.html")
    
    # Check if honeypot has a value, then it's bot
    if len(request.form.get("honeypot")) > 0:
        return {"message": "Welldone "}
    
    # Call Function to handle merging and return filename of the merged docx
    document_filename = handle_merge_pdf(request)
    
     # Store the service name for the header on the session object
    session["service_name"] = "Your PDF Files have been Merged!"
    session["description"] = "Thanks for using our free tool. You can download the file to your device by clicking the Download Button Below! ✅"
        
    return redirect("/download/" + document_filename)


#Create route for compressing a PDF File
@convata_views.route("/convert/compress-pdf", strict_slashes=False, methods=["POST", "GET"])
def compress_pdf():
    """Upload file and convert to pdf"""
     
    if request.method == "GET":
        return render_template("pdfcompress.html")
    
    # Check if honeypot has a value, then it's bot
    if len(request.form.get("honeypot")) > 0:
        return {"message": "Welldone "}
    
    # Ensure filesize is not more than 20mb
    file_size = request.files["file"].content_length
    
    if file_size > (20 * 1024 * 1024):
        return {"message": "Sorry, file sizes above 20mb are for Pro Subscribers on our platform. Thanks for understanding"}
    
    
    # Call Function to handle merging and return filename of the merged docx
    document_filename = handle_compress_pdf(request)
    
     # Store the service name for the header on the session object
    session["service_name"] = "File Compression Successful!"
    session["description"] = "Thanks for using our free tool. You can download the file to your device by clicking the Download Button Below! ✅"
        
    return redirect("/download/" + document_filename)



#Create route for Converting Images to PDF File
@convata_views.route("/convert/image-to-pdf", strict_slashes=False, methods=["POST", "GET"])
def imagepdf():
    """Upload file and convert to pdf"""
     
    if request.method == "GET":
        return render_template("imagetopdf.html")
    
    # Check if honeypot has a value, then it's bot
    if len(request.form.get("honeypot")) > 0:
        return {"message": "Welldone "}
    
    # Ensure filesize is not more than 20mb
    file_size = request.files["file"].content_length
    
    if file_size > (20 * 1024 * 1024):
        return {"message": "Sorry, file sizes above 20mb are for Pro Subscribers on our platform. Thanks for understanding"}
    
    
    # Call Function to handle merging and return filename of the merged docx
    document_filename = handle_image_to_pdf(request)
    
     # Store the service name for the header on the session object
    session["service_name"] = "Image Successfully Converted to PDF.😎"
    session["description"] = "Thanks for using our free tool. You can download the file to your device by clicking the Download Button Below! ✅"
        
    return redirect("/download/" + document_filename)


@convata_views.route("/convert/shorten-url", strict_slashes=False, methods=["POST", "GET"])
def shorten_url():
    """Upload file and convert to pdf"""
    # document_filename = pdf_to_docx(request)
        
    return {"response_code": 200, "status": "Will Implement some other time"}


@convata_views.route("/download/<filename>", strict_slashes=False)
def download_page(filename):
    """Receives the file name and creates a button with it"""
    return render_template("downloadpage.html", filename=filename)


@convata_views.route("/file/<filename>", strict_slashes=False)
def download_file(filename):
    """Sends the current file saved in session to the user"""
    return send_from_directory(environ["DOWNLOADS"], filename, as_attachment=True)