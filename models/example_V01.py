# Check settings
import tensorflow as tf
from keras import backend as K
print("-------------------------------------------")
print("GPU available: ", tf.test.is_gpu_available())
print("Keras backend: ", K.backend())
print("-------------------------------------------")

import numpy as np
import pandas as pd
import glob
# Load layers from keras
from keras.layers import Dense
from keras.models import Sequential
from keras.losses import binary_crossentropy

# loading all numpy arrays in relevant dir
prodLabel='V01'
inputfiles='../rootToNumpy/output/skim_{}/*npy'.format(prodLabel)


count=0
for f in glob.glob(inputfiles):
  print('Loading  array from file =' , f)
  if count==0: data = np.load(f)
  else: data = np.vstack((data,np.load(f)))
  count+=1

print(data)
#data = np.vstack((data,np.load(f)))
#data.append(pd.DataFrame(np.load(f)))

#print('Going to shuffle rows of this dataset, i.e. shuffle the order of the events not the order of the features')
#np.random.shuffle(data)
#print(data)

print('Going to separate array into X and Y')
X = data[:, 1:] # all tabular w/o first column 
y = data[:, 0 ] # a tabular w/ first column only

print('X=', X)
print('shape=', X.shape)

print('Y=' , y)
print('shape=',  y.shape)
#X = data[1:,:] # all tabular w/o first row
#y = data[0, :]  # a rabular  w/ first row only


from sklearn.model_selection import train_test_split

#print('only take a small subset and leave the rest') # selecting only 10% of events for analysis
#X_train, X_left, y_train, y_left = train_test_split(X, y, test_size=0.9, random_state=123)

#print('divide into training (90%) and validation (10%)')
#X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=231)

print('divide into training (90%) and validation (10%)')
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=42)

############
## important: do batch rescaling 
###########

# Setup network
model = Sequential()
model.add(Dense(80, activation="relu", input_shape=(X.shape[1],)))
model.add(Dense(80, activation="relu"))
model.add(Dense(80, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

# Compile model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])

# Train model
history = model.fit(x=X_train, y=y_train, validation_data=(X_val, y_val), epochs=10, batch_size=100000)

# evaluate
results = model.predict(X_val, batch_size=10000)

from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_val, results)

print("area under ROC curve: ", auc)

# save model
model.save('model_V01.h5')
print('Saved model')

