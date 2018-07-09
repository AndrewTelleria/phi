from .base import *
import os


SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
