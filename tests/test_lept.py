import cv2 as cv
import os

from operators import cv_func, find_skew, file_opt
import config as C

from .base import *


class CvTest(BT):
    def setUp(self):
        find_skew.init(C.LIB_PATH_LEPT)

    def test_cv_lines(self):
        test_path = C.TEST_PATH + 'images/'
        result_path = f'{C.RESULT_PATH}/images/'
        if not os.path.exists(result_path):
            os.makedirs(result_path)

        image_files = file_opt.get_realpaths(test_path)
        for image_file in image_files:
            image = cv.imread(image_file)
            img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            skew_angle = find_skew.find_by_text(img_gray)
            print(f'{image_file}: {skew_angle}')
            (folder_path, file_name) = os.path.split(image_file)
            save_name = os.path.join(result_path, file_name)
            if abs(skew_angle) > 0.2:
                img_rotate = cv_func.rotate_image(image, -skew_angle)
                cv.imwrite(save_name, img_rotate)
