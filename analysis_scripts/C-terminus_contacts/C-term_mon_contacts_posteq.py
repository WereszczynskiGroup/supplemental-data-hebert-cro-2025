import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import numpy as np
import sys
import os
from tqdm import tqdm  # <- FIXED: Proper import

outdir = 'C-terminus_contacts_posteq'
os.makedirs(outdir, exist_ok=True)  # <- FIXED: was `os.mkdirs`, which is invalid

prefix = sys.argv[1]

#------------------------------------------------------------------------------------#
# Contact Analysis DNA-base pairs and protein
#------------------------------------------------------------------------------------#
# Load the topology and trajectory
u = mda.Universe(f'{prefix}.prmtop', f'{prefix}eq.xtc')
residues_1 = u.select_atoms('resid 60-66 and not (name H*)')
residues_2 = u.select_atoms('resid 1-50 and not (name H*)')

# Loop over the frames
def contacts_within_cutoff(u, group_a, group_b, radius=4.5):
    timeseries = []
    trajectory = u.trajectory[::10]
    for ts in tqdm(trajectory, desc="Calculating contacts"):
        dist = contacts.distance_array(group_a.positions, group_b.positions)
        n_contacts = contacts.contact_matrix(dist, radius).sum()
        timeseries.append([ts.frame, n_contacts])
    return np.array(timeseries)

# Run analysis and save
conts = contacts_within_cutoff(u, residues_1, residues_2, radius=4.5)
np.savetxt(f'{outdir}/{prefix}_c_contacts.dat', conts, fmt='%d %d', header='Frame Contacts')

