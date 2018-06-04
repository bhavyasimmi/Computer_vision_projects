#!/usr/bin/python3

import cv2
import numpy as np

f1 = cv2.imread("flower.jpeg")
f2 = cv2.imread("flower1.jpeg")

cv2.imshow("flower1",f1)
cv2.imshow("flower2",f2)

print(f1.shape)
print(f2.shape)


cut_f1 = f1[0:int(f1.shape[0]/2),0:int(f1.shape[1]/2)]
cut_f2 = f2[0:int(f2.shape[0]/2),0:int(f2.shape[1]/2)]


cv2.imshow("cut_flower1",cut_f1)
cv2.imshow("cut_flower2",cut_f2)

print(cut_f1.shape)

# size is 94*100 because in row wise frow 100 to 200 (94 ) are available and in column wise from 100 to 200 (100) are available out of actual size of image ie (194*254)

print(cut_f2.shape)


#assigning values of (100*100) out of f1 to (100*100) of f2
cut_f1 = cut_f2
if cut_f1.all == cut_f2.all:
	print("matched and equated")


new_image = cv2.add(cut_f1,cut_f2)
#cv2.imshow("new_image",new_image)


# merging data of flower2 in flower1 using the concept of numpy array
for i in range(0,cut_f1.shape[0]):
	for j in range(0,cut_f1.shape[1]):
		f1[i][j] = cut_f2[i][j]
		f1[2*i][2*j] = cut_f2[i][j]		
			

#f1.add(new_image)

cv2.imwrite('new_merged_flower.png',f1)
cv2.imshow("flower",f1)
cv2.waitKey(0)
cv2.destroyAllWindows


