#!/usr/bin/python3

import cv2
import time

image = input("which image do you want to open\n")

#read the user image by default in colorful mode
img = cv2.imread(image)

#loading the actual image
print("actual image is\n")
cv2.imshow("actual_image",img)
cv2.waitKey(4)
cv2.destroyAllWindows()

time.sleep(1)
shape = img.shape
print("actual size of image is :",shape)

i = input("how much part of the image do you want to see\n")

if i == "1/2":
	part = 2
elif i == "1/3":
	part = 3
elif i == "1/4":
	part = 4
elif i == "1/8":
	part = 8


# partition of image as per user partitions
user_image = img[0:int(shape[0]/part),0:int(shape[1]/part)]

print("the image after partition is\n")
#cv2.imshow("user_image",user_image)

rem_image = img[int(shape[0]/part):shape[0],int(shape[1]/part):shape[1]]

cv2.imshow("remaining_image",rem_image)


#time.sleep(4)
cv2.waitKey(0)
cv2.destroyAllWindows()
