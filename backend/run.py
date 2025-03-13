import os
import sys
import logging
from flask import Flask
from flask_cors import CORS

# Adding logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.api import api

app = Flask(__name__)

# Initializing API
api.init_app(app)

# Enabling CORS with support for credentials
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    # Logging the start of the application
    logger.info("Starting the Flask application")
    app.run(debug=True, port=5000)
    # Logging the shutdown of the application
    logger.info("Shutting down the Flask application")