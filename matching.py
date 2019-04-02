#-*- coding:utf-8 -*-

import cv2
import numpy as np


def matchTemplate(template, target, threshold=0.8):
    """
    模版匹配
    """
    h, w = template.shape
    matches = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    if threshold < 0:
        min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(matches)
        return [[max_loc[0], max_loc[1], max_loc[0] + w, max_loc[1] + h]]
    else:
        matches = sorted(matches, key=lambda x: x)
        loc = np.where(matches >= threshold)
        result = []
        for pt in zip(*loc[::-1]):
            result.append([pt[0], pt[1], pt[0] + w, pt[1] + h])

        return result
