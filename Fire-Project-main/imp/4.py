from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from glob import glob
# Initialising the CNN
classifier = Sequential()
# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Step 3 - Flattening
classifier.add(Flatten())
# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))
# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('training_set',
target_size = (64, 64),batch_size = 32,class_mode = 'binary')
test_set = test_datagen.flow_from_directory('test_set',target_size = (64, 64),batch_size = 32,class_mode = 'binary')
classifier.fit_generator(training_set,steps_per_epoch = 100,epochs = 3,validation_data = test_set,validation_steps = 10)
# Part 3 - Making new predictions
import numpy as np
from keras.preprocessing import image
count=0
accuracy=0.0
tp=0
fp=0
tn=0
fn=0

img_mask='dataset/Fire/*.jpg'
img_names=glob(img_mask)
for fn in img_names:
	test_image=image.load_img(fn,target_size=(64,64))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)
	training_set.class_indices
	if result[0][0] == 1:
		prediction='no_fire'
		#fn=fn+1
		
			
	else:
		prediction='fire'
		accuracy=accuracy+1
		tp=tp+1
	#print prediction
	count=count+1


img_mask='dataset/No/*.jpg'
img_names=glob(img_mask)
for fn in img_names:
	test_image=image.load_img(fn,target_size=(64,64))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)
	training_set.class_indices
	if result[0][0] == 1:
		prediction='no_fire'
		accuracy=accuracy+1
		tn=tn+1		
	else:
		prediction='fire'
		fp=fp+1
	print prediction
	count=count+1

accuracy=accuracy/count
print "accuracy=",accuracy
print "tp=",tp
print "fp=",fp
print "tn=",tn
#print "fn=",fn