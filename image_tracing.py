#!/usr/bin/python3

# import module of computer vision
import cv2

#read image
img = cv2.imread("/home/bhavyaagrawal/Pictures/img.png")

#img.reshape(400,500,3) the reshape on actual image can't be done this ways

shape = img.shape
#shape is of type float so first do it int to apply normal maths on it

# for alternate boxes of image
for i in range(0,int(shape[0]/2),2):
	for j in range(0,int(shape[1]),2):
		img[i][j][0] = 0		#showing red or blue color its BGR 
		img[i][j][1] = 255		#showing green color
		img[i][j][2] = 0		#showing red or blue color depending on its BGR or RGB

#show image
cv2.imshow("image_window",img)

print("image shape is  ",img.shape)
print("image size is  ",img.size)


# let the window always wait for some user action for 2ms
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()


