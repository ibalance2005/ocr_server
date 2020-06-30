import cv2 as cv
# import fitz
import numpy as np


color_bgr_r = (0, 0, 255)


"""def pdf2img(filename, stream=None, dpi=200, rotate_angle=0, img_type='jpg'):
    if stream is None:
        fitz.open
        pdf_file = fitz.Document(filename)
    else:
        pdf_file = fitz.Document(filename, stream=stream)

    zoom = dpi / 100.0
    trans_param = fitz.Matrix(zoom, zoom).preRotate(rotate_angle)
    images = list()
    for i in range(pdf_file.pageCount):
        page = pdf_file[i]
        img_pix = page.getPixmap(trans_param)
        continue
        img_data = img_pix.getImageData(output=img_type)
        img_array = np.frombuffer(img_data, dtype=np.uint8)
        img_cv = cv.imdecode(img_array, cv.IMREAD_ANYCOLOR)
        images.append(img_cv)
    pdf_file.close()
    return images """


def filter_red(image):
    index = np.logical_and(
        (image[:, :, 2]) > 30,
        (image[:, :, 2]) - 30 > image[:, :, 0],
        (image[:, :, 2] - 40) > image[:, :, 1]
    )

    image[index] = 255
    return image


def rotate_image(img_src, angle):
    height, width, channel = img_src.shape
    matRotate = cv.getRotationMatrix2D((width * 0.5, height * 0.5), angle, 1.0)  # mat rotate 1 center 2 angle 3 缩放系数
    dst = cv.warpAffine(img_src, matRotate, (width, height), borderValue=(0,0,0))
    return dst
