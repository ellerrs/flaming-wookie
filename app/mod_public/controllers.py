# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_public = Blueprint('public', __name__, url_prefix='/public')

# Set the route and accepted methods
@mod_public.route('/test/', methods=['GET', 'POST'])
def index():
    return render_template("public/index.html")
