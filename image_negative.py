import cv2

# Specify the file name
file_name = "cameraman.png"
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
negative_img = 255 - img
cv2.imshow("Original Image", img)
cv2.imshow("Negative Image", negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
