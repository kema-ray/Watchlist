#  from instance.config import MOVIE_API_KEY
import os #aloow our application to interact with the os dependent functionality

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:hotspurs@localhost/watchlist'
#os.environ.get function to get SECRET_KEY and MOVIE_API_KEY which we will set as environment variables.
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = { #is a dictionaryto help us to access different configuration option classes.
'development':DevConfig,
'production':ProdConfig
}