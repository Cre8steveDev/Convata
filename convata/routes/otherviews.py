"""Definition of routes to separate the logic into multiple files"""

import json
from flask import Blueprint, request, render_template, redirect
from flask import flash, url_for

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
    return redirect("/register")


# Create Registration Route for New Users
@otherviews.route("/register", strict_slashes=False, methods=["POST", "GET"])
def register():
    """User Registration Route"""
    if request.method == "GET":
        return render_template("register.html")
    
    # Retrieve User collection 
    from ..models.user_database import user
    
    # Encrypt user's password before saving to database
    user_password = request.form.get("password")
    hashed_password = user_password + "TADA"
    
    # Construct expected input from user
    new_user_dict = {
        "name": request.form.get("username"),
        "email": request.form.get("email"),
        "password": hashed_password,
        "profile_picture": url_for("static", filename="avatar.png"),
        "account_balance": 0, 
        "summarized_pdfs": [],
    }
    try:
        new_user = user.insert_one(new_user_dict)
        print(new_user)
    except Exception as e:
        print(e)
    
    

# Create Login Route 


# Create Sign Out Route 

