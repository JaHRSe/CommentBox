from .base import *

DEBUG = False

CELERY_BROKER_URL = 'redis://localhost:6379/0'

ALLOWED_HOSTS= ['eadscommentbox.herokuapp.com', '.eadscommentbox.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d29kp7mhfu4etj",
        "USER": "zhzxexhflkrgsm",
        "PASSWORD": os.environ.get("DATABASE_PASS"),
        "HOST": 'ec2-174-129-33-107.compute-1.amazonaws.com',
        "PORT": "5432",
    }
}

SECURE_SSL_REDIRECT = True

#############
# Celery
#############

CELERY_BROKER_URL = os.environ.get("REDIS_URL")
# CELERY_RESULTS_BACKEND = os.environ.get("REDIS_URL")