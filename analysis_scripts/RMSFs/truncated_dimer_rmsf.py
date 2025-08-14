import sys
import os
import subprocess
import numpy as np
os.makedirs("RMSF", exist_ok=True)
# Get the input files
prefix = sys.argv[1]

#Subunit 1
for i in np.arange(1,6):
    rmsf = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc 2001 50000 1
    rms first :7-45@CA
    atomicfluct :1-59&!@H= byres out ./RMSF/{prefix}{i}_sub1rmsf.dat 
    go
    quit
    """
 
# Save the content to "sectstruc.in"
    file_path = "rmsd.in"
    with open(file_path, "w") as file:
        file.write(rmsf)
 
    command = "cpptraj -i rmsd.in"
    subprocess.run(command, shell=True, check=True)
    print("Cpptraj script executed, removing script...")
    remove = "rm rmsd.in"
    subprocess.run(remove, shell=True, check=True)


#Subunit 2
for i in np.arange(1,6):
    rmsf = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc 2001 50000 1
    rms first :66-104@CA
    atomicfluct :60-118&!@H= byres out ./RMSF/{prefix}{i}_sub2rmsf.dat 
    go
    quit
    """
 
# Save the content to "sectstruc.in"
    file_path = "rmsd.in"
    with open(file_path, "w") as file:
        file.write(rmsf)
 
    command = "cpptraj -i rmsd.in"
    subprocess.run(command, shell=True, check=True)
    print("Cpptraj script executed, removing script...")
    remove = "rm rmsd.in"
    subprocess.run(remove, shell=True, check=True)

os.chdir('./RMSF')
avg = f"""readdata {prefix}1_sub1rmsf.dat
readdata {prefix}2_sub1rmsf.dat
readdata {prefix}3_sub1rmsf.dat
readdata {prefix}4_sub1rmsf.dat
readdata {prefix}5_sub1rmsf.dat
avg {prefix}1_sub1rmsf.dat:2 {prefix}2_sub1rmsf.dat:2 {prefix}3_sub1rmsf.dat:2 {prefix}4_sub1rmsf.dat:2 {prefix}5_sub1rmsf.dat:2 oversets out {prefix}_sub1rmsfavg.dat
go
quit
"""
 
# Save the content to "sectstruc.in"
file_path = "rmsd.in"
with open(file_path, "w") as file:
    file.write(avg)
 
print(f"Cpptraj script saved as {file_path}")
print("Running script.")
 
command = "cpptraj -i rmsd.in"
subprocess.run(command, shell=True, check=True)
print("Cpptraj script executed, removing script...")
remove = "rm rmsd.in"
subprocess.run(remove, shell=True, check=True)
print("Cpptraj script removed.")





avg = f"""readdata {prefix}1_sub2rmsf.dat
readdata {prefix}2_sub2rmsf.dat
readdata {prefix}3_sub2rmsf.dat
readdata {prefix}4_sub2rmsf.dat
readdata {prefix}5_sub2rmsf.dat
avg {prefix}1_sub2rmsf.dat:2 {prefix}2_sub2rmsf.dat:2 {prefix}3_sub2rmsf.dat:2 {prefix}4_sub2rmsf.dat:2 {prefix}5_sub2rmsf.dat:2 oversets out {prefix}_sub2rmsfavg.dat
go
quit
"""
 
# Save the content to "sectstruc.in"
file_path = "rmsd.in"
with open(file_path, "w") as file:
    file.write(avg)
 
print(f"Cpptraj script saved as {file_path}")
print("Running script.")
 
command = "cpptraj -i rmsd.in"
subprocess.run(command, shell=True, check=True)
print("Cpptraj script executed, removing script...")
remove = "rm rmsd.in"
subprocess.run(remove, shell=True, check=True)
print("Cpptraj script removed.")
