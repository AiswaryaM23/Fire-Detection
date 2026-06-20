import numpy as np 
import matplotlib.pyplot as plt 
import os
import cv2

DATADIR="C:\\Users\\ATHIRA\\OneDrive\\Desktop\\Fire Project\\dataset"
CATAGORIES=["fire","nonfire"]

for category in CATAGORIES:
    path=os.path.join(DATADIR,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array,cmap="gray")
        plt.show()
        break
    break  

print(img_array.shape)
IMG_SIZE=50
new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
plt.imshow(new_array,cmap='gray')
plt.show()

training_data=[]
def create_training_data():
    for category in CATAGORIES:
        path=os.path.join(DATADIR,category)
        class_num=CATAGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass
create_training_data()

print(len(training_data))

import random
random.shuffle(training_data)

for sample in training_data:
    print(sample[1])

x=[]
y=[]

for features,label in training_data:
    x.append(features)
    y.append(label)

x=np.array(x).reshape(-1,IMG_SIZE,IMG_SIZE,1)

import pickle

pickle_out=open("x.pickle","wb")
pickle.dump(x,pickle_out)
pickle_out.close()

pickle_out=open("y.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()

pickle_in=open("x.pickle","rb")
x=pickle.load(pickle_in)
x[1]


#======================================================
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

x=pickle.load(open("x.pickle","rb"))
y=pickle.load(open("y.pickle","rb"))

x=x/255.0
x.shape
model=Sequential()
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128,input_shape=x.shape[1:],activation="relu"))

model.add(Dense(2,activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
y = np.array(y)
x = np.array(x)
model.fit(x, y, epochs=5, validation_split=0.1)


from keras.preprocessing import image
test_image = image.load_img('C:\\Users\\ATHIRA\\OneDrive\\Desktop\\Fire Project\\dataset\\fire\\frame3.jpg', target_size = (64, 64))
plt.imshow(test_image,cmap='gray')
plt.show()


def predict_image(imagepath):
    predict = image.load_img(imagepath, target_size = (64, 64))  
    IMG_SIZE=50
    predict=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
    predict_modified = image.img_to_array(predict)
    predict_modified = predict_modified / 255
    predict_modified = np.expand_dims(predict_modified, axis = 0)
    result = model.predict(predict_modified)
    
   # print("ROUND : ",round(result[0][0]))
    if result[0][0] <1:
        from twilio.rest import Client
        account_sid ='AC4544a12103ec4839ab8d10b17fcd88c1'
        auth_token ='9192ca5508269df7efc29b0b239ee288'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="FIRE ALERT!!",
            from_='+16067160811',
            to='+919074354819'
        )
        print(message.sid)
        prediction = 'Fire'
        probability = result[0][0]
        #print ("probability = " + str(probability))
        print("Prediction = " + prediction)
        
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        
    else:
        prediction = 'Not Fire'
        probability = 1 - result[0][0]
        #print ("probability = " + str(probability))
        print("Prediction = " + prediction)
        
predict_image("C:\\Users\\ATHIRA\\OneDrive\\Desktop\\Fire Project\\dataset\\fire\\frame47.jpg")

