import os
from django.core.wsgi import get_wsgi_application

import environ
env = environ.Env()
environ.Env.read_env('mysite/.env')
myvar = env('MYVAR')
print("MYVAR wsgi.py ==============> ", myvar)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', myvar)

application = get_wsgi_application()