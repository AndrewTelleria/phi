from .base import *
# from .dev import *
import os

# SECRET_KEY = SECRET_KEY

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
