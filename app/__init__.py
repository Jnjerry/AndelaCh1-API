from flask import Flask
from flask_restful import Api


import config



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)



    return app
