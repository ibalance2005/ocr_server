import cv2 as cv
import os

from operators import cv_lines, file_opt
import config as C

from .base import *


class CvTest(BT):
    def setUp(self):
        cv_lines.init_lib(C.LIB_PATH_CV)

    def test_cv_lines(self):
        test_path = C.TEST_PATH + 'images/'
        result_path = f'{C.RESULT_PATH}/images/'
        if not os.path.exists(result_path):
            os.makedirs(result_path)

        image_files = file_opt.get_realpaths(test_path)
        for image_file in image_files:
            image = cv.imread(image_file)
            img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            img_bin = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 11.0)
            lines_h, lines_v = cv_lines.find_lines_all(img_bin, 50, 2600)

            image_draw = cv_lines.draw_lines_h(image, lines_h)
            image_draw = cv_lines.draw_lines_v(image_draw, lines_v)

            (folder_path, file_name) = os.path.split(image_file)
            save_name = os.path.join(result_path, file_name)
            cv.imwrite(save_name, image_draw)
