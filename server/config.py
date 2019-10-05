import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Base Config Class
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''


class ProductionConfig(Config):
    """
    Production Config
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development Env Config
    """
    DEBUG = True
    TESTING = True