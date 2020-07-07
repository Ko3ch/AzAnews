import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        The parent configuration class with the General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        The parent configuration class with the General configuration settings
    '''
    pass

    DEBUG =  True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}