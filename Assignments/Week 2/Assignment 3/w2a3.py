import cv2
import numpy

radius_of_colours_to_ignore = 30
max_occurence_count = numpy.zeros(5, numpy.int64)

def maxOccuringPixel(pixel_count):
    return_pixel = numpy.empty(3, numpy.int64)
    max = 0
    i = 0
    while i < len(pixel_count):
        j = 0
        while j < len(pixel_count[0]):
            k = 0
            while k < len(pixel_count[0][0]):
                if(pixel_count[i][j][k] > max):
                    max = pixel_count[i][j][k]
                    return_pixel[0] = i
                    return_pixel[1] = j
                    return_pixel[2] = k
                k += 1
            j += 1
        i += 1
    i = 0
    while i < 5:
        if(max_occurence_count[i] == 0):
            max_occurence_count[i] = max
            break
        i += 1
    return return_pixel


pixel_count = numpy.zeros((256, 256, 256), numpy.int64)

image = cv2.imread('Assignments/Week 2/Assignment 3/assets/input/input_image.jpeg')
image_nparr = numpy.array(image)
image_nparr = image_nparr.astype(numpy.uint16)
image_nparr = image_nparr.reshape((int(numpy.product(image_nparr.shape)/3), 3))

for pixel in image_nparr:
    pixel_count[pixel[0]][pixel[1]][pixel[2]] += 1

output_image = numpy.empty(image_nparr.shape)

max_occuring_pixels = numpy.empty((5, 3), numpy.int64)

i = 0
while i < 5:
    pixel = maxOccuringPixel(pixel_count)
    j = -radius_of_colours_to_ignore
    while j <= radius_of_colours_to_ignore:
        k = -radius_of_colours_to_ignore
        while k <= radius_of_colours_to_ignore:
            l = -radius_of_colours_to_ignore
            while l <= radius_of_colours_to_ignore:
                if(pixel[0] + j < 256 and pixel[0] + j > 0 and pixel[1] + k < 256 and pixel[1] + k > 0 and pixel[2] + l < 256 and pixel[2] + l > 0):
                    pixel_count[pixel[0] + j][pixel[1] + k][pixel[2] + l] = 0
                l += 1
            k += 1
        j += 1
    max_occuring_pixels[i] = pixel
    i += 1

print(max_occuring_pixels)

output_image = numpy.empty(image_nparr.shape)

j = 0
while j < len(image_nparr):
    pixel = image_nparr[j]
    min_diff_value = 270
    min_index = 0
    i = 0
    while i < 5:
        prom_pixel = max_occuring_pixels[i]
        diff_value = abs(prom_pixel[0] - pixel[0]) + abs(prom_pixel[1] - pixel[1]) + abs(prom_pixel[2] - pixel[2])
        if(diff_value < min_diff_value):
            min_diff_value = diff_value
            min_index = i
        i += 1
    output_image[j] = max_occuring_pixels[min_index]
    j += 1

output_image = output_image.reshape(image.shape)

sum_of_occurence = 0
for occurence in max_occurence_count:
    sum_of_occurence += occurence

prominent_colours_image = numpy.zeros((5 * 100, 5 * (2 * radius_of_colours_to_ignore + 1), 3))
i = 0
height_boundary = int(max_occurence_count[0] * 5 * 100/sum_of_occurence)
counter = 0
print(height_boundary)
while i < (5 * 100):
    if(i == height_boundary and counter < 4):
        counter += 1
        height_boundary += int(max_occurence_count[counter] * 5 * 100/sum_of_occurence)
    j = 0
    while j < 5 * (2 * radius_of_colours_to_ignore + 1):
        prominent_colours_image[i][j] = max_occuring_pixels[counter]
        j += 1
    i += 1

cv2.imwrite('Assignments/Week 2/Assignment 3/assets/output/prominent_colours_image.jpg', prominent_colours_image)
cv2.imwrite('Assignments/Week 2/Assignment 3/assets/output/output_image.jpg', output_image)