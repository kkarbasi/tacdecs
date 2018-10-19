#!/bin/sh

#SBATCH
#SBATCH --job-name=KavehJob2
#SBATCH --time=24:0:0
#SBATCH --partition=parallel
#SBATCH --mem=110G
##SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --cpus-per-task=1

module reset
module load python/2.7
python -m pip install --user --no-cache-dir -r requirements.txt 
#python -m pip uninstall -y  subprocess32
#python -m pip install --user --no-cache-dir -U subprocess32

python run_parallel.py
