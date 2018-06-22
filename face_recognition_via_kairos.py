#!/usr/bin/python3

import requests

url = "https://api.kairos.com/detect"
# put your keys in the header taken from kairos page

headers = {
    "app_id": "##########",
    "app_key": "########################"
	}

#files= {'image':open('./test_frames/file 0.png','rb')}

files= {'image':open('/home/bhavyaagrawal/Downloads/profile.jpg','rb')}


# make request
r = requests.post(url, files=files, headers=headers)
print(r.text)
