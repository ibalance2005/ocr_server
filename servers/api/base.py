from flask import Blueprint
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser

import config as C
from loggers import ocr_log


class API(object):
    def __init__(self, name, module):
        blueprint = Blueprint(name, module)
        api = Api(blueprint)
        self.api = api
        self.blueprint = blueprint

    def resource(self, *urls, **kwargs):
        purls = [C.API_URL_PREFIX + u for u in urls]
        ocr_log.debug(f'API urls with prefix:{C.API_URL_PREFIX}')

        def add_resource(r):
            self.api.add_resource(r, *purls, **kwargs)
            return r
        return add_resource

    def init_app(self, app):
        app.register_blueprint(self.blueprint)