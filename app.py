from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resource.auth_resource import AuthResource


def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    CORS(app)
    app.config.from_pyfile('./.env')
    api = Api(app)

    api.add_resource(AuthResource, '/login')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

