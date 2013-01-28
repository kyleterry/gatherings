from gatherings.settings import *

ADMINS = (
    ('Kyle Terry', 'kyle@kyleterry.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gatherings',
        'USER': 'kyle',
        'PASSWORD': 'testing',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}