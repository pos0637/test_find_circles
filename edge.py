# -*- coding: utf-8 -*-

import cv2
import numpy as np


def enhanced(src):
    """
    边缘增强
    """
    image = cv2.Laplacian(src, cv2.CV_8U, ksize=3)
    image = cv2.add(src, image)
    return image


def getContours(src):
    """
    提取轮廓
    """
    contours, hierarchy = cv2.findContours(
        src.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def drawBoundingRect(src, contours, color=(255, 255, 255)):
    """
    绘制外接矩形
    """
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(src, (x, y), (x + w, y + h), color, 1)

    return src


def drawRotatedRect(src, rect, color=(255, 255, 255)):
    """
    绘制旋转外接矩形
    """
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(src, [box], 0, color, 1)


def autoCanny(src, sigma=0.33):
    """
    自动查找边缘
    """
    # compute the median of the single channel pixel intensities
    v = np.median(src)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(src, lower, upper)

    return edged


def getCenter(contour):
    """
    获取轮廓几何中心
    """
    M = cv2.moments(contour)
    if M['m00'] == 0:
        return [-1, -1]
    else:
        return [int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])]
