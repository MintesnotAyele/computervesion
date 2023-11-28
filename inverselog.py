import cv2
import numpy as np
img = cv2.imread("cameraman.png", 0)
inverse_log_img = np.exp(np.clip(255 - img, 0, 255))
inverse_log_img = np.uint8(inverse_log_img)
cv2.imshow("Original", img)
cv2.imshow("Inverse Log Transformed", inverse_log_img)
cv2.waitKey(0)
cv2.destroyAllWindows()