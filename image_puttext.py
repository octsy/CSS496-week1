import cv2
    

    
# Reading an image in default mode
img = cv2.imread('./mypic.jpg')
    
# Window name in which image is displayed
window_name = 'Image'
  
# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (300, 900)
  
# fontScale
fontScale = 0.5
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
   
# Using cv2.putText() method
image = cv2.putText(img, 'Name : Chinapat Onprasert  ID : 62070505218', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
   
# Displaying the image
cv2.imshow(window_name, image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
