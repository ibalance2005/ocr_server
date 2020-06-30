from .base import *


def resource_path(name):
    return P.join(APP_ROOT, name).replace('\\', '/')


WITH_TIME = True

LIB_PATH_LEPT        = resource_path('data/libs/lept_api.so')
LIB_PATH_CV          = resource_path('data/libs/cv_func.so')
LIB_PATH_TESSERACT   = resource_path('data/libs/tesseract_api.so')
TESSERACT_DATA       = resource_path('data/tesseract')
TEST_PATH            = resource_path('tests/')
RESULT_PATH          = resource_path('results/')
IMAGE_BUF            = resource_path('images/')

API_PORT             = 6062
