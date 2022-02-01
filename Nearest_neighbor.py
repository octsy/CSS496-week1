from multiprocessing.sharedctypes import Value
import cv2
import numpy as np
 
def Near_img(img):
    
    width = int(1024)
    height = int(1024)
    dim = (width, height)
    near_img = cv2.resize(img, dim ,fx = 0 , fy = 0,  interpolation = cv2.INTER_NEAREST)
    return near_img

img = cv2.imread('./newmypic.jpg')
Near_img = Near_img(img)

#cv2.imwrite('./newmypic.jpg', Near_img)

cv2.imshow('near image', Near_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

