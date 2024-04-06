"""Authentication route for Login; Register and Log Out"""

from flask import request, render_template, url_for
from flask import flash, redirect, Blueprint
from flask_login import login_required, logout_user, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
#from models.user_database import User
from ..models.user_database import User
from datetime import datetime


auth = Blueprint("auth", __name__)

# Create Registration Route for New Users
@auth.route("/register", strict_slashes=False, methods=["POST", "GET"])
def register():
    """User Registration Route"""

    if current_user.is_authenticated:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("register.html")

    # Retrieve User collection 
    from ..models.user_database import user

    # Encrypt user's password before saving to database
    user_password = request.form.get("password")
    hashed_password = generate_password_hash(user_password, salt_length=16)

    # Construct expected input from user
    new_user_dict = {
        "username": request.form.get("username"),
        "email": request.form.get("email"),
        "password": hashed_password,
        "profile_picture": url_for("static", filename="avatar.png"),
        "account_balance": 0, 
        "summarized_pdfs": [],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    try:
        test_email = user.find_one({"email": request.form.get("email")})
        test_username = user.find_one({"username": request.form.get("username")})
        
        if test_email or test_username:
            flash("Credentials Already in use!", "error")
            return redirect("/register")
        
        new_user = user.insert_one(new_user_dict)
        return redirect("/login")

    except Exception as e:
        print(e)
        flash("Error occured during registration. Try again!", "error")
        return redirect("/register"), 403


# Create Login Route for New Users
@auth.route("/login", strict_slashes=False, methods=["POST", "GET"])
def login():
    """User Login Route"""
    if current_user.is_authenticated:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("login.html")
    
    # Retrieve User collection 
    from ..models.user_database import user
    
    # Get username and password from the form
    username = request.form.get("username")
    user_password = request.form.get("password")
    
    # Retrieve user from the database with username
    find_user = user.find_one({"username": username})
       
    # Return an error if user not in database
    if find_user == None:
        flash("Invalid Login Credentials!", "error")
        return redirect("/login")

    # Compare the user's password with the password returned from db
    
    is_valid_password = check_password_hash(find_user.get("password"), user_password)
    
    # If password does not match, redirect user to login again
    if not is_valid_password:
        flash("Invalid Login Credentials!", "error")
        return redirect("/login")
        
    # At this point all is well; so instantiate the User class 
    # This is to enable the Flask-Login Extension kick in
    log_user = User(find_user.get("username"), str(find_user.get("_id")))
    
    # use the login_user function from flask_login
    login_user(log_user)

    return redirect("/pdf_summarizer")


# Create Sign Out Route 
@auth.route("/logout", strict_slashes=False)
@login_required
def logout():
    logout_user()
    return redirect("/")

# Dashboard route
@auth.route("/dashboard", strict_slashes=False)
@login_required
def dashboard():
    return """<h1>TODO: Implement the Dashboard view to display User's summary history</h1>
<p><a href='/'>Go back Home</a></p>
"""