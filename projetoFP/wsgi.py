"""
@Jean Lucas Parra
@jeanparra
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoFP.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
