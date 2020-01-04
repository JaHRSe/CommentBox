from .base import *

DEBUG = False

CELERY_BROKER_URL = 'redis://localhost:6379/0'

ALLOWED_HOSTS= ['eadscommentbox.herokuapp.com',]