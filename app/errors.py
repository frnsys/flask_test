from flask import Blueprint

# Create another blueprint for error handling
bp = Blueprint('errors', __name__)


@bp.app_errorhandler(404)
def not_found(error):
    return 'uh oh 404', 404


@bp.app_errorhandler(500)
def internal_error(error):
    return 'uh oh 500!!', 500
