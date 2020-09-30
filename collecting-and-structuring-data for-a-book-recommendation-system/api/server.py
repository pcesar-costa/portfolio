import os
import app
from waitress import serve
from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv("PORT")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=PORT)