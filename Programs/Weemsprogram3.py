# Samuel Weems
# Program 3
# CMPS 4553/5353 Summer 2018
# June 21, 2018

from PIL import Image
import numpy as np 
import scipy.ndimage

#############################################################################
########################### Image Filter Function ###########################
#############################################################################

# Apply a filter based on random numbers in a 3x3 mask

def randomFilter(image, minimum, maximum):
  
  rows  = 3
  cols = 3
  filter = np.matrix(np.random.randint(minimum,maximum, size=(rows, cols)))
  
  result = scipy.ndimage.convolve(image, filter)
  resultImage = Image.fromarray(result)

  return resultImage

##############################################################################
############################ Main Program ####################################
##############################################################################

imageFile= raw_input("Enter name of the original image: ")
image = Image.open(imageFile)

minimum = raw_input("Enter the minimum mask value: ")
maximum = raw_input("Enter the maximum mask value: ")

filteredImage = randomFilter(image, minimum, maximum)
filteredImage.show()
