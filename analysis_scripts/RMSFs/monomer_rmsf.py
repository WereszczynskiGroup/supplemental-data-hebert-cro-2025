import sys
import os
import subprocess
import numpy as np
os.makedirs('RMSF', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    h3rmsf = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc 2001 last 10
    rms Run1 :7-45@CA first		
    atomicfluct :*&!@H= byres out ./RMSF/{prefix}{i}_fluct.dat
    go
    clear all
    go
    quit
    """


    file_path = "h3rmsf.in"
    with open(file_path, "w") as file:
        file.write(h3rmsf)


    command = "cpptraj -i h3rmsf.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm h3rmsf.in"
    subprocess.run(remove, shell=True, check=True)

os.chdir('./RMSF')
average = f"""readdata {prefix}1_fluct.dat
readdata {prefix}2_fluct.dat
readdata {prefix}3_fluct.dat
readdata {prefix}4_fluct.dat
readdata {prefix}5_fluct.dat
avg {prefix}1_fluct.dat:2 {prefix}2_fluct.dat:2 {prefix}3_fluct.dat:2 {prefix}4_fluct.dat:2 {prefix}5_fluct.dat:2 oversets out {prefix}_allfluct.dat
go
quit
"""


file_path = "average.in"
with open(file_path, "w") as file:
    file.write(average)


command = "cpptraj -i average.in"
subprocess.run(command, shell=True, check=True)
remove = "rm average.in"
subprocess.run(remove, shell=True, check=True)
