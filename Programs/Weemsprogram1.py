# Samuel Weems
# Program 1
# CMPS 4553/5353 Summer 2018
# June 14, 2018

import os
from PIL import Image
#############################################################################
################################# Image Save Function #######################
#############################################################################
# creates 4 new files so that all of the following types are present:
# JPG, TIF, GIF, BMP, PNG
# Note: Ran into an error in saving BMP files as TIFF so exception code saves
# BMP as JPEG and then uses new JPEG file to save as TIFF

def imageSave(original, new):
    os.makedirs(new)
    image = Image.open(original)

    exceptionFlag = False           #Code to handle exception of BMP --> TIFF
    if image.format == 'BMP':
        exceptionFlag = True

    image = image.convert('RGB')    #Convert to RGB before saving in formats
    
    image.save('./' + new + '/' + new + '.jpg', 'jpeg')
    image.save('./' + new + '/' + new + '.gif', 'gif')
    image.save('./' + new + '/' + new + '.bmp', 'bmp')
    image.save('./' + new + '/' + new + '.png', 'png')
    
    if exceptionFlag:        #Code to handle excpetion of BMP --> TIFF
        imageException = Image.open('./' + new + '/' + new +'.jpg')
        imageException.save('./' + new + '/' + new + '.tif', 'tiff')
    else:
        image.save('./' + new + '/' + new + '.tif', 'tiff')

###############################################################################
############################ Main Program #####################################
###############################################################################
# User input file to be converted (check it exists) and name for new files

originalFileName = raw_input("Enter the original file name you would like to convert: ")

if os.path.isfile('./' + originalFileName):
    newFileName = raw_input ("Enter a new name for directory and files to be created (make sure directory doesn't already exist!): ")
    image=Image.open(originalFileName)
    imageSave(originalFileName, newFileName)
else:
    print("File does not exist. Make sure file is current working directory: " + os.getcwd())





