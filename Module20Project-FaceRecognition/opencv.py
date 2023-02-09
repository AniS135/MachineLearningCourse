# Simple Program to read and show an Image

import cv2

img = cv2.imread('Module20Project-FaceRecognition\Data\dog.png')
gray = cv2.imread('Module20Project-FaceRecognition\Data\dog.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image', img)
cv2.imshow('Gray Dog Image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
