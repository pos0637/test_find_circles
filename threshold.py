# -*- coding: UTF-8 -*-

import cv2


def binary(src, threshold, max=255):
    """
    像素点灰度值大于阈值变为255，小于阈值变为0
    """
    _, image = cv2.threshold(src, threshold, max, cv2.THRESH_BINARY)
    return image


def tozeroInv(src, threshold, max=255):
    """
    像素点灰度值大于阈值不变，小于阈值变为0
    """
    _, image = cv2.threshold(src, threshold, max, cv2.THRESH_TOZERO_INV)
    return image


def binaryOtsu(src, threshold, max=255):
    """
    像素点灰度值大于阈值变为255，小于阈值变为0
    """
    image = cv2.GaussianBlur(src, (3, 3), 0)
    _, image = cv2.threshold(image, threshold, max, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return image


def adaptive(src, max=255):
    """
    自适应阈值二值化
    """
    image = cv2.adaptiveThreshold(src, max, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
    return image
