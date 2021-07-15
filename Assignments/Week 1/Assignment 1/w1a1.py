import numpy
from PIL import Image
from numpy import asarray

img = Image.open('Assignments/Week 1/Assignment 1/assets/input/input.jpg')
img_array = asarray(img)
print(type(img_array))
print(img_array)

i = 0
inverted_img_array = numpy.empty((1000, 1000, 3), numpy.uint8)
grayscale_img_array = numpy.empty((1000, 1000, 3), numpy.uint8)
while(i < len(img_array)):
    j = 0
    while(j < len(img_array[0])):
        gray_scale_value = ((img_array[i][j][0] + img_array[i][j][1] + img_array[i][j][2])/(3))
        grayscale_img_array[i][j] = [gray_scale_value, gray_scale_value, gray_scale_value]
        inverted_img_array[i][j] = [255 - img_array[i][j][0], 256 - img_array[i][j][1], 256 - img_array[i][j][2]]
        j += 1
    i += 1

inverted_img = Image.fromarray(inverted_img_array)
inverted_img.save('Assignments/Week 1/Assignment 1/assets/output/inverted_output.png')

grayscale_img = Image.fromarray(grayscale_img_array)
grayscale_img.save('Assignments/Week 1/Assignment 1/assets/output/grayscale_output.png')