#!/usr/bin/python
#_*_ coding: utf-8 _*_

from keras.models import Sequential
from keras.layers import Dense, Dropout
from data_handle import data_handle
from merge import merge_csv

# Generate dummy data

def train(handled_data, tag):
	x_train = handled_data
	y_train = tag
	#y_train.reshape(-1,1)
	#x_train.reshape(-1,1)
	x_test = handled_data
	y_test = tag

	model = Sequential()
	model.add(Dense(64, input_dim=1, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(64, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(1, activation='sigmoid'))

	model.compile(loss='binary_crossentropy',
		      optimizer='rmsprop',
		      metrics=['accuracy'])
	model.fit(x_train, y_train,
		  epochs=20,
		  batch_size=128)
	score = model.evaluate(x_test, y_test, batch_size=128)

if __name__ == "__main__":
	merge_csv()
	handled_data, tag = data_handle()
	train(handled_data, tag)
