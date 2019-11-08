# MT2MLO
Package to optimize MT2 Analysis with ML-based methods

Will contains several tools:
- to convert ROOT ntuples into Numpy Array
- to train model on data (Keras) and evaluate model
- to write back ROOT ntuples with trained model is evaluated

## Setup and Installation
Log in to t3ui02.

Environment to have uproot available:
```
source /work/mratti/bootAnaconda_fromMauro.sh
```
To run a jupyter notebook:
```
jupyter notebook --port 8883 --no-browser 
```
To display the notebook on your lapton browser
```
ssh -N -f -L localhost:8883:localhost:8883 t3ui02.psi.ch
http://localhost:8883/tree
```



Installation:
```
git clone git@github.com:MT2Analysis/MT2MLO.git 
git checkout -b <own-branch>
```
Development done in own branch, then PR to master for review and merging:
```
git add bla.py
git commit -m "reasonable comment"
git push origin <own-branch>
```



## Example
```
cd rootToNumpy
python convertRootToNumpy.py
```

```
cd ../models
python example.py
```
