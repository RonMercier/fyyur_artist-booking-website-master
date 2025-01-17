import os

from settings import DB_NAME, DB_PASSWORD, DB_USER

SECRET_KEY = os.urandom(32)
# Retrieves the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enables debug mode.
DEBUG = True

# DATABASE URL - Used to connect to the database
SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{hostname}:5432/{database_name}'

SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
