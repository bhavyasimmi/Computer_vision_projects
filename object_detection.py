#!/usr/bin/python3

import cv2

cap = cv2.VideoCapture(0)

#reading 3 consecutive frames for an instance at once snapshot when camera is just opened for the first time
tp1 = cap.read()[1]
tp2 = cap.read()[1]
tp3 = cap.read()[1]

gray1 = cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY) 

# function to detect difference between actual and moved image
def detect(x,y,z):


	diff1 = cv2.absdiff(gray1,gray2)
	diff2 = cv2.absdiff(gray2,gray3)
	# to compare the movement of any body part through 2 differences each between the successive frames taken 
	compare = cv2.bitwise_and(diff1,diff2)

	return compare


while cap.isOpened():
	
	# to get return of detect() method into a comparison variable to show it
	comparison = detect(gray1,gray2,gray3)
	cv2.imshow("comparison_detected_images",comparison)

	# reading next 3 frames
	gray1 = gray2
	gray2 = gray3
	gray3 = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2GRAY)

	status,frame = cap.read()
	cv2.imshow("original_image",frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()		


