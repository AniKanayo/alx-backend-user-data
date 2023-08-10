#!/usr/bin/env python3
"""
Flask blueprint for defining API endpoints.
"""

from flask import Blueprint, abort

blueprint = Blueprint("index", __name__)

@blueprint.route("/unauthorized")
def unauthorized_endpoint():
    """
    Endpoint to trigger a 401 Unauthorized error.
    """
    abort(401)

# Other endpoints can be added here
