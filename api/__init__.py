import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello world!'

    from api.routes import news
    app.register_blueprint(news.bp)

    return app
