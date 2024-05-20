# Default imports
from flask import Blueprint
from flask import render_template


# Home Blueprint
home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/home')
def home_handler():
    return render_template('index.html')