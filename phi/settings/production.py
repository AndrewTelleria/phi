from .base import *
from .dev import SECRET_KEY

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
