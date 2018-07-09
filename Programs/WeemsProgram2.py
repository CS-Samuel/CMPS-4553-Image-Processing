# Samuel Weems
# Program 2
# CMPS 4553/5353 Summer 2018
# June 18, 2018

import numpy as np
from PIL import Image


#############################################################################
################################# Image Merge Function ######################
#############################################################################

def imageMerge(image1, image2):
    width = 1000
    height = 1000

    newImage = Image.open(image1).resize((width,height), Image.NEAREST)
    imageB = Image.open(image2).resize((width,height), Image.NEAREST)
    
    newImage.paste(imageB, (0,0), imageB)
    newImage.show()


#############################################################################
############################ Main Program ###################################
#############################################################################

firstFile = raw_input("Enter name of the original image: ")
secondFile = raw_input("Enter the name of the pattern image: ")

imageMerge(firstFile, secondFile)







