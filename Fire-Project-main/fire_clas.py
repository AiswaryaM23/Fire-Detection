# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:56:42 2018

@author: PAVEETHRAN
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 12:12:47 2018

@author: PAVEETHRAN
"""

import numpy
import tensorflow as tf
import keras
import tensorflow.python
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Activation
#INITIALSE CNN
cl=Sequential()

#ADD INPUT LAYER
cl.add(Conv2D(32,(3,3),activation='relu',input_shape=[64,64,3])) 
#ADD THE MAX POOLING LAYER
cl.add(MaxPooling2D(pool_size=(2,2)))#...same padding is zero padding
#layer 2
cl.add(Conv2D(32,(3,3),activation='relu'))
cl.add(MaxPooling2D(pool_size=(2,2)))

#layer 3
cl.add(Conv2D(32,(3,3),activation='relu'))
cl.add(MaxPooling2D(pool_size=(2,2)))
#layer 4
cl.add(Conv2D(64,(3,3),activation='relu'))
cl.add(MaxPooling2D(pool_size=(2,2)))
#FLATTEN
cl.add(Flatten()) 

#ADING THE FIRST LAYER OF DENSE..to maka a fully connected cnn
cl.add(Dense(activation='relu',output_dim=64))
cl.add(Dropout(0.5))
#O/P LAYER
#cl.add(Dense(activation='softmax',output_dim=3))
cl.add(Dense(1))
cl.add(Activation('sigmoid'))

#ALEXNETT

#ADD INPUT LAYER
cl1.add(Conv2D(32,(3,3),activation='relu',input_shape=[64,64,3])) 
#ADD THE MAX POOLING LAYER
cl1.add(MaxPooling2D(pool_size=(2,2)))#...same padding is zero padding
#layer 2
cl1.add(Conv2D(96,(3,3),activation='relu'))
cl1.add(MaxPooling2D(pool_size=(2,2)))


cl1.add(Conv2D(256,(3,3),activation='relu'))
cl1.add(MaxPooling2D(pool_size=(2,2)))


cl1.add(Conv2D(256,(3,3),activation='relu'))
#layer 4
cl1.add(Conv2D(500,(3,3),activation='relu'))
cl1.add(MaxPooling2D(pool_size=(2,2)))
#FLATTEN
cl1.add(Flatten()) 

#ADING THE FIRST LAYER OF DENSE..to maka a fully connected cnn
cl1.add(Dense(activation='relu',output_dim=500))
cl1.add(Dropout(0.5))

cl1.add(Dense(activation='relu',output_dim=500))
cl1.add(Dropout(0.5))
#O/P LAYER

#cl.add(Dense(activation='softmax',output_dim=3))
cl1.add(Dense(1))
cl1.add(Activation('sigmoid'))
"""
cl.add(Conv2D(32, (3, 3), input_shape=[64,64,3]))
cl.add(Activation('relu'))
cl.add(MaxPooling2D(pool_size=(2, 2)))

cl.add(Conv2D(32, (3, 3)))
cl.add(Activation('relu'))
cl.add(MaxPooling2D(pool_size=(2, 2)))

cl.add(Flatten())
cl.add(Dense(64))
cl.add(Activation('relu'))
cl.add(Dropout(0.5))
cl.add(Dense(3))
cl.add(Activation('sigmoid'))
"""
#Compiling the cnn
cl.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

#IMPLEMENT THE TRAIN AND TEST IMAGES IN CNN
from keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

#LETS DO THISSSSS
trainingset = train_datagen.flow_from_directory('training_set',
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='binary')

                                                    
testset = test_datagen.flow_from_directory( 'test_set',
                                            target_size=(64, 64),
                                            
                                            batch_size=32,
                                            class_mode='binary')


     
cl.fit_generator(trainingset,steps_per_epoch=152,epochs=5,validation_data=testset,validation_steps=15)

#This is to test for images in folders+++++
img=load_img('rr.jpg',target_size=(64,64))
#img = [np.exand_dims(img, 1) if img is not None and img.ndim == 1 else img]
img=img_to_array(img)
img=np.expand_dims(img,axis=0)
pred=cl.predict(img)

trainingset.class_indices
    
import numpy as np
import os
import cv2
import glob
img_dir="te"
dp=os.path.join(img_dir,'*g')
files=glob.glob(dp)
data=[]
count=0
im=0
images=0
from os import listdir
from os.path import isfile, join
#mypath="te"
#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
#images = numpy.empty(len(onlyfiles), dtype=object)
#for n in range(0, len(onlyfiles)):
#  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
#  im=img_to_array(images[2])
#  im=np.expand_dims(im,axis=0)
#  prd=cl.predict(images[2])
#    if p==0:
#        count=count+1
#images=0
#img=0  
#
#for fi in files:
#    img=load_img("te\,target_size=(64,64))
#
#    img=load_img(rr,target_size=(64,64))
#    p=cl.predict(img)
#    tif p==0:
#        count=count+1

x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

#MAKE PREDICTION FOR A SINGLE IMAGE
import numpy as np
    trainingset.class_indices
    
img_dir="te"    
dp=os.path.join(img_dir,'*g')
files=glob.glob(dp)
images=0    
p=0    
fi=0
count=0

for fi in files:
    img=load_img(fi,target_size=(64,64))
    #img = [np.exand_dims(img, 1) if img is not None and img.ndim == 1 else img]
    img=img_to_array(img)
    img=np.expand_dims(img,axis=0)
    pred=cl.predict(img)
    if pred==0:
        count=count+1
        print("FIRE DETECTED!!!")
    img=np.squeeze(img,axis=0)


    

