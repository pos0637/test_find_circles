# -*- coding: UTF-8 -*-

import cv2
import numpy as np
import math


def getROI(src, left, top, width, height, fx=1, fy=1):
    image = src[top:top + height, left:left + width]
    image = cv2.resize(image, (0, 0), fx=fx, fy=fy,
                       interpolation=cv2.INTER_AREA)
    return image


def getROI2(src, fx=1, fy=1):
    image = cv2.resize(src, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
    return image


def transfrom(src, offsetX, offsetY, width, height):
    matrix = np.float32([[1, 0, offsetX], [0, 1, offsetY]])
    return cv2.warpAffine(src, matrix, (width, height))


def rotate(src, angle, center=None, scale=1.0):
    (height, width) = src.shape[:2]
    if center is None:
        center = (width / 2, height / 2)

    matrix = cv2.getRotationMatrix2D(center, angle, scale)

    return cv2.warpAffine(src, matrix, (width, height))


def rotate2(src, angle, center=None, scale=1.0):
    (height, width) = src.shape[:2]
    w = int(math.sqrt(width * width + height * height))
    src = transfrom(src, (w - width) / 2, (w - height) / 2, w, w)
    if center is None:
        center = (w / 2, w / 2)

    matrix = cv2.getRotationMatrix2D(center, angle, scale)

    return cv2.warpAffine(src, matrix, (w, w))


def rotate3(src, angle, center=None, scale=1.0):
    src = rotate2(src, angle, center, scale)
    contours, _ = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = cv2.boundingRect(contours[0])
    return src[y:y + h, x:x + w]
