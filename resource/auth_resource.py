from flask import make_response
from flask_restful import Resource, reqparse

class AuthResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', location='form', default=None, help='username')
        self.parser.add_argument('password', location='form', default=None, help='password')

    def post(self):
        make_response('', 401)

    def _get_user_by_username(self, username):
        """
        reads a user by its username
        :param username:
        :return:
        """
        pass