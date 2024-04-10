from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config = False)
    #TODO
    with app.app_context():
        from routes.api import api

        app.register_blueprint(api)
        
    return app