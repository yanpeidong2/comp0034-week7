import pickle
from pathlib import Path
import numpy as np
from flask import render_template, current_app as app


pickle_file = Path(__file__).parent.joinpath("data", "model_lr.pkl")
IRIS_MODEL = pickle.load(open(pickle_file, "rb"))


@app.route("/")
def index():
    """Create home page"""
    return render_template("index.html")


def make_prediction(flower_values):
    """Takes the flower values, makes a model using the prediction and returns a string of the predicted flower variety

    Parameters:
    flower_values (List): List of sepal length, sepal width, petal length, petal width

    Returns:
    variety (str): Name of the predicted iris variety
    """

    # Convert to a 2D numpy array with float values, needed as input to the model
    input_values = np.asarray([flower_values], dtype=float)

    # Get a prediction from the model
    prediction = IRIS_MODEL.predict(input_values)

    # convert the prediction to the variety name
    varieties = {0: "iris-setosa", 1: "iris-versicolor", 2: "iris-virginica"}
    variety = np.vectorize(varieties.__getitem__)(prediction[0])

    return variety
