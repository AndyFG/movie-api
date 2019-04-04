class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'A0Zr98j/3yX+R~XHH!jmN]LWX/,?RT'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://near:near@localhost/near'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
