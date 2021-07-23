import cv2
import numpy

image = cv2.imread('Assignments/Week 2/Assignment 2/assets/input/input_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = numpy.array(circles)
    circles = circles.astype(numpy.uint16)
    circles = circles.reshape((int(numpy.product(circles.shape)/3), 3))
    for circle_to_draw in circles:
        x = circle_to_draw[0]
        y = circle_to_draw[1]
        r = circle_to_draw[2]
        cv2.circle(image, (x, y), r, (0, 0, 0), 2)

cv2.imwrite('Assignments/Week 2/Assignment 2/assets/output/output_image.jpg', image)

