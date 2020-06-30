from threading import Thread
import cv2 as cv
import time

import config as C
from operators import tesseract_ocr

from .base import *


def tesseract_run(path, thd_number):
    time_start = time.time()
    image = cv.imread(path)
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_bin = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 11.0)
    img_bin_normal = cv.resize(img_bin, (0, 0), fx=2.0, fy=2.0, interpolation=cv.INTER_CUBIC)
    print(f'{thd_number} Load image time = {time.time() - time_start}')

    time_start = time.time()
    words_text = tesseract_ocr.ocr(img_bin_normal)
    print(f'{thd_number} Ocr image time = {time.time() - time_start}')
    print(words_text)


class CvTest(BT):
    def tearDown(self):
        pass

    def test_tesseract(self):
        time_start = time.time()
        tesseract_ocr.init(C.LIB_PATH_TESSERACT, C.TESSERACT_DATA, 'chi_sim')
        print(f'Init time = {time.time()-time_start}')

        image_path = f'{C.TEST_PATH}/images/ocr01.jpg'
        thread_count = 1
        thread_list = []
        for i in range(thread_count):
            thread_ocr = Thread(target=tesseract_run, args=(image_path, f'{i+1}'))
            thread_list.append(thread_ocr)
            thread_ocr.start()
        for t in thread_list:
            t.join()

        tesseract_ocr.release()
