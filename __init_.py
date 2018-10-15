from flask import Flask
from flask_restful import Api

#local import
import config


#wraps flask oject and returns it after being loaded with necessary files
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config)

    api=Api(app)

    return app
