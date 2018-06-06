#!/usr/lib/python3

import cv2
import numpy as np

# capturing live data from Video 
cap = cv2.VideoCapture(0)
list_color = []

while cap.isOpened():
	# redaing data

	# writing data to files
	for i in range(20):
		#print(frame)
		status,frame = cap.read()
		cv2.imshow("image",frame)

		cv2.imwrite("./test_frames/file "+str(i)+".png",frame)

		# to save data from image frame into file ,for size of nparray >2 file extension is .npy
		np.save("./test_frames/file"+str(i)+".npy",frame)
		
		# to load data from files
		data = np.load("./test_frames/file"+str(i)+".npy")

		# loading data and storing in video,it can be noted that image and video both are same for a given instance
		cv2.imwrite("./test_frames/video"+str(i)+".png",data)
		cv2.imshow("videos",data)


	# checking that q is pressed while video is in motion or not	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	
	

cv2.destroyAllWindows()
cap.release()
	




