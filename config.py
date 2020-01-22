import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'concat-list.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    DEBUG = False


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
    