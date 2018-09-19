from smr import File
import numpy as np
from matplotlib import pyplot as plt
from kaveh.plots import axvlines
from kaveh.sorting.spikesorter import SimpleSpikeSorter
from joblib import Parallel, delayed
import multiprocessing

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle
    
import fnmatch
import os


def processInputFile(arg):
    input_fn, output_fn = arg
    smr_content = File(input_fn)
    smr_content.read_channels()
    voltage_chan = smr_content.get_channel(0)

    sss = SimpleSpikeSorter(voltage_chan.data, voltage_chan.dt)
    sss.freq_range = (0, 5000)
    sss.cs_cov_type = 'tied'
    sss.cs_num_gmm_components = 4
    sss.run()
    with open(output_fn, 'wb') as output:
	print('writing {} ...'.format(output_fn))
	pickle.dump(smr_content, output, pickle.HIGHEST_PROTOCOL)
	


source_path = '../data/raw_data/'
#source_path = '/mnt/papers/Herzfeld_Nat_Neurosci_2018/raw_data/2006/Oscar/O89/'
target_path = '../data/auto_processed/'
#target_path = '/mnt/data/temp/kaveh/'

process_inputs = []

print('Recursive dir search on {}'.format(source_path))
for root, dirnames, filenames in os.walk(source_path):
    for filename in filenames:
        if filename.endswith('smr'):
            path_to_mkdir = os.path.join(target_path, os.path.relpath(root, source_path))
            if not os.path.exists(path_to_mkdir):
                os.makedirs(path_to_mkdir)
            print('Found smr file: '.format(os.path.join(root, filename)))
	    input_filename = os.path.join(root, filename)
            output_filename = os.path.join(path_to_mkdir, filename + '.pkl')
	    process_inputs = process_inputs + [(input_filename, output_filename)]

num_cores = multiprocessing.cpu_count()
print('Number of cores to be used = {}'.format(num_cores))     
Parallel(n_jobs=18, verbose=1)(map(delayed(processInputFile), process_inputs))