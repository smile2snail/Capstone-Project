# This program serves the following role:
# it contains the application factory, and it tells Python that the flaskr directory should be treated as a package

# run this application (on Linux or Mac) as the following:
# $ export FLASK_APP=__init__.py
# $ export FLASK_ENV=development
# $ flask run
# use 127.0.0.1:5000/music on a browser to view 'Hello, Music!'


import os

from flask import Flask


def create_app(test_config=None):
    # this is an application factory function
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/music')
    def hello():
        return 'Hello, Music!'

    return app
