#!/usr/bin/python3

import cv2
import numpy as np
from os import listdir
import os


files_list = []
datas = []
video_format = cv2.VideoWriter_fourcc(*'XVID')
data1 = np.empty

# reading files with extension .npy from test_frames folder to load all data regarding frames
for files in listdir("./test_frames/"):
	if files.endswith(".npy"):
		files_list.append(files)



for i in range(len(files_list)-1):
	data = np.load("./test_frames/file"+str(i)+".npy")

	print(data.shape)

	np.save("./test_frames/total_data.npy",data)
	#np.save("./test_frames/total_data.npy",np.append(data1,data))
	
	data1 = np.load("./test_frames/total_data.npy")
	
#print(np.load("./test_frames/total_data.npy"))

final_data = np.load("./test_frames/total_data.npy")

#print(type(final_data))
#print(final_data.shape)

shape = final_data.shape
#final_data = final_data.reshape((640,480,3))

# size of video is (640*480) as per my webcam so make size to be (shape[1],shape[0])
video_out = cv2.VideoWriter('./test_frames/video.avi',video_format,20.0,(640,480))

video_out.write(final_data)

