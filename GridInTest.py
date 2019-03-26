from imutils import contours
import numpy as np
import imutils
import cv2
import csv

def readGridInImage(image):

    cv2.imshow("original image", image)
    cv2.waitKey(0)                                          #Waits for button press before moving on

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #Converts the image to greyscale

    #Converts to a binary image by changing the background of the image to black and the foreground to white
    binary_image = cv2.threshold(gray_image, 0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(0)


    #Finds all contours in the binary image
    all_contours = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    all_contours = imutils.grab_contours(all_contours)
    #The list that will hold all our multiple choice questions
    mc_questions = []

    #Draws the image with all the questions highlighted in green
    cv2.drawContours(image, all_contours, -1, (0,255,0), 3)
    cv2.imshow("contours", image)
    cv2.waitKey(0)

if __name__ == '__main__':
    
    image = cv2.imread('real_test_image.jpg')

    #HARDCODED, DEPENDS ON RESOLUTION AND FORMATING OF SHEET
    first_grid_in = image[3200:4200, 500:2000]
    second_grid_in = image[3200:4200, 1300:2100]
    third_grid_in = image[3200:4200, 2100:2900]
    fourth_grid_in = image[3200:4200, 2900:3700]
    fifth_grid_in = image[3200:4200, 3700:4500]

    ############TEST###########

    readGridInImage(first_grid_in)
    readGridInImage(second_grid_in)
    readGridInImage(third_grid_in)
    readGridInImage(fourth_grid_in)
    readGridInImage(fifth_grid_in)