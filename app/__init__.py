from flask import Flask
# from ..config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# from app import views
# from app import error

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config
    from .request import configure_request
    configure_request(app)

    #will add the views and forms
    return app

#initializing application
#   app = Flask(__name__)#rachel(variable)=Flask

#setting up configuration
# app.config.from_object(DevConfig) #rachel.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

#Initializing flask Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error