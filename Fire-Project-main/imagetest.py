import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

dir="C:\\Users\\ATHIRA\\OneDrive\\Desktop\\Fire Project\\dataset"
categories=['fire','nonfire']

for category in categories:
	path=os.path.join(dir,category)
	
	for img in os.listdir(path):
		imgpath=os.path.join(path,img)
		data_img=cv2.imread(imgpath,5)
		cv2.imshow('image',data_img)
		
		break
		
	break

cv2.waitKey(0)
cv2.destroyAllWindows()