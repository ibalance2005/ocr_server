from datetime import datetime
import cv2 as cv
import os

from operators import tesseract_ocr
from services import file_transfer, ocr_traditional
import config as C

from .base import API, Resource, RequestParser


api = API('ocr', __name__)


def init_ocr():
    tesseract_ocr.init(C.LIB_PATH_TESSERACT, C.TESSERACT_DATA, 'chi_sim')


@api.resource('/ocr_tratitional/chi_all')
class AuthCert(Resource):
    def post(self):
        args = self.parse_post_args()

        image_buf_path = datetime.now().date()
        save_path = f'{C.IMAGE_BUF}/{image_buf_path}'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        files_list = file_transfer.save_files(save_path)
        if len(files_list) == 0:
            image_name = args.get('image_name')
            image_path = os.path.join(C.IMAGE_BUF, image_name)
            if os.path.exists(image_path):
                files_list.append(image_path)
        resp = ocr_traditional.ocr_images(files_list)
        return resp


    def parse_post_args(self):
        paster = RequestParser()
        paster.add_argument('image_name', type=str, required=False)
        rqargs = paster.parse_args()
        return rqargs