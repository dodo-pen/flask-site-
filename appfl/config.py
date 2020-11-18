from appfl.password import password


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://myshop_user:*****@192.168.100.214/mydb'
    SQLALCHEMY_NATIVE_UNICODE = True