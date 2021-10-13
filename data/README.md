# DATA 
This directory contains the simulation data and results used in my prelim
document. 

### TRISO Homogenization
`/triso_homogenization` contains 2 FHR slab OpenMC simulations with and without 
TRISO homogenization. Results are in Table 5.1 of my prelim. 

`/triso_homogenization/fhr_plank_as_is`: homogenized

`/triso_homogenization/fhr_plank_as_is_5_layers`: no homogenization

### Hyperparameter Search 
`./hyperparameter_search` contains the input, results, and analysis files used 
in Section 5.1.2 of my prelim. 

### Multiphysics Preliminary Work 
`./multiphysics_preliminary` contains the inputs and results for Section 5.2
of my prelim. 

`./multiphysics_preliminary/plank_10_slice`: No spatial and energy homogenization

`./multiphysics_preliminary/plank_10_slice_mg`: Homogenized and using group 
constants generated in `/plank_10_slice`