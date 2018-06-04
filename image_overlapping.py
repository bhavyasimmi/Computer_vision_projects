#!/usr/bin/python3

import cv2
import numpy as np


dog = cv2.imread("dog.jpg")
cat = cv2.imread("cat.jpg")


# print shapes of both pictures

print(dog.shape)
print(cat.shape)

cv2.imshow("dog_image",dog)
cv2.imshow("cat_image",cat)

#after tracing both pics lets takeout the nose of dog and fix it on equal sized nose of cat

#taking about 20*20 of both pics (dog has nose somewhere around 131*138)
dog_nose = dog[121:141,128:148]

#pic of dog's nose
#cv2.imshow("dog_nose",dog_nose)

#takeout equal piece of 20*20 cat's nose so that the cat nose can be replaced by dogs and dogs by nose of cat
cat_nose = cat[131:151,88:108]

#pic of cat's nose
cv2.imshow("cat_nose",cat_nose)


#adding nose of dog on cat (iamge of dogs nose overwritten on nose of cat) 
nose_add = cv2.addWeighted(cat_nose,.01,dog_nose,1,1)
#dog_nose.copyTo(cat_nose)


# trying to add portions passing values of dog_nose to cat_nose
cat_nose = dog_nose

# by now the actual cat_nose is replaced by that of dog's_nose

# to see if the values of dog's_nose passed to cat's_nose or not
if cat_nose.all == dog_nose.all:
	image = cv2.add(cat_nose,cat_nose)
	cv2.imwrite("new_cat.jpeg",image)
	print("matched")



# ie match whereever the color is reddish do black over there using numpy integrated with cv2
#cat[np.where((cat == [255,255,255]).all(axis = 2))] = [0,0,0]

#changing the color wherever cat is white do it black over there and save as output.png
cat[np.where(cv2.inRange(cat,(100,100,100),(230,230,230)))] = [0,0,0]
cv2.imwrite('output.png', cat)

#cv2.imshow("new_cat_nose",cat_nose)
cv2.imshow("new_cat",cat)


cv2.waitKey(0)
cv2.destroyAllWindows() 
