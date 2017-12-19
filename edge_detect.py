import os
import cv2

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
PIC_PATH = CURRENT_PATH + '/door3.jpg'

image = cv2.imread(PIC_PATH)
height, width = image.shape[:2]
dst = cv2.imread(PIC_PATH)

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# cv2.imshow("gray", image)

# image = cv2.GaussianBlur(image, (3, 3), 0)
image = cv2.medianBlur(image, 5)

# ret, image = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
# image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
# ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 2))

# dilation = cv2.dilate(image, element2, iterations=1)
# erosion = cv2.erode(image, element1, iterations=1)
# dilation = cv2.dilate(image, element2, iterations=1)
# image = dilation

cv2.imshow('threshold', image)

# image = cv2.Canny(image, 30, 50)
# cv2.imshow('canny', image)

circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1,
                           width / 16, None, param1=100, param2=30, minRadius=10, maxRadius=30)
for i in circles[0, :]:
    cv2.circle(dst, (i[0], i[1]), i[2], (255, 0, 0), 2)
    print 'radius: ' + str(i[2])

cv2.imshow('circles', dst)

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()
