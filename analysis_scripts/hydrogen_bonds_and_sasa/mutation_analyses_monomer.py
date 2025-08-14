import sys
import subprocess
import os
import numpy as np

# Before usage: Combine post-equilibration trajectory frames

os.makedirs('Mut_check', exist_ok=True)
prefix = sys.argv[1]
top_file = f'{prefix}.prmtop'
traj_file = f'{prefix}eq.xtc'
mutated_residues=[17,21,22,26]
# Generate the cpptraj script with dynamic names
sectstruc1 = f"""parm {top_file}
trajin {traj_file} 1 last 10
hbond :* avgout Mut_check/{prefix}hbond.dat
go
quit
"""
file_path = "rmsd.in"
with open(file_path, "w") as file:
    file.write(sectstruc1)
command = "cpptraj -i rmsd.in"
subprocess.run(command, shell=True, check=True)
remove = "rm rmsd.in"
subprocess.run(remove, shell=True, check=True)
print("Hbond analysis completed.")
###
# SASA
cpptraj_input = f"parm {top_file}\ntrajin {traj_file}\n"
for resid in mutated_residues:
    cpptraj_input += f"surf :{resid} out Mut_check/{prefix}sasa_{resid}.dat\n"
cpptraj_input += "run\n"

with open("sasa.in", "w") as f:
    f.write(cpptraj_input)

# Run cpptraj
subprocess.run(["cpptraj", "-i", "sasa.in"], check=True)

x,y1 = np.loadtxt(f'Mut_check/{prefix}sasa_17.dat', unpack=True, usecols=(0,1), comments='#')
y2 = np.loadtxt(f'Mut_check/{prefix}sasa_21.dat', unpack=True, usecols=(1), comments='#')
y3 = np.loadtxt(f'Mut_check/{prefix}sasa_22.dat', unpack=True, usecols=(1), comments='#')
y4 = np.loadtxt(f'Mut_check/{prefix}sasa_26.dat', unpack=True, usecols=(1), comments='#')

combined=np.column_stack((x,y1,y2,y3,y4))
np.savetxt(f'Mut_check/{prefix}mutsasa.dat', combined, fmt="%.6f", delimiter=' ', header='Frame(ns) 17  21  22  26')
remove = 'rm ./Mut_check/*sasa_*.dat'
subprocess.run(remove, shell=True, check=True)

