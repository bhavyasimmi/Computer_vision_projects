#!/usr/bin/python3

import cv2

cap = cv2.VideoCapture(0)
#read images
img1 = cap.read()[1]
img2 = cap.read()[1]

black1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
black2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#cv2.imshow("image",cap.read()[1])

'''
#comparing the 2 iamges
diff1 = cv2.subtract(img1,img2)

#cv2.imshow("difference in images",diff1)

#for better difference between the 2 images
diff2 = cv2.absdiff(black1,black2)
diff3 = cv2.absdiff(black2,black1)

#cv2.imshow("difference in images",diff2)

#print(diff2)
#print(diff3)
if diff2.all() == diff3.all():
	print("yes")

# for checking the difference between the 2 images via bitwise and operation
diff4 = cv2.bitwise_and(diff2,diff3)
#print(diff4)
# diff4 is in the form of nparray,for checking all its elements use nparray_name.all() method
if diff4.all == 1:
	print("the 2 images are identical")
else:
	print("the 2 images are not identical")
'''

while cap.isOpened():
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	img1 = cap.read()[1]
	img2 = cap.read()[1]

	black1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	black2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

	diff2 = cv2.absdiff(black1,black2)
	diff3 = cv2.absdiff(black2,black1)

	diff4 = cv2.bitwise_and(diff2,diff3)

	if diff4.all() == black1.all():
		print("No movement detected")
	else:
		print("Movement detected")
	
	cv2.imshow("diff",diff4)

	cv2.imwrite("/home/bhavyaagrawal/Desktop/image.png",diff4)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()

cap.release()
