import os
from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# db variable initialization
db = SQLAlchemy()

# Marshmallow initialization
ma = Marshmallow()

# initialize migrate 
migrate = Migrate()

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def create_app():
    news_app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
    news_app.config.from_object(app_config['development'])
    db.init_app(news_app)
    ma.init_app(news_app)
    migrate.init_app(news_app, db)

    from .world_news import cbsnews as world_news_views

    
    news_app.register_blueprint(world_news_views)

    return news_app