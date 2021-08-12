# ***************************** HOW TO USE !!!!
#           1. Wait for the programme to run.
#           2. Enter a certain value which corresponds to a data in test
#           3. View the expected output, actual output and the actual figure!
# ***************************************************************************


# Results:     
    # accuracy: 0.9951 
    # loss: 0.0161  
    # val_loss: 0.0728 
    # val_accuracy: 0.9811
    # ********************


import tensorflow as tf
import numpy as np
import os
from tensorflow import keras
from tensorflow.keras import layers
from keras.datasets import mnist
from matplotlib import pyplot

(trainData, trainLabels), (testData, testLabels) = mnist.load_data()

trainData = trainData / 255.0
testData = testData / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # input layer (1)
    keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
    keras.layers.Dense(10, activation='softmax') # output layer (3)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(trainData, trainLabels, epochs=10, 
                    validation_data=(testData, testLabels))


# test_loss, test_acc = model.evaluate(testData,  testLabels, verbose=1) 
# print('Test accuracy:', test_acc)

clear = lambda: os. system('cls')
clear()


while True:
    i = int(input("Enter a number and get the prediction corresponding to the number: "))
    predictions = model.predict(testData)
    print("Expected output: ", testLabels[i])
    print("Actual output: ", np.argmax(predictions[i]))
    pyplot.imshow(testData[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show()