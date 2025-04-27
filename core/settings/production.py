from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "165.22.124.147",
    "laurencemercer.com",
    "www.laurencemercer.com",
]

try:
    from .local import *
except ImportError:
    pass
