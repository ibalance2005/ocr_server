import ctypes
import numpy as np

from loggers import ocr_log


lib_ocr = None


def init(lib_path, data_path, language):
    global lib_ocr
    lib_ocr = ctypes.CDLL(lib_path)
    lib_ocr.init_ocr.restype = ctypes.c_int
    lib_ocr.ocr.restype = ctypes.c_int
    lib_ocr.ocr_all.restype = ctypes.c_int
    lib_ocr.ocr_all.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float, ctypes.c_char_p, ctypes.c_int)

    data_path = data_path.encode()
    language = language.encode()
    return lib_ocr.init_ocr(data_path, language)


def ocr(image_bin):
    array_gray = np.asarray(image_bin)
    dataptr = array_gray.ctypes.data_as(ctypes.c_char_p)
    buffer_size = 102400
    buffer_h = ctypes.create_string_buffer(buffer_size)
    height, width = image_bin.shape
    lib_ocr.ocr(dataptr, width, height, 1, width, buffer_h, buffer_size)
    buffer_result = str(buffer_h, encoding="utf-8")
    buffer_result = buffer_result.replace(' ', '')
    return buffer_result


def ocr_all(image_bin):
    array_gray = np.asarray(image_bin)
    dataptr = array_gray.ctypes.data_as(ctypes.c_char_p)
    buffer_size = 102400
    buffer_h = ctypes.create_string_buffer(buffer_size)
    height, width = image_bin.shape
    lib_ocr.ocr_all(dataptr, width, height, 1, width, 50.0, buffer_h, buffer_size)
    buffer_result = str(buffer_h, encoding="utf-8")
    words = buffer_result.split('&|')
    words_text = words[0].split(';')[:-1]
    words_centainty = words[1].split(';')[:-1]
    words_centainty = [float(certainty) for certainty in words_centainty]
    words_box = words[2].split(';')[:-1]

    # buffer_result = buffer_result.replace(' ', '')
    return words_text, words_centainty, words_box


def release():
    lib_ocr.release_ocr()