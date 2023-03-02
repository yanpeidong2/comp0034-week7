# Flipped activities for COMP0034 2022-23 Week 7

## Set-up

1. You will need to a Python environment e.g [create](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) and [activate](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment) a venv.

2. Make sure you venv (or alternative) is Active. Then install the Python packages using the requirements.txt file in the environment, e.g. `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

3. Install the editable project code, e.g. `pip install -e .`

NOTE: If at step 1 above if you wish to use `poetry` rather than `venv`, then rename `pyproject.txt` to `pyproject.toml` first.

## Dataset

The paralympic dataset was published with a CC0: Public Domain license. No attribution required.

## Week 6 solutions

Possible solutions to the activities from week 6 are included in the following folders:

`flask_app` contains a worked solution to the configuration activitity and the activity to create a homepage using HTML and bootstrap CSS.

To run the flask app from the subdirectory:

```terminal
python -m flask --app 'flask_app:create_app()' --debug run
```

`flask_bp` contains a worked solution using optional blueprint and configuring Flask environments activity.

To run the flask app from the subdirectory:

```terminal
python -m flask --app 'flask_bp:create_app()' --debug run
```

## Week 7 activities

The activities are accessed from [activities/activities.md](/activities/activities.md)

There are two versions, the `iris_app` version focuses on a machine learning app; the `paralypic_app` version focuses on a REST API app.

To run these starter code for these two flask apps from the subdirectories:

```terminal
python -m flask --app 'iris_app:create_app()' --debug run
```

```terminal
python -m flask --app 'paralympic_app:create_app()' --debug run
```
