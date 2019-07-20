# coding:utf-8
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sfvixfzs',
        'USER': 'sfvixfzs',
        'PASSWORD': 'KI46BG2GOB50sv-9mtR9Wa1S3-fqQXGZ',
        'HOST': 'raja.db.elephantsql.com',
        'PORT': '',
    },
}


DEBUG = True
BASE_URL = 'http://localhost:8000'

# Details
# install devs
# Install requierementes
# migrate
# makemigrate



# Init
# pip install -r requierements.txt
#
# first flow
# python settings/manage.py migrate --settings=settings_staging
# python settings/manage.py runserver --settings=settings_staging
# python settings/manage.py createsuperuser --settings=settings_staging

# create super use
# python settings/manage.py createsuperuser --settings=settings_staging

# Second flow
# python settings/manage.py makemigrations clientes --settings=settings_staging
# python settings/manage.py makemigrations productos --settings=settings_staging
# python settings/manage.py makemigrations pedidos --settings=settings_staging
# python settings/manage.py migrate --settings=settings_staging
# python settings/manage.py runserver --settings=settings_staging
