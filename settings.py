class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:230809@127.0.0.1:3306/news'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    ENV = 'development'


class ProConfig(Config):
    ENV = 'production'
    DEBUG = False
