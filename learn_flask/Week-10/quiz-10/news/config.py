
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/my_database'
    SECRET_KEY = 'mysecretkey'

class DevolpmentConfig(BaseConfig):
    DEBUG = True

class TestConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = True

app_config = {
    'development':DevolpmentConfig,
    'testing':TestConfig,
    'production':ProductionConfig
}