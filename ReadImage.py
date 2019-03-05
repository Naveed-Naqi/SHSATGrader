#This program succesffuly converts a given image to a binary image and displays both on the screen
#Dev Notes: Make sure the circle is completely filled in and there are no stray marks on the page
#Dev Notes: Make sure that the the pencil marks are inside the bubbles as much as possible
#Dev Notes: Make sure that only ONE answer is selected

import cv2
import imutils
from imutils import contours
import numpy as np


image = cv2.imread('test_image.png')                 #Reads the image

cv2.imshow("original image", image)
cv2.waitKey(0)                                          #Waits for button press before moving on

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #Converts the image to greyscale

#Converts to a binary image by changing the background of the image to black and the foreground to white
binary_image = cv2.threshold(gray_image, 0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
