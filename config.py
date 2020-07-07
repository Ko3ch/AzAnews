import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_API_BASE_URL ='http://newsapi.org/v2/sources?category={}&apiKey=7f82d84e45d64550bacc0dd3433aae1a'
    NEWS_SOURCE_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=7f82d84e45d64550bacc0dd3433aae1a'
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