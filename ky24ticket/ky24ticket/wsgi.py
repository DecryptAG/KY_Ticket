"""
WSGI config for ky24ticket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('./path/to/venv/lib/python3.11/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ky24ticket.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
