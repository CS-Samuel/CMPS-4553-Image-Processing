# Samuel Weems
# Program 4
# CMPS 4553/5353 Summer 2018
# July 05, 2018

import cv2 as cv
import numpy as np 
import scipy.ndimage

#############################################################################
########################### Reduce Colors Function ##########################
#############################################################################

# Accept an RGB image matrix set and a threshold value (0-255)
# Returns a new RGB image matrix set
# In each of the three RGB matrices if the pixel is greater than the threshold
# the corresponding pixel value in the new image will be 255, otherwise 0

def reduceColors(image, threshold_value):
    
    redBand = image[:,:,2]
    greenBand = image[:,:,1]
    blueBand = image[:,:,0]

    rows, columns, channels = image.shape
    threshold_value = int(threshold_value)  # Cast threshold as int

    for i in range(rows):
        for j in range(columns):

            if (redBand[i,j] > threshold_value):
                redBand[i,j] = 255
            else:
                redBand[i,j] = 0

            if (greenBand[i,j] > threshold_value):
                greenBand[i,j] = 255
            else:
                greenBand[i,j] = 0

            if (blueBand[i,j] > threshold_value):
                blueBand[i,j] = 255
            else:
                blueBand[i,j] = 0

    new_image = cv.merge((blueBand,greenBand,redBand))
    cv.imshow('Thresholded Image',new_image)    # Display image
    cv.waitKey(0)   # Wait on key click 
    cv.destroyAllWindows()  # Remove image from display

##############################################################################
############################ Main Program ####################################
##############################################################################

# Receives input of file and threshold value and calls function

imageFile= raw_input("Enter name of the original image: ")
image = cv.imread(imageFile)

threshold_value = raw_input("Enter the threshold value (0-255): ")

newImage = reduceColors(image, threshold_value)

