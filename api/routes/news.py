from flask import Blueprint
from bson.json_util import dumps
from .. import db

bp = Blueprint('news', __name__)


@bp.route('/news', methods=['GET'])
def get_news():
    news = db.news.find().limit(10)
    return dumps(news)
