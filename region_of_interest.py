import cv2
import numpy as np
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting the image to grayscale.
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,100)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200,height),(1100,height),(550,250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    masked_image = cv2.bitwise_and(image,mask) #
    return masked_image

#reading the image and the window for the image
image = cv2.imread('test_image.jpeg')
lane_image=np.copy(image)#copying the image to the variable lane_image
canny=canny(lane_image)
cropped_image = region_of_interest(canny)
cv2.imshow('result',region_of_interest(canny))
cv2.waitKey(0)
