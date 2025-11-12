"""
Flask Application Entry Point
"""
from service import app

# Export the app for Flask CLI and WSGI servers
__all__ = ['app']


