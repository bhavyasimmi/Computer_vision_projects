#!/usr/bin/python3

import cv2

cap = cv2.VideoCapture(0)
video_format = cv2.VideoWriter_fourcc(*'XVID')

# get width and height of the image taken by webcam
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width)
print(height)


# capture video in file video.avi with video_format,FramesPerSecond = 20.0,with given width and height
video_out = cv2.VideoWriter('video.avi',video_format,20.0,(int(width),int(height)))

while cap.isOpened():
	status,frame = cap.read()
	cv2.imshow("live_image",frame)
	# to write video to a file video.avi
	video_out.write(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()
		
