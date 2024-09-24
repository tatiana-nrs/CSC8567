from .settings import *

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",
    "rest_framework"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tniauronis', 
        'USER': 'tniauronis',          
        'PASSWORD': 'azerty',          
        'HOST': 'db',                
        'PORT': '5432',                     
}
}

ROOT_URLCONF = "projet.api_urls"