# -*- coding: UTF-8 -*-

import cv2


def open(src, size=(5, 5)):
    """
    开运算
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    image = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
    return image


def close(src, size=(5, 5)):
    """
    闭运算
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    image = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
    return image


def erode(src, size=(5, 5)):
    """
    腐蚀
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    image = cv2.erode(src, kernel)
    return image


def dilate(src, size=(5, 5)):
    """
    膨胀
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    image = cv2.dilate(src, kernel)
    return image
