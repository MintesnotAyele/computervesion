import cv2
import numpy as np
img=cv2.imread('cameraman.png')
img_kernel=np.array([[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04],[0.04,0.04,0.04,0.04,0.04]])
img1_kernel=np.array([[0.11,0.11,0.11,0.11],[0.11,0.11,0.11,0.11],[0.11,0.11,0.11,0.11]])
out_img=cv2.filter2D(src=img,ddepth=-1,kernel=img_kernel)
imag2=cv2.filter2D(src=img,ddepth=-1,kernel=img1_kernel)
cv2.imshow('original',img)
cv2.imshow("smoth",out_img)
cv2.imshow('fair',imag2)
cv2.waitKey(0)