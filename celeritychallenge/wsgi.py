"""
WSGI config for celerity-challenge project.

"""
# Standard lib imports
import os

# Third party imports
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celeritychallenge.settings")

application = get_wsgi_application()
