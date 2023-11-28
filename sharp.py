import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("cameraman.png",0)
mean=0
stdev=180
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)
img1_kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img2=cv2.filter2D(src=gaussian_blur,ddepth=-1,kernel=img1_kernel)
cv2.imshow('input',img)
cv2.imshow("smooth1",gaussian_blur)
cv2.imshow('sharp',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
