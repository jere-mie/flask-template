from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import json

# getting config details
with open('config.json') as f:
    data = json.load(f)

# initializing Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

# setting up SQLAlchemy connection (sqlite in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# initializing authentication system
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from website import routes