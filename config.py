import os

class Config:

    PITCH_API_BASE_URL = 'https://api.thepitchdb.org/3/pitch/{}?api_key={}'
    PITCH_API_KEY = os.environ.get('PITCH_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:flora123@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):
    pass




class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:flora123@localhost/watchlist'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:flora123@localhost/watchlist'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
