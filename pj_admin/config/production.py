import dj_database_url
from decouple import config

from .main import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')4aphr)jpgb8j@l3rn%_d-r&ycu^5jp2raa75mtd&@^#!@8_p^'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default = config('DATABASE_URL')
    )
}