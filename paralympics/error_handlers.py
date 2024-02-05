from flask import json, current_app as app, jsonify, make_response
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import HTTPException


# ERROR HANDLERS

def handle_404_error(e):
    """ Error handler for 404.

        Used when abort() is called. THe custom message is provided by the 'description=' parameter in abort().
        Args:
            HTTP 404 error

        Returns:
            JSON response with the validation error message and the 404 status code
        """
    return jsonify(error=str(e)), 404