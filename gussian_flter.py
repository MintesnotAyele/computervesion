import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("cameraman.png", 0)
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(3, 3), sigmaX=0, sigmaY=0)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.show()
plt.imshow(gaussian_blur, cmap='gray')
plt.title('GaussianBlur filter')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()