#!/usr/bin/python3

import cv2
import numpy as np

#image = np.zeros((512,512,3))
image = cv2.imread("circle.png")

i = 200
j = 50

# write text on image
#           image    text           position of text     font of text    font_size    color   font_width   line_type
cv2.putText(image, "Text on image", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1 , (0,0,250), 1, cv2.LINE_AA)



#make check shape  at points in image see image circle.png in current folder
'''for i in range(0,image.shape[0],64):
	for j in range(0,image.shape[1],64):
		#image[i][j][0] = 255
		#image[i][j][1] = 255
		#image[i][j][2] = 255
		#cv2.imshow("draw_circle",image)
		cv2.rectangle(image,(i,j),(i+64,j+64),(255,255,255),-1)
		cv2.imwrite("new_circle.png",image)
		cv2.imshow("draw_circle",image)'''


# draw checks like in chess
'''for i,j in range(0,image.shape[0],64),range(0,image.shape[1],64):
		cv2.rectangle(image,(i,j),(i+64,j+64),(255,255,255),-1)
		cv2.imwrite("new_chess.png",image)
		cv2.imshow("draw_chess",image)'''		


# make circles on the checked image 
while i!=0:
	cv2.circle(image,(256,256),i,(100+j,10+j,50+j),-1)
	#cv2.circle(image,(256,256),i,(255,0,0),8)
	cv2.imwrite("new_circle.png",image)
	cv2.imshow("draw_circle",image)
	i = i-10
	j = j+10


# for making 3 consecutive circles
'''cv2.circle(image,(256,256),i,(255,0,0),-1)
cv2.circle(image,(256,256),i-20,(0,255,0),-1)
cv2.circle(image,(256,256),i-50,(0,0,255),-1)'''
	

'''cv2.imwrite("new_circle.png",image)
cv2.imshow("draw_circle",image)'''
cv2.waitKey(0)
cv2.destroyAllWindows()
