"""
WSGI config for ignition2021 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/ignition2021')
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ignition2021.settings")

application = get_wsgi_application()
