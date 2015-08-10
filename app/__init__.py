import config
import pkgutil
import importlib
from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy


def create_app(package_name=__name__, package_path=__path__, static_folder='static', template_folder='templates', **config_overrides):
    """
    Create an instance of the application.
    """
    app = Flask(package_name,
                static_url_path='/static',
                static_folder=static_folder,
                template_folder=template_folder)

    app.config.from_object(config)

    # Apply overrides.
    app.config.update(config_overrides)

    # Register blueprints.
    register_blueprints(app, package_name, package_path)

    SQLAlchemy(app)

    return app


def register_blueprints(app, package_name, package_path):
    """
    Register all Blueprint instances on the
    specified Flask application found
    in all modules for the specified package.
    """
    results = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            results.append(item)
    return results