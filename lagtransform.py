import cv2
import numpy as np
file_name = "cameraman.png"
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
log_transformed_img = np.log1p(img)
log_transformed_img = (log_transformed_img / np.max(log_transformed_img)) * 255
log_transformed_img = np.uint8(log_transformed_img)
cv2.imshow("Original Image", img)
cv2.imshow("Log-Transformed Image", log_transformed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

