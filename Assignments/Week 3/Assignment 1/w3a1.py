import cv2
import numpy

camera = cv2.VideoCapture(0)
return_value, image = camera.read()

# image = cv2.imread("Assignments/Week 3/Assignment 1/assets/input/input_image_3.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
output_image = numpy.array(image)

blurIntensity = 11 #initial blur intensity
numOfCircles = 50

coins = numpy.zeros((2, 3))

while(numOfCircles > 2 and blurIntensity < 300):
    output_image = numpy.array(image)
    print("blurIntensity - "+str(blurIntensity))
    gray_image = cv2.medianBlur(gray_image, blurIntensity)

    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=50, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = numpy.array(circles)
        circles = circles.astype(numpy.uint16)
        numOfCircles = (int(numpy.product(circles.shape)/3))
        circles = circles.reshape(numOfCircles, 3)
        if(numOfCircles == 2):
            coins = numpy.array(circles)
        for circle_to_draw in circles:
            print(circle_to_draw)
            x = circle_to_draw[0]
            y = circle_to_draw[1]
            r = circle_to_draw[2]
            cv2.circle(output_image, (x, y), r, (0, 0, 255), 3)
    
    blurIntensity += 2

if(numpy.sum(coins) == 0):
    print("Program exited, coins not detected, check output image.")
    cv2.imwrite('Assignments/Week 3/Assignment 1/assets/output/output_image.jpg', output_image)
else:
    start_x = int(coins[0][0])
    start_y = int(coins[0][1])
    end_x = int(coins[1][0])
    end_y = int(coins[1][1])
    radius = int(coins[0][2])  # Assuming radius of both coins is the same
    distance = round((((start_x - end_x) ** 2 + (start_y - end_y) ** 2) ** 0.5)/radius, 2)
    cv2.line(output_image, (start_x, start_y), (end_x, end_y), (255, 0, 0), 5)
    cv2.circle(output_image, (start_x, start_y), 5, (0, 0, 255), 10)
    cv2.circle(output_image, (end_x, end_y), 5, (0, 0, 255), 10)
    cv2.putText(output_image, "distance - " + str(distance) + " units", (int((start_x + end_x)/2 + 10), int((start_y + end_y)/2) + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    cv2.imwrite('Assignments/Week 3/Assignment 1/assets/output/output_image.jpg', output_image)

    print("program exited, check output image")

