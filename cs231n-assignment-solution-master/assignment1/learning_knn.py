# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:16:54 2018

@author: Administrator
"""

from __future__ import print_function

import random
import numpy as np
from cs231n.data_utils import load_CIFAR10
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']=(10.0,8.0)
plt.rcParams['image.interpolation']='nearest'
plt.rcParams['image.cmap']='gray'

# Load the raw CIFAR-10 data
cifar10_dir='cs231n/datasets/cifar-10-batches-py'

#Cleaning up variable
try:
    del X_train,y_train
    del X_test,y_test
    print('Clear previously loaded data.')
except:
    pass

X_train,y_train,X_test,y_test=load_CIFAR10(cifar10_dir)
#print out the size of the training and test data

print('Training data shape:',X_train.shape)
print('Training labels shape:',y_train.shape)
print('Test data shape:',X_test.shape)
print('Test labels shape:',y_test.shape)

#Visualize
#We show a few examples of training images from each class
classes = ['plane','car','bird','cat','deer','dog','frog','horse','ship','truck']
num_classes=len(classes)
samples_per_class=7
for y,cls in enumerate(classes):
    idxs=np.flatnonzero(y_train == y)
    #通过给定的一维数组数据产生随机采样，在第一个参数的范围下随机采样，第二个参数
    #决定了输出的shape，而replace=False则表示采样的数字不重复
    idxs=np.random.choice(idxs,samples_per_class,replace=False)
    for i,idx in enumerate(idxs):
        plt_idx=i*num_classes +y+1
        plt.subplot(samples_per_class,num_classes,plt_idx)
        plt.imshow(X_train[idx].astype('uint8'))
        plt.axis('off')
        if i==0:
            plt.title(cls)
plt.show()

#Subsample the data for more efficient code excution in this exercise
num_training=5000
mask=list(range(num_training))
X_train=X_train[mask]
y_train=y_train[mask]

num_test=500
mask=list(range(num_test))
X_test=X_train[mask]
y_test=y_test[mask]
##有疑问，下一模块存在的必要性

#reshape the image data into rows
X_train=np.reshape(X_train,(X_train.shape[0],-1))
X_test=np.reshape(X_test,(X_test.shape[0],-1))
print(X_train.shape,X_test.shape)

from cs231n.classifiers import KNearestNeighbor

classifier=KNearestNeighbor()
classifier.train(X_train,y_train)

#compute_distances_two_loops
dists=classifier.compute_distances_two_loops(X_test)
print(dists.shape)

#visualise
plt.imshow(dists,interpolation='none')
plt.show()

#predict
y_test_pred=classifier.predict_labels(dists,k=1)

#compute the fraction of correctly predicted example
num_correct = np.sum(y_test_pred==y_test)
accuracy=float(num_correct)/ num_test
print('Got %d / %d correct=>accuracy: %f' % (num_correct,num_test,accuracy))