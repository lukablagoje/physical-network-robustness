# Physical network robustness [In progress] 
In this project, we are simulating 2D and 3D graphs of physical attacks (spatial edge removal) in their embedding space Specifically, we are focused on random and targeted attacks to identify how robust the networks are. 
To perform targeted attacks in space, we are developing a spatial measure of connectivity, that can be applied to both 2D and 3D datasets. Below are the random graph (Erdos-Renyi) grid models we are currently working with where we develop such measures, for different rewiring probabilities $p$:

![original_tile_removal_animation](https://github.com/user-attachments/assets/644d12bd-d9a5-4b28-a4b0-b697c5af132f)

![fruit_fly_4_original_tile_removal_animation (1)](https://github.com/user-attachments/assets/b0d94636-cc8c-441a-893a-11ea962b50a3)

# Technical project overview
[1. random_edge_removal.py](https://github.com/lukablagoje/physical-network-robustness/blob/main/1.%20random_edge_removal.py) - Removing random edges from the graph to observe how quickly they fall apart.

[2D_grid_model.ipynb](https://github.com/lukablagoje/physical-network-robustness/blob/main/2D_grid_model.ipynb) - 2D grid models are created and the spatial connectivity of the grid that bins the space they are embedded in is calculated


