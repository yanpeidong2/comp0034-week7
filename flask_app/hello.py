# The Flask import is no longer required so can be removed.
from flask import Flask, render_template, current_app as app


# Remove this and the subsequent line, left in to show what was here before the Factory Application pattern was applied
# app = Flask(__name__)


@app.route("/")
def index():
    """Generates the home page."""
    # Remove this and the subsequent line, left in to show what was here before render_template was used
    # return "Hello, World!"
    return render_template("index.html")
