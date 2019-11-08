import numpy as np
import glob
# Load layers from keras
#from keras.layers import Dense
#from keras.models import Sequential
#from keras.losses import binary_crossentropy

# loading all numpy arrays in relevant dir
prodLabel='V00'
inputfiles='../rootToNumpy/output/skim_{}/*npy'.format(prodLabel)


data = np.array([])
for f in glob.glob(inputfiles):
  print('Loading first np array from file =' , f)
  data = np.load(f)
  break

for f in glob.glob(inputfiles):
  print('Stacking np array from file =' , f)
  data = np.hstack((data,np.load(f)))


X = data[1:,:] # all tabular w/o first row
y = data[0, :]  # a rabular  w/ first row only

print(X.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

############
## important: do batch rescaling 
###########

## Setup network
#model = Sequential()
#model.add(Dense(20, activation="relu", input_shape=(X.shape[1],)))
#model.add(Dense(40, activation="relu"))
#model.add(Dense(1, activation="sigmoid"))
#
## Compile model
#model.compile(optimizer="adam", loss="binary_crossentropy")
#
## Train model
#history = model.fit(x=X_train, y=y_train, validation_data=(X_test, y_test), epochs=100, batch_size=10000)
#
## evaluate
#results = model.predict(X_test, batch_size=10000)
#
#from sklearn.metrics import roc_auc_score
#auc = roc_auc_score(y_test, results)
#
#print("area under ROC curve: ", auc)
#
#
##
