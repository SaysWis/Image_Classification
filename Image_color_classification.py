import cv2
import numpy as np

input_image = cv2.imread('Test.png')
hsv_input_image = cv2.cvtColor(input_image,cv2.COLOR_BGR2HSV)

###################Color Boundaries######################### 
# Yellow Color Boundaries in HSV
lower_Yellow = np.array([20, 100, 100])
upper_Yellow = np.array([30, 255, 255])

# Blue Color Boundaries in HSV
lower_Blue = np.array([100,150,0])
upper_Blue = np.array([140,255,255])

# Gray Color Boundaries in HSV
lower_Gray = np.array([0, 0, 40])
upper_Gray = np.array([180, 0, 230])

###############Apply Mask to the image###################### 
mask_Yellow = cv2.inRange(hsv_input_image, lower_Yellow, upper_Yellow)
res_Yellow = cv2.bitwise_and(input_image,input_image, mask= mask_Yellow)

mask_Blue = cv2.inRange(hsv_input_image, lower_Blue, upper_Blue)
res_Blue = cv2.bitwise_and(input_image,input_image, mask= mask_Blue)

mask_Gray = cv2.inRange(hsv_input_image, lower_Gray, upper_Gray)
res_Gray = cv2.bitwise_and(input_image,input_image, mask= mask_Gray)

############Apply Morph to clean the image##################
morph_Yellow = cv2.morphologyEx(res_Yellow, cv2.MORPH_CLOSE, np.ones((5,5),np.uint8)) 
morph_Blue = cv2.morphologyEx(res_Blue, cv2.MORPH_CLOSE, np.ones((5,5),np.uint8))
morph_Gray = cv2.morphologyEx(res_Gray, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))

##################Create the full image#####################
image_output = morph_Yellow + morph_Blue + morph_Gray

#################Save the different image###################
cv2.imwrite('Yellow.png',res_Yellow)
cv2.imwrite('Blue.png',res_Blue)
cv2.imwrite('Gray.png',res_Gray)


cv2.imwrite('Yellow_morph.png',morph_Yellow)
cv2.imwrite('Blue_morph.png',morph_Blue)
cv2.imwrite('Gray_morph.png',morph_Gray)

cv2.imwrite('image_output.png',image_output)