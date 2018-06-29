#!/usr/bin/python3

import cv2

# take the instance of computer camera 0 for inbuilt camera and 1 for any external camera
cam = cv2.VideoCapture(0)

#if camera is opened cv2.isOpened() returns True
while cam.isOpened():
	# status of image is returned in status variable and real frames of image in frame variable
	status,frame = cam.read()

	# to change color of image to black and white
	new_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	#to run image frame window name is let say camera0
	cv2.imshow("camera0",frame)
	cv2.imshow("camera1",new_image)

	# for saving image frames
	for i in range(1000):
		cv2.imwrite("frames_of_image.jpg",frame)

	# if no action taken by the user regarding window and not quited by action of 'q' button till the the live images will be taken on pressing any button on the keyboard 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
#after destroying all windows at the last release the camera thread
cam.release()
