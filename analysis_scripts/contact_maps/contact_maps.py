import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import numpy as np
import os
import sys
from tqdm import tqdm

# Ensure output directory exists
os.makedirs('./Contact_Matrices', exist_ok=True)
prefix = sys.argv[1]

#------------------------------------------------------------------------------------#
# Residue-wise Symmetric Contact Frequency Matrix
#------------------------------------------------------------------------------------#

# Load the system
u = mda.Universe(f'{prefix}.prmtop', f'{prefix}eq.xtc')

# Select protein residues (excluding hydrogens)
group1 = u.select_atoms('(protein or nucleic) and not name H').residues
group2 = group1  # same group for symmetry

n1 = len(group1)
contact_counts = np.zeros((n1, n1), dtype=int)
n_frames = 0

# Estimate total frames
stride = 10
total_frames = len(u.trajectory[::stride])

# Progress bar loop
for ts in tqdm(u.trajectory[::stride], desc="Processing frames", total=total_frames):
    n_frames += 1
    for idx1, res1 in enumerate(group1):
        for idx2 in range(idx1, n1):  # only upper triangle, including diagonal
            res2 = group2[idx2]
            d = contacts.distance_array(res1.atoms.positions, res2.atoms.positions).min()
            if d < 4.5:
                contact_counts[idx1, idx2] += 1
                if idx1 != idx2:  # avoid double-counting the diagonal
                    contact_counts[idx2, idx1] += 1  # mirror to lower triangle

# Convert counts to percent contact frequency
contact_percent = contact_counts / n_frames

# Save as 2D matrix (percent contacts)
outfile = f'./Contact_Matrices/{prefix}_contmap.dat'
np.savetxt(outfile, contact_percent, fmt='%.2f')
print(f'Residue contact matrix for trajectory saved to {outfile}')

