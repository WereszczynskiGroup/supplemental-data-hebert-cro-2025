import sys
import subprocess
import os
import numpy as np

prefix = sys.argv[1]
os.chdir(f'{prefix}')
for i in np.arange(1,6,1):

    command1 = f"mv ./Run{i}/gbsa.dat ./Run{i}/{prefix}gbsa{i}.dat"
    command2 = f"mv ./Run{i}/gbsa.xvg ./Run{i}/{prefix}gbsa{i}.xvg"
    command3 = f"mv ./Run{i}/gbsa.txt ./Run{i}/{prefix}gbsa{i}.txt"
    subprocess.run(command1, shell=True, check=True)
    subprocess.run(command2, shell=True, check=True)
    subprocess.run(command3, shell=True, check=True)
