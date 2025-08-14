# Input Files

This directory contains files and scripts used to generate the molecular system and prepare it for simulation.

Common contents:
- Initial PDB files
- Topology and coordinate files (e.g., `.prmtop`, `.inpcrd`, `.psf`, `.gro`)
- Parameter or force field modifications (`.frcmod`, `.lib`, `.itp`)
- System-building scripts (e.g., `tleap.in`, `parmed.in`, `gmx pdb2gmx`)
- Solvation and ionization commands
- Any notes on missing residues, mutations, or modeling steps

**Simulation engine neutrality:**  
While most systems in this lab are prepared using AMBER tools (e.g., `tleap`), this directory structure is designed to support setup workflows for other MD engines as well.

Please document:
- The intended simulation platform (Amber, NAMD, GROMACS, etc.)
- Force field(s) used (e.g., ff14SB, CHARMM36, GAFF2)
- Specific preparation steps (e.g., protonation states, box dimensions, ion concentrations)

If a single command/script was used to build the system, place it here (e.g., `tleap.in`, `gmx_setup.sh`).
