import os
from flask import Flask, request
from pymongo import MongoClient

client = MongoClient('mongodb://mongodb:27017')
db = client.newsdb


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello world!'

    from api.routes import news
    app.register_blueprint(news.bp)

    return app


def get_arg(key, default):
    arg = request.args.get(key)
    return arg if arg else default
