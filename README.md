# Flipped activities for COMP0034 2022-23 Week 7

## Set-up

1. You will need to a Python environment e.g create and activate a venv.

2. Install the Python packages using the requirements.txt file in the environment, e.g. `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

3. Install the editable project code, e.g. `pip install -e .`

NOTE: If at step 1 above if you wish to use `poetry` rather than `venv`, then create a `pyproject.toml` file, e.g.

```toml
[tool.poetry]
name = "comp0034-week7"

[tool.poetry.dependencies]
python = "^3.7"
flask = "^2.2.2"

[tool.poetry.dev-dependencies]
pytest = "^4.6"
pylint = "^2.16"
black = "^23.1.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

```

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
