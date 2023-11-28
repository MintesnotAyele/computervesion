import cv2
import numpy as np


file_name = "cameraman.png"   
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)       
min_intensity = np.min(img)
max_intensity = np.max(img)
stretched_img = np.clip((img - min_intensity) * (255.0 / (max_intensity - min_intensity)), 0, 255)       
stretched_img = np.uint8(stretched_img)      
cv2.imshow("Original Image", img)
cv2.imshow("Contrast Stretched Image", stretched_img)        
cv2.waitKey(0)     
cv2.destroyAllWindows()

