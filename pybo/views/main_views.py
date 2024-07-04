from flask import Blueprint, render_template, url_for
from pybo.model import Question, Answer
from datetime import datetime
from werkzeug.utils import redirect
q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return redirect(url_for('question._list'))