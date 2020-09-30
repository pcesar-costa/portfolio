import os
import json
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask import request, Response
from werkzeug.exceptions import HTTPException

from resources import Books
from resources import BooksStars
from resources import GenerateToken

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(35)
CORS(app)
rest = Api(app)

rest.add_resource(GenerateToken, '/token')
rest.add_resource(Books, '/books')
rest.add_resource(BooksStars, '/bookstars')

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = json.dumps({"status": 404, "error": "Not found", "description": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."})
    return Response(response, mimetype="application/json", status=400)

if __name__ == "__main__":
    app.run(debug=True)