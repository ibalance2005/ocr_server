import config as C
from servers import app


if __name__ == '__main__':
    app_run = app.init()
    app_run.run(host='0.0.0.0', port=C.API_PORT)