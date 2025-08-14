import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import numpy as np
import sys
import os

os.makedirs('Cro_dna_contact', exist_ok=True)

prefix = sys.argv[1]
output = f'./Cro_dna_contact/{prefix}_dnacont.dat'
# Load the topology and trajectory
u = mda.Universe(f'{prefix}.prmtop', f'{prefix}eq.xtc')

# Define the residue ranges
residues_1 = u.select_atoms('resid 1-64 and not name H*')
residues_2 = u.select_atoms('resid 65-196 and not name H*')
residues_3 = u.select_atoms('(resid 190-196 or resid 124-130) and not name H*')

def contacts_within_cutoff (u, group_a, group_b, group_c, radius=4.5):
    timeseries = []
    for ts in u.trajectory[0::10]:
        # Calculate distance matrix between the two groups
        dist = contacts.distance_array(group_a.positions, group_b.positions)
        dist2 = contacts.distance_array(group_a.positions, group_c.positions)

    # Count the number of contacts below the cutoff distance
        n_contacts = contacts.contact_matrix(dist, radius).sum()
        n2_contacts = contacts.contact_matrix(dist2, radius).sum()
        timeseries.append([ts.frame, n_contacts, n2_contacts])
    return np.array(timeseries)
# Save the contact time series to a .dat file

conts = contacts_within_cutoff(u, residues_1, residues_3, residues_2, radius=4.5)
np.savetxt(output, conts, fmt='%d %d %d', header='Frame C-Contacts All-Contacts')
