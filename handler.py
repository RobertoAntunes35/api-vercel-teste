from flask import request
import os
from app import app

def handler(event, context):
    return app.handle_request()
