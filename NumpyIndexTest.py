import cv2

image = cv2.imread('test_image.png')

first_col = image[300:700, 50:350]
second_col = image[300:700, 350:600]
third_col = image[300:700, 600:900]
fourth_col = image[300:700, 850:1150]

cv2.imshow("original image", image)
cv2.waitKey(0)

cv2.imshow("first col", first_col)
cv2.waitKey(0)

cv2.imshow("second col", second_col)
cv2.waitKey(0)

cv2.imshow("third col", third_col)
cv2.waitKey(0)

cv2.imshow("fourth col", fourth_col)
cv2.waitKey(0)
