from flask import Blueprint

# Create a blueprint for the routes
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return 'sup'
