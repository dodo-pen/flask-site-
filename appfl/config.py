from appfl.tt import ps
class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ps  #mysql+mysqlconnector://user:password@host/db
    SQLALCHEMY_NATIVE_UNICODE = True