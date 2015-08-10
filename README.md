A simple example to demo unit testing and Flask.

It demos using an app factory (`app.create_app`) to create a testing application which can have its config overridden.
Here the dev database config is replaced with the test database config for the unit tests.

It also demos the Flask best-practice of using blueprints to organize things (see `app.errors`, `app.routes`, and `app.register_blueprints`).


## Setup

(built for Python 3, but could be adapted to 2.7)

Install the requirements:

    pip install -r requirements.txt

Run the tests:

    nosetests tests.py