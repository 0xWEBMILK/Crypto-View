# Default imports
from flask import Blueprint
from flask import render_template
from flask_cors import cross_origin


# Home Blueprint
home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/home')
@cross_origin()
def home_handler():
    return render_template('index.html')