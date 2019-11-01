
import numpy as np

inputarrays = [
  'ht',
  'mt2',
  'jet1_pt',
]

for ia in inputarrays:
  print('Loading array={i}'.format(i=ia))
  data = np.load('../rootToNumpy/output/{i}.npy'.format(i=ia))
  print(data)
