from .base import *

debug=True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cqzah9qnqq()2r^@n0nm9vaivv=y8@v6u#z9im6pqm9ovon1vc'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'commentbox',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

