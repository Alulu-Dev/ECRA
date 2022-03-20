from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from .settings import MONGO_DATABASE
from .apis import api as api_namespace

from .core.model import User

app = Flask(__name__)

app.secret_key = 'd4e290e4d9b2b4c2a75e92418d370a9a'

app.config['MONGODB_SETTINGS'] = {
    'db': MONGO_DATABASE,
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(id=user_id)


api_namespace.init_app(app)

app.run(port=9000, debug=True)
