import logging
import os


LOG_LEVEL = logging.DEBUG


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(processName)s.%(threadName)s:%(message)s', level=LOG_LEVEL)

root = logging.getLogger()

ocr_log = logging.getLogger('api')


def init(path=None):
    if not path:
        return True
    folder = os.path.split(path)[0]
    if not os.path.exists(folder):
        os.mkdir(path)

    hander = logging.FileHandler(path)
    hander.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(processName)s - %(threadName)s - %(message)s')
    hander.setFormatter(formatter)
    ocr_log.addHandler(hander)