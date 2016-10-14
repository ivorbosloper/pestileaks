import os

STATIC_ROOT = '/home/pestileaks/run/static'
DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
