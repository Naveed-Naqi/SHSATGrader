import cv2

image = cv2.imread('real_test_image.png')

#First indices control the length of the cropped section
#Second indices control the width of the cropped section

ela_first_col = image[180:460, 970:1130]
ela_second_col = image[1400:2800, 1500:2500]
ela_third_col = image[1400:2800, 2500:3500]
ela_fourth_col = image[1400:2800, 3500:4500]

#Need to determine these numbers and determine a negative sign
first_grid_in = image[3220:4150, 850:1200]
second_grid_in = image[3220:4150, 1450:2000]
third_grid_in = image[3220:4150, 2100:2900]
fourth_grid_in = image[3220:4150, 2900:3700]
fifth_grid_in = image[3220:4150, 3700:4500]

math_first_col = image[4200:5500, 500:1500]
math_second_col = image[4300:5500, 1500:2500]
math_third_col = image[4300:5500, 2500:3500]
math_fourth_col = image[4300:5500, 3500:4500]

cv2.imshow("ela_first col", ela_first_col)
cv2.waitKey(0)
"""
cv2.imshow("ela_second col", ela_second_col)
cv2.waitKey(0)

cv2.imshow("ela_third col", ela_third_col)
cv2.waitKey(0)

cv2.imshow("ela_fourth col", ela_fourth_col)
cv2.waitKey(0)

cv2.imshow("math first col", math_first_col)
cv2.waitKey(0)

cv2.imshow("math second col", math_second_col)
cv2.waitKey(0)

cv2.imshow("math third col", math_third_col)
cv2.waitKey(0)

cv2.imshow("math fourth col", math_fourth_col)
cv2.waitKey(0)

cv2.imshow("first grid in", first_grid_in)
cv2.waitKey(0)

cv2.imshow("second grid in", second_grid_in)
cv2.waitKey(0)

cv2.imshow("third grid in", third_grid_in)
cv2.waitKey(0)

cv2.imshow("fourth grid in", fourth_grid_in)
cv2.waitKey(0)

cv2.imshow("fifth grid in", fifth_grid_in)
cv2.waitKey(0)
"""