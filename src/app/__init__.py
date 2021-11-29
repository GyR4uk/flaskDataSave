from flask import Flask

import os, config

# создание экземпляра приложения
app = Flask(__name__)
# app.config.from_object(os.environ.get("FLASK_ENV") or "config.DevelopementConfig")

# import views
from . import views
