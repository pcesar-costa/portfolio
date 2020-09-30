import os
import jwt
import json
import datetime as dt
from pymongo import MongoClient
from flask_restful import Resource
from flask import request, Response

from config.authentication import auth
from config.mongodb import mongo

class GenerateToken(Resource):
    def get(self):
        secret = os.getenv("JWT_SECRET")
        exp = dt.datetime.now() + dt.timedelta(hours=1)
        jwt_token = jwt.encode({'iss': 'pedro-costa.wtf', 'exp': exp}, secret, algorithm='HS256').decode("utf-8")
        response = json.dumps({'token': jwt_token, 'exp': exp.strftime("%Y-%m-%d %H:%M:%S")})
        return Response(response, mimetype="application/json", status=200)

class Books(Resource):
    @auth.login_required
    def get(self):
        args = request.args
        if 'title' not in args and 'category' not in args:
            response = json.dumps({"status": 400, "error": "Bad Request", "description": "*title* or *category* param not informed in query."})
            return Response(response, mimetype="application/json", status=400)
        else:
            query = dict(args)
            params = {'_id': 0, 'qty_in_stock': 0, 'in_stock': 0, 'url': 0}
            [query.pop(k) for k in dict(args) if k not in ['title', 'category']]
            book_info = [r for r in mongo.books.find(query, params)]

            response = json.dumps({
                'query': query,
                'data': book_info
            })
            return Response(response, mimetype="application/json", status=200)

class BooksStars(Resource):
    @auth.login_required
    def get(self):
        args = request.args
        if ('min' not in args and 'max' not in args):
            response = json.dumps({"status": 400, "error": "Bad Request", "description": "*min* or *max* param not informed in query."})
            return Response(response, mimetype="application/json", status=400)
        else:
            try:
                min_stars = 0 if 'min' not in args else int(args['min'])
                max_stars = 5 if 'max' not in args else int(args['max'])
            except:
                response = json.dumps({"status": 400, "error": "Bad Request", "description": "*min* or *max* param is not a integer."})
                return Response(response, mimetype="application/json", status=400)

            query = { 'stars': { '$lt': max_stars, '$gt': min_stars }}
            params = {'_id': 0, 'qty_in_stock': 0, 'in_stock': 0, 'url': 0}
            book_info = [r for r in mongo.books.find(query, params)]

            response = json.dumps({
                'query': query,
                'data': book_info
            })
            return Response(response, mimetype="application/json", status=200)