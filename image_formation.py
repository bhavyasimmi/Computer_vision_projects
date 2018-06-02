#!/usr/bin/python3

import cv2
import numpy as np

# a black image ie with all blocks 0 of shape 400*400
#img = np.zeros((400,400))

# to give color channels also in image
img = np.zeros((400,400,3))		# each cell now has 3 colors either BGR or RGB depending on us

print(img.shape)

shape = img.shape

# shape[0] shows rows in image shape[1] shows column in image
for i in range(0,int(shape[0]),2):
	for j in range(0,int(shape[1]),2):
		img[i][j][0] = 10
		img[i][j][1] = 20
		img[i][j][2] = 80

'''def draw(op,point1,point2):
	if op == 1:
		cv2.circle(img,point1,point2)'''

# to take an image of size 200*200 out of the main image img
img1 = img[0:200,0:200]

center = ()
color = ()
#take user input
design = input("what image do you want to draw\n")
if design == "circle":
	radius = input("enter the radius\n")
	radius = int(radius)
	row = int(input("enter the row of center point in form of tuple\n"))
	column = int(input("enter the column of center point in form of tuple\n"))
	red = int(input("what is the ratio of red color in image\n"))
	green = int(input("what is the ratio of green color in image\n"))
	blue = int(input("what is the ratio of blue color in image\n"))
	width = input("what width do you want for the image : -1 is for completely filling the image\n")
	width = int(width)
	cv2.circle(img,(row,column),radius,(red,green,blue),width)


cv2.imshow("part_image",img1)
cv2.imshow("image_window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
