import cv2
import numpy as np
import glob
import os

inputFile = 'Record.mp4'
os.mkdir('Frame_Folder')

vidcap = cv2.VideoCapture('Record.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
	success,image = vidcap.read()
	cv2.imwrite("Frame_Folder/frame%d.jpg" % count, image)     # save frame as JPEG file
	if cv2.waitKey(10) == 27:                     # exit if Escape is hit
		break
	count += 1


cv2.destroyAllWindows()