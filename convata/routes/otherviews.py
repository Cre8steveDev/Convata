"""Definition of routes to separate the logic into multiple files"""

import json
from flask import Blueprint, request, render_template, redirect, url_for

from ..utils.vars import TOOLS, FEATURES


# Create an instance of the blueprint that will be used 
# In defining your routes 

# The name you give the blueprint is how you will refer to the 
# functions when you use url_for("name_of_function") instead of 
# the route itself

otherviews = Blueprint("otherviews1", __name__)


# Create route for the home page
@otherviews.route("/about-us", strict_slashes=False)
def about_us():
    """About Page View"""
    
    return {"name": "Will Soon Implement the About us Page!"}


# Create route for Upload of file
@otherviews.route("/pdf_summarizer", strict_slashes=False, methods=["POST", "GET"])
def pdf_summarizer():
    """PDF Summarizer logic"""
    # return {"name": "THE PDF SUMMARIZER PAGE"}
    return redirect("https://google.com")

