from flask import Flask
import config


def create_app(config_class_name):
    """
    Initialise the Flask application.
    :type config_class_name: Specifies the configuration class
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name)

    # Include the bp_main blueprint for the routes in hello_bp.py
    from flask_bp.hello_bp import bp_main

    app.register_blueprint(bp_main)

    return app
