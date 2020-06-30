from flask import Blueprint, current_app


blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return current_app.send_static_file('index.html')


@blueprint.route('/health.html')
def health():
    return 'I am alive.'


def init_app(app):
    app.register_blueprint(blueprint)