import numpy as np 
import cv2

path = "luffy.jpg"
image = cv2.imread(path)

# converting the coloured image to greyscale 
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#inverting the image
invert_image = 255 - grey_image

#applying gaussian blur to image
blurred = cv2.GaussianBlur(invert_image, (21,21) , -1)

#inverting the blurred image
invert_blur = 255 - blurred

#converting the processed image to pencil sketch 
pencil_sketch = cv2.divide(grey_image ,invert_blur , scale = 250.0)
final_image = np.concatenate((grey_image, pencil_sketch) , axis=1)

#displaying the image
cv2.imshow("final_image(grey + sketch)",final_image)
cv2.waitKey(0)

