from flask import Flask
from .route import  init_image_route

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    init_image_route(app,'/image')
    return app