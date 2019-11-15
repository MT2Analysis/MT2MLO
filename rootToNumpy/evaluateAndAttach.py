'''
Script to create a tree with evaluated score
'''

import uproot
import numpy as np
from keras.models import load_model


# branches that were used for training => needed for model prediction
from branches_V01 import outbranches

filename_to_evaluate = '/scratch/mratti/NEWSnTtrees/2016/zinv_ht600to800.root'
filename_friend      = '/t3home/mratti/friend_zinv_ht600to800.root'

with uproot.open(filename_to_evaluate) as f:
  events = f["mt2"]

  ars={}
  # column stack with the **same** order of columns as they were given to the NN
  for i,ib in enumerate(outbranches):
    print('Reading branch=', ib)
    ars[ib] = events.array(ib)
    ars[ib] = ars[ib].reshape((ars[ib].shape[0],1))
    if i==0: X = ars[ib]
    else: X = np.hstack((X, ars[ib]))

print('X=', X)
print('shape=', X.shape)

print('\nLoading model')
loaded_model = load_model('./../models/model_V01.h5')
prediction = loaded_model.predict(X)

prediction = prediction.reshape(prediction.shape[0])
print('reshape prediction is=',prediction )
print('shape=',prediction.shape )

with uproot.recreate(filename_friend) as f:
  f["mt2_friend"] = uproot.newtree({"score_V01": "float64"})
  f["mt2_friend"].extend({"score_V01": prediction})


#training_out = l_model.predict(df[Xnumpy])
