import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import numpy as np
import sys
import os
from tqdm import tqdm  # <- FIXED: Proper import

outdir = 'C-terminus_contacts'
os.makedirs(outdir, exist_ok=True)  # <- FIXED: was `os.mkdirs`, which is invalid

prefix = sys.argv[1]

#------------------------------------------------------------------------------------#
# Contact Analysis DNA-base pairs and protein
#------------------------------------------------------------------------------------#

for i in np.arange(1,6,1):
    # Load the topology and trajectory
    u = mda.Universe(f'{prefix}.prmtop', f'{prefix}{i}.xtc')
    residues_1 = u.select_atoms('resid 124-130 and not (name H*)')
    residues_2 = u.select_atoms('resid 190-196 and not (name H*)')
    residues_3 = u.select_atoms('(resid 1-114 or resid 131-180) and not (name H*)')

    # Loop over the frames
    def contacts_within_cutoff(u, group_a, group_b, group_c, radius=4.5):
        timeseries = []
        trajectory = u.trajectory[::1]
        for ts in tqdm(trajectory, desc="Calculating contacts"):
            dist1 = contacts.distance_array(group_a.positions, group_c.positions)
            dist2 = contacts.distance_array(group_b.positions, group_c.positions)
            n1_contacts = contacts.contact_matrix(dist1, radius).sum()
            n2_contacts = contacts.contact_matrix(dist2, radius).sum()
            timeseries.append([ts.frame, n1_contacts, n2_contacts])
        return np.array(timeseries)

    # Run analysis and save
    conts1 = contacts_within_cutoff(u, residues_1, residues_2, residues_3, radius=4.5)
    np.savetxt(f'{outdir}/{prefix}{i}_c_contacts.dat', conts1, fmt='%d %d %d', header='Frame Contacts1 Contacts2')

