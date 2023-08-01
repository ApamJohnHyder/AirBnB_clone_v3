#!/usr/bin/python3
"""
Package initializer for API views.
"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *  # Add this line to import the new State views
