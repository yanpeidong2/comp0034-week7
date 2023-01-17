from flask import Flask


def create_app():
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "add_your_secret_key_here"

    with app.app_context():
        from iris_app import iris

    return app
