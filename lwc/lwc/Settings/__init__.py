__author__ = 'taiowawaner'

__author__ = 'taiowawaner'

from .base import *

# Look for local file. If found not Live
try:
    from .local import *
    live = False
except:
    live = True

if live:
    from .production import *

