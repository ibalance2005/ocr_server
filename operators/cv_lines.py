import ctypes
import cv2 as cv
import numpy as np


lib_impl = None
RESULT_BUFFER_SIZE = 102400


def init_lib(path):
    global lib_impl
    if lib_impl:
        return True
    lib_impl = ctypes.CDLL(path)
    if lib_impl is None:
        return False
    lib_impl.find_lines_h.restype = ctypes.c_int
    lib_impl.find_lines_v.restype = ctypes.c_int
    return True


def draw_lines_h(image, lines):
    point_color = (0, 0, 255)
    thickness = 2
    line_type = cv.LINE_8
    for (average, angle, start, end) in lines:
        point_start = (start, average)
        point_end = (end, average)
        cv.line(image, point_start, point_end, point_color, thickness, line_type)
    return image


def draw_lines_v(image, lines):
    point_color = (0, 255, 0)
    thickness = 2
    line_type = cv.LINE_8
    for (average, angle, start, end) in lines:
        point_start = (average, start)
        point_end = (average, end)
        cv.line(image, point_start, point_end, point_color, thickness, line_type)
    return image


def lines_to_list(lines_str):
    lines_str = lines_str.split(';')
    lines = list()
    for line in lines_str:
        if len(line) is 0:
            continue
        line_param = line.split(',')
        average = int(line_param[0])
        angle = float(line_param[1])
        start = int(line_param[2])
        end = int(line_param[3])
        lines.append((average, angle, start, end))

    return lines


def find_lines_all(image_bin, length_thr_min, length_thr_max):
    height, width = image_bin.shape
    global lib_impl
    if lib_impl is None:
        return None

    array_gray = np.asarray(image_bin)
    dataptr = array_gray.ctypes.data_as(ctypes.c_char_p)
    buffer_size = RESULT_BUFFER_SIZE
    buffer_h = ctypes.create_string_buffer(buffer_size)
    lib_impl.find_lines_h(dataptr, length_thr_min, length_thr_max, width, height, buffer_h, buffer_size)
    buffer_h = str(buffer_h, encoding="utf-8").strip(b'\x00'.decode())
    lines_h = lines_to_list(buffer_h)

    buffer_v = ctypes.create_string_buffer(buffer_size)
    lib_impl.find_lines_v(dataptr, length_thr_min, length_thr_max, width, height, buffer_v, buffer_size)
    buffer_v = str(buffer_v, encoding="utf-8").strip(b'\x00'.decode())
    lines_v = lines_to_list(buffer_v)

    return lines_h, lines_v


#use opencv function,packaged by C++
def find_lines_h(image_bin, length_thr_min, length_thr_max):
    height, width = image_bin.shape
    global lib_impl
    if lib_impl is None:
        return None

    array_gray = np.asarray(image_bin)
    dataptr = array_gray.ctypes.data_as(ctypes.c_char_p)
    buffer_size = RESULT_BUFFER_SIZE
    buffer = ctypes.create_string_buffer(buffer_size)
    result_length = lib_impl.find_lines_h(dataptr, length_thr_min, length_thr_max, width, height, buffer, buffer_size)
    buffer = str(buffer, encoding="utf-8").strip(b'\x00'.decode())
    lines_h = buffer.split(';')

    for line in lines_h:
        if len(line) is 0:
            continue
        line_param = line.split(',')
        average_y = int(line_param[0])
        angle = float(line_param[1])
        left = int(line_param[2])
        right = int(line_param[3])
        print('H', (average_y, angle, left, right))

    return buffer


def find_lines_v(image_bin, length_thr_min, length_thr_max):
    height, width = image_bin.shape
    global lib_impl
    if lib_impl is None:
        return None

    array_gray = np.asarray(image_bin)
    dataptr = array_gray.ctypes.data_as(ctypes.c_char_p)
    buffer_size = RESULT_BUFFER_SIZE
    buffer = ctypes.create_string_buffer(buffer_size)
    result_length = lib_impl.find_lines_v(dataptr, length_thr_min, length_thr_max, width, height, buffer, buffer_size)
    buffer = str(buffer, encoding="utf-8").strip(b'\x00'.decode())
    lines_v = buffer.split(';')

    for line in lines_v:
        if len(line) is 0:
            continue
        line_param = line.split(',')
        average_y = int(line_param[0])
        angle = float(line_param[1])
        left = int(line_param[2])
        right = int(line_param[3])
        print((average_y, angle, left, right))

    return buffer
