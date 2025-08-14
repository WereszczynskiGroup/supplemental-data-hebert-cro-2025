# Analysis Scripts

Contains all post-simulation analysis scripts.

Tools needed to run these analyses:
- AmberTools20 or later
- Amber20 or later for MM/GBSA
- Python 3 
    - MDAnalysis
    - Numpy
    
Scripts for dCNA analysis are not included; source code may be found in The Hamelberg Group's GitHub page: https://github.com/The-Hamelberg-Group/dcna

Prior to analyses, Zenodo trajectories should have post-equilibration frames combined from all runs into one trajectory. Scripts have been written such that they should be named similarly to the trajectories they're composed of. For instance, if combining all Act3 monomer Cro trajectories, the most frictionless name to pick will be "A3_Monomereq.xtc".
