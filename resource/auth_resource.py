import json

from Crypto.Hash import SHA256
from flask import make_response
from flask_restful import Resource, reqparse

from model.user import User


class AuthResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', location='form', default=None, help='username')
        self.parser.add_argument('password', location='form', default=None, help='password')

    def post(self):
        return make_response('', 401)

    def _get_user_by_username(self, username):
        """
        reads a user by its username
        :param username:
        :return:
        """
        with open('./files/users.json', encoding='UTF-8') as file:
            users_dict = json.load(file)
            for data in users_dict:
                if data['username'] == username:
                    user = User(
                        username=data['username'],
                        password=data['password'],
                        role=data['role']
                    )
                    return user

            return None

    def _password_hash(self, password):
        """
        creates the password hash
        :param password:
        :return:
        """
        hash_object = SHA256.new(data=password.encode())
        return hash_object.hexdigest()

    def _make_token(self, user):
        """
        creates the signed and encrypted token for a user
        :param user:
        :return:
        """
        access = None
        return access
