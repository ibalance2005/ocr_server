from flask import Flask
from flask_cors import CORS

import config as C, loggers
from servers import index
from servers.api import ocr_traditional


def init():
    loggers.init()

    static_url = ''
    static_dir = C.resource_path('center/servers/api/fe')

    app = Flask(
        __name__,
        static_url_path = static_url, static_folder=static_dir
    )

    app.secret_key = 'cmbc06dhcn83hzm2013dhucn06dsfn05'
    app.logger.debug(f'App config:{app.config}')
    app.logger.debug(f'static url path:{static_url}')
    app.logger.debug(f'static folder:{static_dir}')

    index.init_app(app)

    ocr_traditional.init_ocr()
    ocr_traditional.api.init_app(app)

    CORS(app, resources=f'{C.API_URL_PREFIX}/*')

    return app