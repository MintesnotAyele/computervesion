#Mintesnot Ayele NRS/1535/13
#yenesew sileshi NSR/2198/13
#samuel fikre NSR/1813/13
#Abilwahid Akrem NSR/2561/13
#Aster Belete NSR/0285/13
#Dominic loang Peter NSR/2542/13
import cv2
file_name = "cameraman.png"
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
equalized_img = cv2.equalizeHist(img)
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()