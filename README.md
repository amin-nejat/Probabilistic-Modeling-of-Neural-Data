# Installation Instructions for the Workshop on Probabilistic Modeling of Neural Data

1. Download and install [**anaconda**](https://docs.anaconda.com/anaconda/install/index.html)

2. Create a **virtual environment** using anaconda and activate it
```
conda create -n pyro
conda activate pyro
```
	- This helps with avoiding package conflicts

3. Install [**pytorch**](https://pytorch.org/get-started/locally/) with conda

	- Make sure that the pytorch version is compatible with your device)
	- If you have GPUs available on your device, use the right cuda version, check your cuda version using 
	```
	nvcc --version
	```

4. Install [**pyro**](https://anaconda.org/conda-forge/pyro-ppl) with conda

5. Run **jypter lab** in conda and execute notebooks
```
jupyter lab
```