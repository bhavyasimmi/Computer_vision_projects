#!/usr/bin/python3

import cv2
import numpy as np
 
if __name__ == '__main__' :
 
    # Read image
	im = cv2.imread('butterfly.jpg')
	print(im.shape)

    # Select ROI
	r = cv2.selectROI(im)
	print(r)     

    # Crop image
	#imCrop = im[0:215,0:330]

	#imCrop = im[r[1]:r[0],r[3]:r[2]] 
	#print(imCrop.shape)	
	
	x1 = r[0]
	y1 = r[1]
	x2 = r[2]
	y2 = r[3]	

	# to crop an image crop_img = image[y:y+h,x:x+w]
	crop = im[y1:(y1+y2),x1:(x1+x2)]
	imCrop = crop

    # Display cropped image

	#after observing the cropped image is somewhere having first point as (r[0],r[1]) and last or 4th point as ((r[0]+r[2]),(r[1]+r[3]))
	#cv2.line(im,(x1,y1),((x1+x2),(y1+y2)),(255,0,0),8)
	#cv2.rectangle(im,(x1,y1),((x1+x2),(y1+y2)),(0,0,255),8)


	cv2.imshow("new_image",im)
	cv2.imshow("crop_image",imCrop)
	cv2.imshow("Image", crop)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


















# read 
# system calls
# target files that starts at boot time
# unwanted system activities
#pam
