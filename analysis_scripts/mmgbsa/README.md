# MM/GBSA Input Files

To use, strip trajectories to post-equilibration time and every tenth frame. This will create trajectories where each frame corresponds to 1 nanosecond.

Each subfolder contains the complex, ligand, and receptor prmtop files, and the MM/GBSA input file decomp.in. Analysis of the results assumes each simulation run was done separately, i.e. run MMPBSA.py on WTdna1.xtc, WTdna2.xtc, etc. The order doesn't really matter as long as all 5 trajectories are sampled.
