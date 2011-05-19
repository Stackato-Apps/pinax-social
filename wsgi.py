import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(here, 'apps'))

import django.core.handlers.wsgi as w
application = w.WSGIHandler()

