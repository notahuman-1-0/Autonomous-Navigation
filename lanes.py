import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting the image to grayscale.
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,100)
    return canny

#reading the image and the window for the image
image = cv2.imread('test_image.jpeg')
lane_image=np.copy(image)#copying the image to the variable lane_image
canny=canny(lane_image)
#cv2.imshow('result',canny)
#cv2.waitKey(0)
plt.imshow(canny)
plt.show()
