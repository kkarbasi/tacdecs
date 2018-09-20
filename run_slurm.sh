#!/bin/sh

#SBATCH
#SBATCH --job-name=KavehJob
#SBATCH --time=10:0:0
#SBATCH --partition=lrgmem
#SBATCH --mem=1000G
#SBATCH --nodes=1

module reset
module load python/2.7
pip install --user --no-cache-dir -r requirements.txt
pip uninstall -y  subprocess32
pip install --user --no-cache-dir -U subprocess32

python run_parallel.py > outlog
