import os
import cv2

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PIC_PATH = CURRENT_PATH + '/door3.jpg'

image = cv2.imread(PIC_PATH)
height, width = image.shape[:2]
dst = cv2.imread(PIC_PATH)

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# image = cv2.medianBlur(image, 5)
image = cv2.GaussianBlur(image, (5, 5), 15, 15)

cv2.imshow('threshold', image)

circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, width / 16, None, param1=100, param2=30, minRadius=10, maxRadius=30)
for i in circles[0, :]:
    cv2.circle(dst, (i[0], i[1]), i[2], (255, 0, 0), 2)    

cv2.imshow('circles', dst)

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()
