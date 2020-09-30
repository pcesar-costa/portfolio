import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

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

if __name__ == "__main__":
    app.run(debug=True)