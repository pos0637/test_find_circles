import os
import cv2
import glob
from roi import *
from morphology import *
from edge import *


CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]


def test(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # gray = cv2.GaussianBlur(gray, (3, 3), 2, 2)

    ret, gray = cv2.threshold(gray, 230, 255, cv2.THRESH_TOZERO)
    cv2.imshow('threshold', gray)

    gray = open(gray, (9, 9))
    cv2.imshow('open', gray)

    maxContour = -1
    maxContourSize = -1
    _, contours, hierarchy = cv2.findContours(
        gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        if hierarchy[0][i][3] != -1:
            size = cv2.contourArea(contours[i])
            print 'size: %d' % size

            if size > maxContourSize:
                maxContour = i
                maxContourSize = size

    temp = image.copy()
    cv2.drawContours(temp, contours, maxContour, (0, 0, 255), 1)
    center = getCenter(contours[maxContour])
    cv2.line(temp, (center[0] - 5, center[1]),
             (center[0] + 5, center[1]), (0, 0, 255), 1)
    cv2.line(temp, (center[0], center[1] - 5),
             (center[0], center[1] + 5), (0, 0, 255), 1)
    cv2.imshow('maxContour', temp)
    cv2.waitKey(0)


files = glob.glob(CURRENT_PATH + '/data1/*.*')
for f in files:
    image = cv2.imread(f)
    image = getROI(image, 400, 200, 1000, 800)
    test(image)

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()
