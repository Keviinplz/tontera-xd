from .main import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['http://localhost:8000']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')4aphr)jpgb8j@l3rn%_d-r&ycu^5jp2raa75mtd&@^#!@8_p^'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}