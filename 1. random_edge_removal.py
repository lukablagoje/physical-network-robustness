# Import necessary libraries
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import networkx as nx

# List of names for different biological networks to be analyzed
name_list = ['human_neuron', 'vascular_2', 'fruit_fly_2', 'rat_neuron', 'vascular_3', 
             'vascular_1', 'mitochondrial', 'anthill', 'root_1', 'root_2', 
             'monkey_neuron', 'zebrafish_neuron', 'fruit_fly_3', 'fruit_fly_1', 'fruit_fly_4']

# Dictionary to store final results for each network
final_results = {}

# Number of trials for edge removal
n_trials = 100

# Main loop over each biological network
for name_index, name in enumerate(name_list):
    final_results[name] = {}
    path = '../../link_confinement/1. data/3. final_data/'
    
    # Load network paths from CSV
    skeleton_paths = pd.read_csv(path + name + '.paths.csv', index_col=[0])
    connectome = skeleton_paths[['path_id', 'bodyId_pre', 'bodyId_post']].drop_duplicates()
    
    # Initialize Graph
    G = nx.Graph()
    G.add_edges_from(connectome[['bodyId_pre', 'bodyId_post']].values)
    
    # Initial sizes and conditions
    initial_component_size = len(max(nx.connected_components(G), key=len))
    initial_number_of_edges = len(G.edges())
    
    first_component_size = {}
    second_component_size = {}
    
    # Trials for removing edges randomly
    for trial in range(n_trials):
        # Re-initialize graph for each trial
        G = nx.Graph()
        G.add_edges_from(connectome[['bodyId_pre', 'bodyId_post']].values)
        
        first_component_size[trial] = {}
        second_component_size[trial] = {}
        
        # Shuffle edges for random removal
        random_edges_list = connectome[['bodyId_pre', 'bodyId_post']].sample(frac=1, random_state=(trial+1) + 1000*(name_index+1)).values
        
        # Remove edges one by one and calculate component sizes
        for edge_index, edge in enumerate(random_edges_list):
            G.remove_edge(edge[0], edge[1])
            component_lengths = sorted([len(c) for c in nx.connected_components(G)], reverse=True)
            
            if len(component_lengths) >= 1:
                first_component_size[trial][edge_index] = component_lengths[0] / initial_component_size
                second_component_size[trial][edge_index] = component_lengths[1] / initial_component_size if len(component_lengths) > 1 else 0
                
    # Analysis of component size changes after edge removals
    second_occurrence_proportion_list = []
    first_comp_list = []
    second_comp_list = []
    
    for trial in range(n_trials):
        first_component_list = list(first_component_size[trial].values())
        second_component_list = list(second_component_size[trial].values())
        maximum_index = max(range(len(second_component_list)), key=lambda i: second_component_list[i])
        maximum_proportion = maximum_index / len(second_component_list)
        
        second_occurrence_proportion_list.append(maximum_proportion)
        first_comp_list.append(first_component_list[maximum_index])
        second_comp_list.append(second_component_list[maximum_index])
    
    # Calculate and store statistical measures for the analysis
    final_results[name]['first_component_change_trial_edge_index'] = first_component_size
    final_results[name]['second_component_change_trial_edge_index'] = second_component_size
    final_results[name]['breakdown_point_mean_random_edge_proportion_removed'] = np.round(np.mean(second_occurrence_proportion_list), 3)
    final_results[name]['breakdown_point_std_random_edge_proportion_removed'] = np.round(np.std(second_occurrence_proportion_list), 3)
    final_results[name]['mean_first_component_size'] = np.round(np.mean(first_comp_list), 3)
    final_results[name]['std_first_component_size'] = np.round(np.std(first_comp_list), 3)
    final_results[name]['mean_second_component_size'] = np.round(np.mean(second_comp_list), 3)
    final_results[name]['std_second_component_size'] = np.round(np.std(second_comp_list), 3)
    
    # Save the results for each network to a pickle file
    with open("1. random_edge_removal_results/" + name + "_r_edge_removal_results.pkl", "wb") as h:
        pickle.dump(final_results[name], h)
