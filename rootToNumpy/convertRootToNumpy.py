
import uproot
import numpy as np

if __name__ == "__main__":

  inputbkg = '/scratch/mratti/NEWSnTtrees/2016/zinv_ht1200to2500.root'
  #inputsig = '/pnfs/psi.ch/cms/trivcat/store/user/mratti/NEWSnTtrees/2016/T1qqqq_94x.root'
  inputs = [inputbkg]
  #prefix = 'root://t3dcachedb.psi.ch:1094/'

  inbranches=[
  'ht',
  'mt2',
  'jet1_pt',
  ]

  for infile in inputs:
    
    ##f = uproot.open(prefix+infile)
    f = uproot.open(infile)
    events = f["mt2"]

    ars={}
    for ib in inbranches:
      ars[ib]=events.array(ib)
      np.save('./output/{}.npy'.format(ib), ars[ib], allow_pickle=False)
   
