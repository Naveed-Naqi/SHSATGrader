import cv2

if __name__ == '__main__':
    #HARDCODED, DEPENDS ON RESOLUTION AND FORMATING OF SHEET
    image = cv2.imread('real_test_image.png',cv2.IMREAD_GRAYSCALE)

    height, width = image.shape[:2]

    print(height)
    print(width)
    print("-----")

    image2 = cv2.imread('test_image.jpg',cv2.IMREAD_GRAYSCALE)

    height, width = image2.shape[:2]

    print(height)
    print(width)