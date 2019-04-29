import numpy as np
import cv2 as cv
from imutils import contours
import imutils
import csv

#id_matrix is a 10 by 5 matrix, but this method would work for any matrix
def formatID(id_matrix):

    id_number = 0

    #The number of columns in the matrix
    minimum_width = len(id_matrix[0])
    filler = "0"
    
    place_value = minimum_width - 1
    
    for i in range(len(id_matrix)):
        for j in range(len(id_matrix[i])):
            if(id_matrix[i][j] == 1):
                id_number += (i * (10**(place_value - j)))
    
    id_number = f'{id_number:{filler}{minimum_width}}'
    
    return id_number

im = cv.imread('real_test_image.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
thresh = cv.threshold(imgray, 0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
#cv.imshow("gray", thresh)
#cv.waitKey(0)
#cv.destroyAllWindows()
all_contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#print(hierarchy[0])
external_contours = []
test  = []
mc_questions = []

for i in range(len(all_contours)):
    if(hierarchy[0][i][3] != 418 and hierarchy[0][i][3] != -1):
        external_contours.append(hierarchy[0][i][3])



for i in range(len(all_contours)):
    if(hierarchy[0][i][3] == 166):
        (x, y, width, height) = cv.boundingRect(all_contours[i])
        aspect_ratio = width/float(height)
        if width >= 15 and width <= 50 and height >= 15 and height <= 50 and aspect_ratio >= .5 and aspect_ratio <= 1.3:
            mc_questions.append(all_contours[i])

x= max(external_contours, key=external_contours.count)
print(x)



cv.drawContours(im, mc_questions, -1, (0,255,0), 3)
cv.imshow("contours", im)
cv.waitKey(0)
cv.destroyAllWindows()

mc_questions = contours.sort_contours(mc_questions,method="top-to-bottom")[0]
cnts = []
  
#Number of answer choices per question
cols = 5

# each question has 4 possible answers, to loop over the question in batches of 4
for (q,i) in enumerate(np.arange(0, len(mc_questions), cols)):
    # sort the contours for the current question from left to right
    cnts += contours.sort_contours(mc_questions[i:i+cols],method="left-to-right")[0]

mc_question_array = []

# loop over the sorted contours
for (j, c) in enumerate(cnts):

    # construct a mask that reveals only the current "bubble" for the question
    mask = np.zeros(thresh.shape, dtype="uint8")
        
    cv.drawContours(mask, [c], -1, 255, -1)
    # apply the mask to the thresholded image, then
    # count the number of non-zero pixels in the bubble area
    mask = cv.bitwise_and(thresh, thresh, mask=mask)
    #cv2.imshow("mask",mask)
    #cv2.waitKey(0)
    total = cv.countNonZero(mask)
        
    mc_question_array.append(total)

a = np.array(mc_question_array).reshape(len(mc_question_array)//cols,cols)

min_val = 0

for i in range(len(a)):

    min_val = min(a[i])

    for j in range(len(a[i])):

        if(a[i][j] < (min_val * 1.9)):
            a[i][j] = 0
        else:
            a[i][j] = 1

print(formatID(a))




