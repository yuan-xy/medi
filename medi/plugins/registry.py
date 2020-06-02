"""
This is not a plugin, this is just the place were plugins are registered.
"""

from medi.plugins import stdlib
from medi.plugins import flask
from medi.plugins import pytest
from medi.plugins import django
from medi.plugins import plugin_manager


plugin_manager.register(stdlib, flask, pytest, django)
