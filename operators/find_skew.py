from ctypes import *

import ctypes
import numpy as np


lept_impl = None


def init(path):
    global lept_impl
    lept_impl = cdll.LoadLibrary(path)
    lept_impl.findskew.restype = ctypes.c_float
    lept_impl.findskew.argtypes = [c_char_p, c_int, c_int]


#use leptonica function,packaged by C++
def find_by_text(image_gray):
    if lept_impl is None:
        return None
    height, width = image_gray.shape
    array_gray = np.asarray(image_gray)
    dataptr = array_gray.ctypes.data_as(ctypes.c_char_p)
    skew_angle = lept_impl.findskew(dataptr, width, height)
    return skew_angle