# MT2MLO
Package to optimize MT2 Analysis with ML-based methods

Will contains several tools:
- to convert ROOT ntuples into Numpy Array
- to train model on data (Keras) and evaluate model
- to write back ROOT ntuples with trained model is evaluated

## Setup and Installation
Log in to t3ui02 -> this enables access to  MT2 ntuples in /scratch
As soon as you want to submit a job to GPU via slurm, you will need to login into t3ui04 and find a solution to get ntuples accessible

Environment (enables uproot):
```
source /work/mratti/bootAnaconda_fromMauro.sh
```
To activate tensorflow environment on CPU or GPU:
```
conda env list
source activate tensorflow
source activate tensorflow_gpu
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
