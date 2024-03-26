"""Definition of routes to separate the logic into multiple files"""

import json
from flask import Blueprint, request, render_template, redirect
from ..utils.converters import pdf_to_docx
from ..utils.vars import TOOLS, FEATURES


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


# Create route for Upload of file
@convata_views.route("/convert/pdf-docx", strict_slashes=False, methods=["POST", "GET"])
def conv_pdf_docx():
    """Upload file and convert to pdf"""
    document_filename = pdf_to_docx(request)
        
    return {"response_code": 200, "status": "Success"}


@convata_views.route("/convert/merge-pdf", strict_slashes=False, methods=["POST", "GET"])
def merge_pdf():
    """Upload file and convert to pdf"""
    # document_filename = pdf_to_docx(request)
        
    return {"response_code": 200, "status": "Success"}


@convata_views.route("/convert/compress-pdf", strict_slashes=False, methods=["POST", "GET"])
def compress_pdf():
    """Upload file and convert to pdf"""
    # document_filename = pdf_to_docx(request)
        
    return {"response_code": 200, "status": "Success"}


@convata_views.route("/convert/shorten-url", strict_slashes=False, methods=["POST", "GET"])
def shorten_url():
    """Upload file and convert to pdf"""
    # document_filename = pdf_to_docx(request)
        
    return {"response_code": 200, "status": "Success"}

