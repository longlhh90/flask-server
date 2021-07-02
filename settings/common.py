import os
from datetime import datetime, time, timedelta

# FLASK CONFIG
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", None)
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")

# API KEYS
API_KEY = os.environ.get("API_KEY", None)

# DATABSE
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True

# JWT AUTH CONFIG
JWT_AUTH_USERNAME_KEY = "email"
JWT_AUTH_PASSWORD_KEY = "password"
JWT_EXPIRATION_DELTA = timedelta(seconds=300)
JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)
