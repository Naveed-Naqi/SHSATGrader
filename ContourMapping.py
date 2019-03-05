#This program succesffuly reads in an image and finds all contours after converting to a binary image
#The contours are then all drawn on the original image
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


#Finds all contours in the binary image
all_contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
all_contours = imutils.grab_contours(all_contours)

#The list that will hold all our multiple choice questions
mc_questions = []

for c in all_contours:
    #Creates the minimum spanning rectangle around each contour
    #Let (x,y) be the top-left coordinate of the rectangle
    (x, y, width, height) = cv2.boundingRect(c)
    aspect_ratio = width/height

    #If the width and height of the rectangle is more than 30 pixels and the aspect ratio is around 1
    #Add the contour to the the list of questions we want to detect
    if width >= 35 and width <= 45 and height >= 35 and height <= 45 and aspect_ratio >= .8 and aspect_ratio <= 1.2:
        mc_questions.append(c)

#Draws the image with all the questions highlighted in green
cv2.drawContours(image, mc_questions, -1, (0,255,0), 3)
cv2.imshow("contours", image)

cv2.destroyAllWindows()