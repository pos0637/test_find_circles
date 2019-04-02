import os
import cv2

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PIC_PATH = CURRENT_PATH + '/door1.jpg'

image = cv2.imread(PIC_PATH)
height, width = image.shape[:2]

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 15, 15)

ret, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('threshold', image)

image = cv2.Canny(image, 30, 50)
cv2.imshow('circles', image)

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()
