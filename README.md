# Physical network robustness
[In progress] In this project, we are simulating 2D and 3D graphs of physical attacks (spatial edge removal) in their embedding space Specifically, we are focused on random and targeted attacks to identify how robust the networks are. 
To perform targeted attacks in space, we are developing a spatial measure of connectivity, that can be applied to both 2D and 3D datasets. Below are the grid models we are currently working with where we develop such measure:



# Technical project overview
First, I  accessed and downloaded the neuron skeleton data, which was further processed to obtain a dataset composed only of points (point clouds) -  **1. obtain_neuron_skeletons.ipynb**.

# Data
To access the original data, you will need to use the Python library provided by the Janelia project, which you can install from https://pypi.org/project/neuprint-python/

If you want to understand this library more, you can read through their documentation https://connectome-neuprint.github.io/neuprint-python/docs/index.html

