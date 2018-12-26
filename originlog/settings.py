import os


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key_default')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'TestingConfig': TestingConfig,
    'Production': ProductionConfig
}
