import os, ssl, pymongo

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", default="123456789asdasdasdfdh")
    AUTH_TOKEN = os.environ.get("AUTH_TOKEN", default="123456789asdasdasdfdh")


class DevelopementConfig(BaseConfig):
    DEBUG = True
    DB_NAME_MONGO = "userdata"

    template = "mongodb://{user}:{password}@{hosts}/"
    connection = template.format(
        user="root",
        password="password",
        hosts="localhost",
    )
    db = pymongo.MongoClient(connection)[DB_NAME_MONGO]


# class ProductionConfig(BaseConfig):
#     DEBUG = False
#     DB_NAME_MONGO = os.environ.get("DB_NAME_MONGO")

#     template = "mongodb://{user}:{password}@{hosts}/"
#     connection = template.format(
#         user=os.environ.get("USER_MONGO"),
#         password=os.environ.get("PASSWORD_MONGO"),
#         hosts=os.environ.get("HOST_MONGO"),
#     )
#     db = pymongo.MongoClient(
#         connection,
#         ssl_ca_certs=os.environ.get("CERT_MONGO"),
#         ssl_cert_reqs=ssl.CERT_REQUIRED,
#     )[DB_NAME_MONGO]
