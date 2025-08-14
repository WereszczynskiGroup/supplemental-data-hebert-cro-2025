import sys
import subprocess
import os
import numpy as np

# Before usage: Combine post-equilibration trajectory frames

os.makedirs('Mut_check', exist_ok=True)
prefix = sys.argv[1]
top_file = f'{prefix}.prmtop'
traj_file = f'{prefix}eq.xtc'
if prefix=='WTrdna' or prefix=='T3dna' or prefix=='T8dna':
    mutated_residues = [81, 85, 86, 90, 140, 144, 145, 149]

else:
    mutated_residues = [81, 85, 86, 90, 147, 151, 152, 156]


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
if prefix=='WTrdna' or prefix=='T3dna' or prefix=='T8dna':
    x,y1 = np.loadtxt(f'Mut_check/{prefix}sasa_81.dat', unpack=True, usecols=(0,1), comments='#')
    y2 = np.loadtxt(f'Mut_check/{prefix}sasa_85.dat', unpack=True, usecols=(1), comments='#')
    y3 = np.loadtxt(f'Mut_check/{prefix}sasa_86.dat', unpack=True, usecols=(1), comments='#')
    y4 = np.loadtxt(f'Mut_check/{prefix}sasa_90.dat', unpack=True, usecols=(1), comments='#')
    y5 = np.loadtxt(f'Mut_check/{prefix}sasa_140.dat', unpack=True, usecols=(1), comments='#')
    y6 = np.loadtxt(f'Mut_check/{prefix}sasa_144.dat', unpack=True, usecols=(1), comments='#')
    y7 = np.loadtxt(f'Mut_check/{prefix}sasa_145.dat', unpack=True, usecols=(1), comments='#')
    y8 = np.loadtxt(f'Mut_check/{prefix}sasa_149.dat', unpack=True, usecols=(1), comments='#')


    combined=np.column_stack((x,y1,y2,y3,y4,y5,y6,y7,y8))
    np.savetxt(f'Mut_check/{prefix}mutsasa.dat', combined, fmt="%.6f", delimiter=' ', header='Frame(ns) 17_1  21_1  22_1  26_1  17_2  21_2  22_2  26_2')
    remove = 'rm ./Mut_check/*sasa_*.dat'
    subprocess.run(remove, shell=True, check=True)

else:
    x,y1 = np.loadtxt(f'Mut_check/{prefix}sasa_81.dat', unpack=True, usecols=(0,1), comments='#')
    y2 = np.loadtxt(f'Mut_check/{prefix}sasa_85.dat', unpack=True, usecols=(1), comments='#')
    y3 = np.loadtxt(f'Mut_check/{prefix}sasa_86.dat', unpack=True, usecols=(1), comments='#')
    y4 = np.loadtxt(f'Mut_check/{prefix}sasa_90.dat', unpack=True, usecols=(1), comments='#')
    y5 = np.loadtxt(f'Mut_check/{prefix}sasa_147.dat', unpack=True, usecols=(1), comments='#')
    y6 = np.loadtxt(f'Mut_check/{prefix}sasa_151.dat', unpack=True, usecols=(1), comments='#')
    y7 = np.loadtxt(f'Mut_check/{prefix}sasa_152.dat', unpack=True, usecols=(1), comments='#')
    y8 = np.loadtxt(f'Mut_check/{prefix}sasa_156.dat', unpack=True, usecols=(1), comments='#')


    combined=np.column_stack((x,y1,y2,y3,y4,y5,y6,y7,y8))
    np.savetxt(f'Mut_check/{prefix}mutsasa.dat', combined, fmt="%.6f", delimiter=' ', header='Frame(ns) 17_1  21_1  22_1  26_1  17_2  21_2  22_2  26_2')
    remove = 'rm ./Mut_check/*sasa_*.dat'
    subprocess.run(remove, shell=True, check=True)
