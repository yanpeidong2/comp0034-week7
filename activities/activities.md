# COMP0034 week 7 activities

Contents:

- [Data sets](#data-sets)

Iris machine learning app activities:

- [Activity 1: Add routes to the Iris ML app (60 mins)](#activity-1-iris-ml-app-create-a-route-to-predict-the-iris-type)
- [Activity 2: Create Jinja templates for the Iris ML app(45 mins)](#activity-2-create-jinja-templates-for-the-iris-ml-app)

Paralympic REST API app activities:

- [Activity 1: Add routes to the Paralympics REST API app (60 mins)](#activity-1-paralympics-rest-api-app-create-skeleton-routes-for-the-rest-api)
- [Activity 2: Create Jinja templates for the REST API app(45 mins)](#activity-2-create-jinja-templates-for-the-rest-api-app)

## Data sets

This week uses two datasets:

1. The paralympics dataset that was prepared in COMP0035. This is use for the REST API app example.
2. The iris dataset. This is used for the ML app example.

There are two sets of starter code and basic folder structure:

1. paralympic_app (REST API app)
2. iris_app (ML app)

This week's tutorial is split into streams focusing on creating a REST API; or a machine learning app.

Before you start the activities, check that the basic apps run. Enter in the VS Code Terminal:

```
python -m flask --app 'paralympic_app:create_app()' --debug run
```

If you try to run two apps on the same port the second app you start will fail with an error message `OSError: [Errno 98] Address already in use`.

To run the second app, state a different port to use. By default, Flask tries port 5000.

```
python -m flask --app 'iris_app:create_app()' --debug run --port 5001
```

You can stop a running Flask app using the 'Ctrl' plus 'C' key in the Terminal in VS Code.

## Activity 1 Iris ML app: Create a route to predict the Iris type

The data folder in the iris app contains a Python script `create_ml_model.py` to create a model using scikit-learn. The resulting model has been saved to the data folder in .pkl format using Pickle.

We don't have scope to teach the creation of models in the course, however if you already have some machine learning knowledge then you are welcome to do so. The PGTAs have some knowledge of creating machine learning models and may be able to support you during the lab session.

Pickle is used after training the model to save it to a file. It uses a process called serialization. Serialization is the process of turning a Python object into a byte stream. The conventional method of serializing objects in Python is by using pickle.

In this activity you will:

- load the pickled model
- create a route that:
  - allows a person to submit am HTTP request with the sepal_length,sepal_width,petal_length,petal_width passed as arguments
  - pass the arguments to the model and get a prediction (classification of Iris type)
  - returns the Iris type as text

Next week, you will build on the basic route to present the user with a form to enter their values and a page returning the results.

1. Load the pickled model as a global variable

The pickled model file has been created for you and is the data folder. The code to generate the file is not taught in the course but is included in [iris_app/data/create_ml_model.py](/iris_app/data/create_ml_model.py).

You will need to install scikit-learn and pandas if you want to run the code in create_ml_model.py. You can do this with `pip install scikit-learn pandas`.

The following code is added to `iris.py` and loads the `model_lr.pkl` file:

```python
from pathlib import Path
import pickle
from flask import render_template, current_app as app, request


pickle_file = Path(__file__).parent.joinpath("data", "model_lr.pkl")
model = pickle.load(open(pickle_file, "rb"))
```

2. Create a route that allows a person to submit an HTTP request with the sepal_length,sepal_width,petal_length,petal_width passed as arguments

To do this you will be using an HTTP GET request and passing arguments in the request.  

To define an [HTTP GET request in Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#http-methods) with a docstring:

```
@app.get("/predict")
def predict():
    """Predict Iris species

    Takes the arguments sepal_length,sepal_width,petal_length,petal_width  from an HTTP request. Passes the arguments to the model and returns a prediction (classification of Iris species).

    Returns:
        species(str): A string of the iris species.
    """

```

You now need to implement the `predict` method.

The first step is to get the values for the sepal_length,sepal_width,petal_length,petal_width which are all float data types that are passed as arguments in the HTTP request.

Flask lets you access the request using the [Flask request object](https://flask.palletsprojects.com/en/2.2.x/api/?highlight=request#flask.request). There is [an example here](https://flask.palletsprojects.com/en/2.2.x/quickstart/#the-request-object) of how to access the parameters submitted in the URL using the args attribute,

The first value is done for you in the code below, you can complete the other three.

```python
from flask import render_template, current_app, request

''' other code ommited here '''

@app.route("/predict", methods=["GET"])
def predict():

    sepal_length = request.args.get("sep-len")
    sepal_width = # add code here
    petal_length = # add code here
    petal_width = # add code here

```

Next add code to get a prediction using the model. You need to pass the 4 values in a list to the `make_prediction()` function that has been added to `iris.py` for you.

Finally, return the prediction value, this will be a string.

```python
from flask import render_template, current_app, request

''' other code ommited here '''

@app.route("/predict", methods=["GET"])
def predict():

    sepal_length = request.args.get("sep-len")
    sepal_width = request.args.get("sep-wid")
    petal_length = request.args.get("pet-len")
    petal_width = request.args.get("pet-wid")

    # Get a prediction by passing a list containing the above 4 variables to the make_prediction(flower_values) function

    # Return the prediction value (the prediction value is a string)
```

Run the app: `python -m flask --app 'iris_app:create_app()' --debug run --port 5001`

Enter this URL: `127.0.0.1:5001/predict?sep-len=5.1&sep-wid=3.5&pet-len=1.4&pet-wid=0.2`

You should get a page with a single word which is the prediction of the iris species.

## Activity 2: Create Jinja templates for the Iris ML app

### Create a Jinja base/parent template

Refer to the [Jinja templates documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/) for this activity.

You should already be able to do the following using HTML only:

1. Create an HTML file in the `templates` directory with an appropriate name e.g. layout.html, base.html

2. Add the overall HTML page structure (e.g. head, body)

3. Add the CSS link to the HTML head (e.g. use Bootstrap)
    Hint: If you are using CSS saved in the `static` directory you can reference it using the Flask url_for as follows:
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">

Now add some Jinja code to allow values for each page that will inherit from the base layout:

1. Define the page title as a Jinja variable

`<title>{{ title }}</title>`

2. Define a Jinja block where the body content of the child pages will go, e.g.

`{% block content %}{% endblock %}`

You can't easily test the resulting page yet as it needs to be run as part of the Flask app.

### Modify index.html to inherit from the layout/base template

You no longer need most of the code in index.html as it will be provided by the layout.

You only need to code to:

- inherit the base template e.g. `{% extends 'layout.html' %}`
- set the value of the title variable to "Iris home" e.g. `{% set title = 'Iris Home' %}`
- set the content block to be `<p>"Hello, World!"<p>` (this will be changed in a later step) e.g. `{% block content <p>Hello, World!</p>{% endblock %}`

Your index.html might look like this:

```jinja
{% extends 'layout.html' %} 
{% set title = 'Iris Home' %} 
{% block content %} 
    <p>Hello, World!</p>
{% endblock %}
```

Now you should see Iris home page if you run the app!

In VS Code Terminal enter: `python -m flask --app 'iris_app:create_app()' --debug run`

### Modify the predict route and the index page to show the prediction result

Currently the predict routes returns the text of the result.

You could create a new template for the predict page. However, in this activity, change it so that it shows the result in the index page template instead.

To do this you will need to:

- modify the index.html template to accept a Jinja variable for the prediction_text in the content block
- modify the predict route to return a redirect to the index page with the prediction text

To add a new Jinja variable to index.html, use a similar syntax to the variable that you added to the template for the page title, e.g.

```jinja
{% extends 'layout.html' %}
{% set title = 'Iris Home' %}
{% block content %}

<p>Hello, World!</p>
<p>{{ prediction_text }}</p>

{% endblock %}
```

## Activity 1: Paralympics REST API app: Create skeleton routes for the REST API

### Check the app runs

The starter code for this activity assumes that the REST API code routes will be added to the file `api_routes.py`. There is also a blueprint used to for these routes.

Pages that are generated using the API will be added to `paralympic_routes.py`. No blueprint is used for these.

While all routes could use a Bluepriont, this has not been done so as to provide code example for those students who do not wish to use blueprints in their solution.

Before you start the activities, check that the basic apps run. Enter in the VS Code Terminal:

```
python -m flask --app 'paralympic_app:create_app()' --debug run
```

### Create the routes

Assume that the following routes were designed for the API.

| HTTP method | URL | Body | Response | Where the data is |
|:---- |:---- |:---- |:---- | :---- |
| GET | api/noc | None | Returns a list of NOC region codes with region name and notes | `noc_regions.csv` |
| GET | api/noc/{code} | None | Returns the region name and notes for a given code | `noc_regions.csv` |
| PATCH | api/noc/{code} | Changed fields for the NOC record| Return all the details of the updated NOC record|`noc_regions.csv` | `noc_regions.csv` |
| POST | api/noc | Region code, region name and (optional) notes | Status code 201 if new NOC code was saved. | `noc_regions.csv` |
| DELETE | api/noc/{code} | None | Removes an NOC code and if successful returns  202 (Accepted) | `noc_regions.csv` |
| GET | api/event | None | Returns a list of events with all details | `paralympics.csv` |
| GET | api/event/{event_id} | None | Returns all the details for a given event |`paralympics.csv` |
| POST | api/event | Event details| Status code 201 if new event was saved. |`paralympics.csv` |
| PATCH | api/event/{event_id} | Event details to be updated (specific fields to be passed) | Return all the details of the updated event|`paralympics.csv` |

You will need to refer to the [Flask routing documentation](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing) for this activity. And spefically the subsection on [HTTP routes](https://flask.palletsprojects.com/en/2.2.x/quickstart/#http-methods).

Add the routes to `paralympic_app/api_routes.py`.

At this stage add only a skeleton route. I've returned text rather than a simple 'pass' to help you check the app while you develop it.

The first route is a GET request. The default method for a Flask route is GET so you don't have to explicitly state it, however it is stated below so you can see the full syntax.

```python
from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route('/noc', methods=['GET',])
def noc():
    """Returns a list of NOC region codes with region name and notes """
    return 'Returns a list on NOC codes'
```

Which does the same as:

```python
@bp.route('/noc')
def noc():
    """Returns a list of NOC region codes with region name and notes """
    return 'Returns a list on NOC codes'
```

And you can also use the Flask shortcut method to achieve the same:

```python
@bp.get('/noc')
def noc():
    """Returns a list of NOC region codes with region name and notes """
    return 'Returns a list of NOC codes'
```

Run the app from Terminal in VS Code: `python -m flask --app 'paralympic_app:create_app()' --debug run`

When the app has started, enter the URL `http://127.0.0.1:5000/api/noc`

The second route is also a GET request, however it accepts a parameter for a specific region.

In Flask this is a variable rule route. You pass the variable as an argument to the function.

As the URL without the parameter is the same, `/noc` then you can either add the logic for the second route to the previous route, then in the noc(code) function handle the logic for either case. Since the first route doesn't have a code you'll need to add a default None to ensure that the `noc(code)` function works e.g.

```python
@bp.route('/noc')
@bp.route('/noc/<code>')
def noc(code=None):
    """Returns a list of NOC codes with the country/region name and notes or if a code is passed then returns the details for that code """
    if code:
        return f"The details for {code}."
    else
        return "Returns a list of NOC codes"
```

Alternatively you can create a second separate route, though you'll need a new route function name, e.g.

```python
@app.get('/noc/<code>')
def noc_code(code):
    """Returns the details for a given code """
    return f"The details for {code}."

```

You should not need to restart the app if you ran it in debug mode as Flask should reload once you save the changes.

Enter the URL `http://127.0.0.1:5000/api/noc` which should return "Returns a list of NOC codes"

Enter the URL `http://127.0.0.1:5000/api/noc/GBR` which should return "The details for GBR."

Try and create the rest of the routes using the table at the start.

## Activity 2: Create Jinja templates for the REST API app

You do not need to do this for a pure REST API. However, if you plan to create an app feature that uses your REST API routes then you will need it.

### Create a Jinja base/parent template

Refer to the [Jinja templates documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/) for this activity.

You should already be able to do the following using HTML only:

1. Create an HTML file in the `templates` directory with an appropriate name e.g. layout.html, base.html

2. Add the overall HTML page structure (e.g. head, body)

3. Add the CSS link to the HTML head (e.g. use Bootstrap)
    Hint: If you are using CSS saved in the `static` directory you can reference it using the Flask url_for as follows:
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">

Now add some Jinja code to allow values for each page that will inherit from the base layout:

1. Define the page title as a Jinja variable

`<title>{{ title }}</title>`

2. Define a Jinja block where the body content of the child pages will go, e.g.

`{% block content %}{% endblock %}`

You can't easily test the resulting page yet as it needs to be run as part of the Flask app.

### Modify index.html to inherit from the layout/base template

You no longer need most of the code in index.html as it will be provided by the layout.

You only need to code to:

- inherit the base template e.g. `{% extends 'layout.html' %}`
- set the value of the title variable to "Paralympics Home" e.g. `{% set title = 'Paralympics Home' %}`
- set the content block to be `<p>"Hello, World! (paralympics)` e.g. `{% block content}<p>Hello, World! (paralympics)</p>{% endblock %}`

Your index.html would look like this:

```jinja
{% extends 'layout.html' %} 
{% set title = 'Paralympics Home' %} 
{% block content %} 
    <p>Hello, World!</p>
{% endblock %}
```

Check the app is running. If it has stopped then in VS Code Terminal enter:

`python -m flask --app 'paralympic_app:create_app()' --debug run`

## Knowledge check

- Be able to create routes in Flask that accept one or more HTTP methods
- Be able to create parent and child Jinja/HTML templates
- Be able to create a route that renders a template that contains a Jinja expression
- Know what Jinja expressions and statements are typically used for
- Know how to start defining a route from the REST API design
