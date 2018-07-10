from .base import *
from .secrets import *


SECRET_KEY = SECRET_KEY

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
