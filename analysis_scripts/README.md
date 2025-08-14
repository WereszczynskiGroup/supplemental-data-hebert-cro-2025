# Analysis Scripts

Contains all post-simulation analysis scripts.

Common tools:
- cpptraj / pytraj
- Python (MDAnalysis, MDTraj, NumPy, Pandas)
- R (for stats or plotting)
- GROMACS tools (e.g., `gmx rms`, `gmx hbond`)

Include:
- Scripts to extract observables (e.g., RMSD, contacts, hydrogen bonds)
- Automation or plotting scripts for generating figures
- Documentation of required input arguments and software dependencies

If analysis is tightly coupled to simulation format, include clear instructions for conversion (e.g., from AMBER `nc` to MDTraj-readable format).
