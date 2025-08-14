# Input Files

This directory contains solvated topology and restart files from after the relaxation steps, representing the starting conformations for each system's production run. 

These files were used for Amber24 simulations. Each system was run with the ff19SB protein force field, OPC water, and Li-Merz ions for OPC water. Systems with DNA additionally used the BSC1 force field. 

All systems are neutralized and have extra Na+ and Cl- ions added to create a concentration of 150mM NaCl.

Monomer and dimer systems were solvated in 10 Angstrom water boxes. Systems with DNA were solvated with 12 Angstrom buffers from the DNA ends along the DNA helical axis and 20 Angstrom buffers perpendicular to the axis.

Variants of Cro were created using Dunbrack 2010 rotamer library in UCSF Chimera for mutations and deleting residues 60-66 prior to running tleap for truncations.
