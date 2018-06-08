#!/usr/bin/python3

import requests

url = "https://api.kairos.com/detect"
# put your keys in the header taken from kairos page

headers = {
    "app_id": "2b0335d7",
    "app_key": "28e7a2915e876413a7f33b2eccd06a62"
	}

#files= {'image':open('./test_frames/file 0.png','rb')}

files= {'image':open('/home/bhavyaagrawal/Downloads/profile.jpg','rb')}


# make request
r = requests.post(url, files=files, headers=headers)
print(r.text)
