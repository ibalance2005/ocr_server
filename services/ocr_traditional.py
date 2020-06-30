import cv2 as cv
import os

from operators import tesseract_ocr


def ocr_images(files_list):
    if len(files_list) == 0:
        resp = dict(status='ERR', result='', message=f'File list is empty!')
        return resp

    results = dict()
    for image_file in files_list:
        image = cv.imread(image_file)
        if image is None:
            resp = dict(status='ERR', result='', message=f'File {image_file} do not exist!')
            return resp
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image_bin = cv.adaptiveThreshold(image_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 11.0)
        words_text = tesseract_ocr.ocr(image_bin)
        words_text = words_text.replace(u'\u0000', '')

        file_name = os.path.split(image_file)[1]
        short_name = os.path.splitext(file_name)[0]
        results[short_name] = words_text
    resp = dict(status='OK', results=results)
    return resp