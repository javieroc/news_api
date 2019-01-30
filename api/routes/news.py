from flask import Blueprint, request
from bson.json_util import dumps
from bson.objectid import ObjectId
import numpy as np
from .. import db, get_arg

bp = Blueprint('news', __name__)


@bp.route('/news', methods=['GET'])
def get_news():
    page = int(get_arg('page', 1))
    per_page = int(get_arg('per_page', 10))

    news = db.news.find().skip(per_page * (page - 1)
                               ).limit(per_page).sort([('date', -1)])

    news_count = db.news.count()

    return dumps({
        "data": news,
        "page": page,
        "per_page": per_page,
        "pages": int(np.ceil(news_count / per_page)),
        "total": news_count
    })


@bp.route("/news/<id>", methods=["GET"])
def get_provider(id):
    new = db.news.find_one({"_id": ObjectId(id)})

    return dumps({
        "data": new
    })
