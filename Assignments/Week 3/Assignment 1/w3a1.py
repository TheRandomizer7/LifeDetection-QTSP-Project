import cv2
import numpy

image = cv2.imread('Assignments/Week 3/Assignment 1/assets/input/input_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray_image = cv2.medianBlur(gray_image, 11)

circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=75, minRadius=0, maxRadius=0)

if circles is not None:
    circles = numpy.array(circles)
    circles = circles.astype(numpy.uint16)
    circles = circles.reshape((int(numpy.product(circles.shape)/3), 3))
    for circle_to_draw in circles:
        print(circle_to_draw)
        x = circle_to_draw[0]
        y = circle_to_draw[1]
        r = circle_to_draw[2]
        cv2.circle(image, (x, y), r, (0, 0, 255), 2)

cv2.imwrite('Assignments/Week 3/Assignment 1/assets/output/output_image.jpg', image)

