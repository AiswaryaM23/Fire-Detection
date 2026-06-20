import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

dir="C:\\Users\\ATHIRA\\OneDrive\\Desktop\\Fire Project\\dataset"
categories=['fire','nonfire']
data=[]

for category in categories:
	path=os.path.join(dir,category)
	label=categories.index(category)

	for img in os.listdir(path):
		imgpath=os.path.join(path,img)
		data_img=cv2.imread(imgpath,0)
		
		try:
			data_img=cv2.resize(data_img,(50,50))
			image=np.array(data_img).flatten()
			data.append([image,label])

		except Exception as e:
			pass
			
print(len(data))
