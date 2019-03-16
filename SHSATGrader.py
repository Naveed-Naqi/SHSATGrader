#This program succesffuly reads in an image and finds all contours after converting to a binary image
#The contours are then all drawn on the original image
#Dev Notes: Make sure the circle is completely filled in and there are no stray marks on the page
#Dev Notes: Make sure that the the pencil marks are inside the bubbles as much as possible
#Dev Notes: Make sure that only ONE answer is selected

from imutils import contours
import numpy as np
import imutils
import cv2
import csv

def readImage(image):

    #cv2.imshow("original image", image)
    #cv2.waitKey(0)                                          #Waits for button press before moving on

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #Converts the image to greyscale

    #Converts to a binary image by changing the background of the image to black and the foreground to white
    binary_image = cv2.threshold(gray_image, 0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #cv2.imshow("Binary Image", binary_image)
    #cv2.waitKey(0)


    #Finds all contours in the binary image
    all_contours = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    all_contours = imutils.grab_contours(all_contours)
    #The list that will hold all our multiple choice questions
    mc_questions = []

    for c in all_contours:
        #Creates the minimum spanning rectangle around each contour
        #Let (x,y) be the top-left coordinate of the rectangle
        (x, y, width, height) = cv2.boundingRect(c)
        aspect_ratio = width/float(height)

        #If the width and height of the rectangle is more than 30 pixels and the aspect ratio is around 1
        #Add the contour to the the list of questions we want to detect
        if width >= 35 and width <= 50 and height >= 35 and height <= 50 and aspect_ratio >= .8 and aspect_ratio <= 1.2:
            mc_questions.append(c)

    #Draws the image with all the questions highlighted in green
    #cv2.drawContours(image, mc_questions, -1, (0,255,0), 3)
    #cv2.imshow("contours", image)
    #cv2.waitKey(0)

    mc_questions = contours.sort_contours(mc_questions,method="top-to-bottom")[0]
    cnts = []
    cols = 4

    # each question has 4 possible answers, to loop over the question in batches of 4
    for (q,i) in enumerate(np.arange(0, len(mc_questions), cols)):
        # sort the contours for the current question from left to right
        cnts += contours.sort_contours(mc_questions[i:i+cols],method="left-to-right")[0]

    mc_question_array = []

    # loop over the sorted contours
    for (j, c) in enumerate(cnts):

        # construct a mask that reveals only the current "bubble" for the question
        mask = np.zeros(binary_image.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        # apply the mask to the thresholded image, then
        # count the number of non-zero pixels in the bubble area
        mask = cv2.bitwise_and(binary_image, binary_image, mask=mask)
        #cv2.imshow("mask",mask)
        #cv2.waitKey(0)
        total = cv2.countNonZero(mask)

        mc_question_array.append(total)

    cv2.destroyAllWindows()

    for x in range(len(mc_question_array)):
        if mc_question_array[x] > 1000:
            mc_question_array[x] = 1
        else:
            mc_question_array[x] = 0

    a = np.array(mc_question_array).reshape(len(mc_question_array)//cols,cols)

    return a

def formatCSV(input_file):
    all_data = csv.reader(open(input_file)) # Here your csv file
    lines = list(all_data)

    for i in range(len(lines)):
        for j in range(4):
            if (i % 2 == 0):
                if (j == 0 and lines[i][j] == "1"):
                    lines[i][0] = "A"
                elif (j == 1 and lines[i][j] == "1"):
                    lines[i][0] = "B"
                elif (j == 2 and lines[i][j] == "1"):
                    lines[i][0] = "C"
                elif (j == 3 and lines[i][j] == "1"):
                    lines[i][0] = "D"
            if (i % 2 == 1):
                if (j == 0 and lines[i][j] == "1"):
                    lines[i][0] = "E"
                elif (j == 1 and lines[i][j] == "1"):
                    lines[i][0] = "F"
                elif (j == 2 and lines[i][j] == "1"):
                    lines[i][0] = "G"
                elif (j == 3 and lines[i][j] == "1"):
                    lines[i][0] = "H"

    for i in range(len(lines)):
        for j in range(3):
            lines[i][j+1] = ""

    writer = csv.writer(open(input_file, 'w'))
    writer.writerows(lines)

if __name__ == '__main__':

    image = cv2.imread('test_image.png')
    first_col = image[20:800, 50:550]
    second_col = image[20:800, 650:1150]
    third_col = image[20:800, 1250:1750]
    fourth_col = image[20:800, 1850:2350]


    ############TEST###########
    a = readImage(first_col)#.tolist()
    b = readImage(second_col)#.tolist()
    c = readImage(third_col)#.tolist()
    d = readImage(fourth_col)#.tolist()

    with open("new_file.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(a)
        csvWriter.writerows(b)
        csvWriter.writerows(c)
        csvWriter.writerows(d)
    
    formatCSV("new_file.csv")



