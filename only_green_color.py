#!/usr/bin/python3

import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():

	for i in range(10):

		status,frame = cam.read()

		#cv2.imshow("real_image",frame)

		#to get color composition of the frames do print(frame) 
		print(frame)

		# for capturing instances of frames formed
		#for i in range(10):
		# see the appropriate ratio of colours by doing print(frame)
		#only_green = cv2.inRange(frame,(100,100,10),(200,200,20))
		only_blue = cv2.inRange(frame,(10,20,20),(20,200,205))
		cv2.imshow("window_blue",only_blue)
		#cv2.imwrite("./frames_images/frames "+str(i)+" .jpg",frame)
		cv2.imwrite("./frame_images/frames "+str(i)+" .jpg",frame)
		#cv2.imshow("real_image",frame)
	

	# 1 is used on waitKey so that frames are get at interval of 1 ms ie to give a real_video shape
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break



cv2.destroyAllWindows()
cam.release()




'''
# load from predefined image
image = cv2.imread("Red.jpg")

#print(image.shape)
#print(image)

only_red = cv2.inRange(image,(0,0,100),(0,20,200))

#cv2.imshow("image",image)
cv2.imshow('window_red',only_red)

cv2.waitKey(0)
cv2.destroyAllWindows()'''
