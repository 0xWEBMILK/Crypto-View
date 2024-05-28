# Default imports
from flask import Blueprint


# Root Blueprint
root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/root')
def root_handler():
    return 'Root!'