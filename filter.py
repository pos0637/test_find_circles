# -*- coding: UTF-8 -*-

import cv2
import numpy as np


def medianBlur(src, size=3):
    """
    中值滤波
    """
    return cv2.medianBlur(src, size)


def contrast(src, ratio=1.0):
    """
    对比度调节
    """
    if len(src.shape) == 3:
        rows, cols, channels = src.shape
        image = src.copy()

        for i in range(rows):
            for j in range(cols):
                for c in range(channels):
                    color = src[i, j][c] * ratio
                    if color > 255:
                        image[i, j][c] = 255
                    elif color < 0:
                        image[i, j][c] = 0
    else:
        rows, cols = src.shape
        image = src.copy()

        for i in range(rows):
            for j in range(cols):
                color = src[i, j] * ratio
                if color > 255:
                    image[i, j] = 255
                elif color < 0:
                    image[i, j] = 0

    return image


def equalized(src):
    """
    直方图均衡化
    """
    hist, _ = np.histogram(src.flatten(), 256, [0, 256])
    cdf = hist.cumsum()  # 计算累积直方图
    cdf_m = np.ma.masked_equal(cdf, 0)  # 除去直方图中的0值
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())  # 等同于前面介绍的lut[i] = int(255.0 *p[i])公式
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # 将掩模处理掉的元素补为0

    return cv2.LUT(src, cdf)
