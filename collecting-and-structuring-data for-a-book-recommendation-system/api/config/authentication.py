import os
import jwt
import json
from flask import Response, request
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')

'''
# TOKEN FORMAT
{
    "iss": domain,
    "exp": expiration
}
'''

@auth.verify_token
def verify_token(jwt_token):
    #print(request.headers)
    secret = os.getenv("JWT_SECRET")
    jwt_decoded = jwt.decode(jwt_token, secret)
    try:
        secret = os.getenv("JWT_SECRET")
        jwt_decoded = jwt.decode(jwt_token, secret)
        return jwt_decoded
    except:
        return False
    return False

@auth.error_handler
def auth_error(status):
    response = json.dumps({
            "error": "Unauthorized",
            "description": 'Authorization not informed, expired or invalid.',
            "status_code": status
        })
    return Response(response, mimetype="application/json", status=status)