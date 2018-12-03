from flask import Blueprint

bp = Blueprint('news', __name__)

@bp.route('/news', methods=['GET'])
def get_news():
  return 'Hello news test!'
