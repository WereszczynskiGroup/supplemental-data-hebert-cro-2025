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
residues_2 = u.select_atoms('resid 126-132 and not (name H*)')
residues_3 = u.select_atoms('(resid 1-50) and not (name H*)')
residues_4 = u.select_atoms('(resid 67-116) and not (name H*)')

# Loop over the frames
def contacts_within_cutoff(u, group_a, group_b, group_c, group_d, radius=4.5):
    timeseries = []
    trajectory = u.trajectory[::10]
    for ts in tqdm(trajectory, desc="Calculating contacts"):
        dist1 = contacts.distance_array(group_a.positions, group_c.positions)
        dist2 = contacts.distance_array(group_a.positions, group_d.positions)
        dist3 = contacts.distance_array(group_b.positions, group_c.positions)
        dist4 = contacts.distance_array(group_b.positions, group_d.positions)
        n1_contacts = contacts.contact_matrix(dist1, radius).sum()
        n2_contacts = contacts.contact_matrix(dist2, radius).sum()
        n3_contacts = contacts.contact_matrix(dist3, radius).sum()
        n4_contacts = contacts.contact_matrix(dist4, radius).sum()
        timeseries.append([ts.frame, n1_contacts, n2_contacts, n3_contacts, n4_contacts])
    return np.array(timeseries)

# Run analysis and save
conts1 = contacts_within_cutoff(u, residues_1, residues_2, residues_3, residues_4, radius=4.5)
np.savetxt(f'{outdir}/{prefix}_c_contacts.dat', conts1, fmt='%d %d %d %d %d', header='#Frame C1_sub1 C1_sub2 C2_sub1 C2_sub2')

