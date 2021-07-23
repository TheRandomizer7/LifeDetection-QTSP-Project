import cv2

camera = cv2.VideoCapture(0)

for i in range(1): 
    print('bla')
    return_value, image = camera.read()
    cv2.imwrite('Assignments/Week 2/Assignment 1/output/captured_image.jpg', image)

    inverted_image = (255 - image)
    cv2.imwrite('Assignments/Week 2/Assignment 1/output/inverted_captured_image.jpg', inverted_image)

    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite('Assignments/Week 2/Assignment 1/output/BGR_captured_image.jpg', bgr_image)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    cv2.imwrite('Assignments/Week 2/Assignment 1/output/HSV_captured_image.jpg', hsv_image)

    hls_image = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    cv2.imwrite('Assignments/Week 2/Assignment 1/output/HLS_captured_image.jpg', hls_image)

del(camera)

