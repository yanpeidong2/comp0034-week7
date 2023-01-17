from flask import Flask


def create_app():
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "add_your_key_here"

    # Include the routes from hello.py
    # Application contexts are explained in a later week
    with app.app_context():
        from flask_app import hello

    return app
