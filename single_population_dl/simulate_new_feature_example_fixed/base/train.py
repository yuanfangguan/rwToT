import numpy as np
import full
import random
import copy
import os
import pickle
import sys
from scipy.interpolate import interp1d
import keras

batch_size=8
train_gs=np.loadtxt('train.dat')[:,0]
train_feature=np.loadtxt('train.dat')[:,1:]

all_set=np.loadtxt('train.dat')
total_n=len(all_set)

train_set=[]
i=0
while (i<int(total_n*0.8)):
    train_set.append(all_set[i,:])
    i=i+1

validation_set=[]
while (i<total_n):
    validation_set.append(all_set[i,:])
    i=i+1


def generate_data(train_set, batch_size, if_train):
    i = 0
    while True:
        image_batch = []
        label_batch = []
        for b in range(batch_size):
            if i == len(train_set):
                i = 0
                random.shuffle(train_set) ## shuffle after epoch
            image= train_set[i][1:]
            label=train_set[i][0]
            image_batch.append(image.reshape((len(image),1)))
            label_batch.append(label)#.reshape((1,1)))
            i = i+1

        image_batch=np.asarray(image_batch) ## data
        label_batch=np.asarray(label_batch) ## label
        yield (image_batch, label_batch)



size=len(all_set[0,:])-1

model = full.full1d(size) ## output length should be dynamically determined. 
name_model='weights_0.h5' ### save the parameters
callbacks = [
    keras.callbacks.ModelCheckpoint(os.path.join('./', name_model),
    verbose=0, save_weights_only=False,save_best_only=True,monitor='val_loss')
    ]

model.fit_generator(
    generate_data(train_set, batch_size,True),
    steps_per_epoch=int(len(train_set) // batch_size), epochs=10,
    validation_data=generate_data(validation_set,batch_size,False),
    validation_steps=int(len(validation_set) // batch_size),callbacks=callbacks)


