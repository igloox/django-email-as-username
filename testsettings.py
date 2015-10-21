import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = os.environ.get('SECRET_KEY', 'SeCrEt!')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'emailusernames',
)

AUTHENTICATION_BACKENDS = (
    'emailusernames.backends.EmailAuthBackend',
)
