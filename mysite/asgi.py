"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

import environ
env = environ.Env()
environ.Env.read_env('mysite/.env')
myvar = env('MYVAR')
print("MYVAR wsgi.py ==============> ", myvar)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', myvar)

application = get_asgi_application()