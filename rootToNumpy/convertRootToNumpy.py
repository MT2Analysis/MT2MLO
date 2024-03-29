'''
Script to apply pre-selection, feature reduction
Input is a ROOT TTree per file
output is a numpy array per file of format:

[
  [feature1_evt0, feature2_evt0, ..., featureX_evt0],
  [feature1_evt1, feature2_evt1, ..., featureX_evt1],
  [..],
  [feature1_evtN, feature2_evtN, ..., featureX_evtN],
]
'''

import uproot
import numpy as np
import os

if __name__ == "__main__":

  debug=True
  prodLabel='V01'
  from branches_V01 import inbranches,outbranches
  from files_V01 import bkgs,sigs

  outputdir='./output/skim_{}/'.format(prodLabel)
  os.system('mkdir -p {}'.format(outputdir))

  # check that output is a subset of input 
  if not (all(x in inbranches for x in outbranches)): raise RuntimeError('logic error, check lists of in and out branches')

  # get input files
  inputs = bkgs+sigs

  for infile,infileNickname in inputs:

    print('reading file =',infile)    

    # open file and get the tree
    f = uproot.open(infile)
    events = f["mt2"]

    # get all interesting branches for this root file
    ars={}
    for ib in inbranches:
      ars[ib] = events.array(ib)
      print ('  reading ib =',ib)
      print ('  ars[ib]=', ars[ib])
      print ('  ars[ib] shape=', ars[ib].shape)
      #print ('  transpose=', np.transpose(ars[ib]))
      #print ('  transpose shape=', np.transpose(ars[ib]).shape)
      #np.save('./output/{}.npy'.format(ib), ars[ib], allow_pickle=False)


    # define the selection array
    selection = (   (ars['nJet30']>0) & (ars['ht']>250)  \
                     & (((ars['ht']<1200) & (ars['met_pt']>250) )| ((ars['ht']>=1200) & (ars['met_pt']>30))) \
                     & (((ars['ht']<1500) & (ars['mt2']>200)) | ((ars['ht']>=1500) & (ars['mt2']>400))) \
                     & (ars['deltaPhiMin']>0.3) \
                     #& ((ars['mht_pt']<(1.5*ars['met_pt'])) | (ars['mht_pt']>(0.5*ars['met_pt']))) \
                     & (ars['nMuons10']==0) & (ars['nElectrons10']==0) \
                     & (ars['nPFLep5LowMT']==0) & (ars['nPFHad10LowMT']==0)
                  )

    print('WARNING setting selection to zero')

    if debug:
      print('  selection array=' , selection)
      print('  shape ht=',        ars['ht'].shape) 
      print('  shape selection=', selection.shape)
      #print('  ht after selection=', ars['ht'][selection])
      print('  shape ht after selection=', ars['ht'][selection].shape)


    # define the label array and use it as first array on which the output arrays are stacked
    label = ( (ars['GenSusyMScan1']!=0) & (ars['GenSusyMScan2']!=0)  ) # True for sig, False for bkg
    stacked = label[selection]
    # make it columnar
    stacked = stacked.reshape((stacked.shape[0],1))

    for ob in outbranches:
      column = ars[ob][selection].reshape(ars[ob][selection].shape[0],1) 
      stacked = np.hstack((stacked, column))
      print('Growing shape of stacked=', stacked.shape)

    np.save('{}/{}.npy'.format(outputdir,infileNickname), stacked, allow_pickle=False)
    print('Saved numpy array in {}/{}.npy'.format(outputdir,infileNickname))
