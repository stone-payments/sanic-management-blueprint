"""A module with the sole purpose of running the Sanic Web API."""
import os

from api import create_api

if __name__ == "__main__":
    API = create_api()
    API.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
