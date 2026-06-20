import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

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

		##cv2.imshow('image',data_img)
		##break
		
	##break
##print(len(data))

##cv2.waitKey(0)
#cv2.destroyAllWindows()
pick_in=open('data1.pickle','wb')
pickle.dump(data,pick_in)
pick_in.close()

pick_in=open('data1.pickle','rb')
data=pickle.load(pick_in)
pick_in.close()

random.shuffle(data)
features=[]
labels=[]

for feature,label in data:
	features.append(feature)
	labels.append(label)

xtrain,xtest,ytrain,ytest=train_test_split(features,labels,test_size=0.55)

#model=SVC(C=1,kernel='poly',gamma='auto')
#model.fit(xtrain,ytrain)

pick=open('medel.sav','rb')
model=pickle.load(pick)
pickle.dump(model,pick)
pick.close()

prediction=model.predict(xtest)
accuracy=model.score(xtest,ytest)

categories=['fire','nonfire']

print('Accuracy: ',accuracy)
print('prediction is : ',categories[prediction[0]])

myproject=xtest[0].reshape(50,50)

plt.inshow(myproject,cmap='gray')
plt.show()