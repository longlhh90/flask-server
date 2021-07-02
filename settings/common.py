import os
from datetime import datetime, timedelta

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
