from smr import File
import numpy as np
from matplotlib import pyplot as plt
from kaveh.plots import axvlines
from kaveh.sorting.spikesorter import SimpleSpikeSorter

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle
    
import fnmatch
import os


# source_path = '../data/raw_data/'
source_path = '/mnt/papers/Herzfeld_Nat_Neurosci_2018/raw_data/2006/Oscar/O89/'
# target_path = '../data/auto_processed/'
target_path = '/mnt/data/temp/kaveh/'

print('Recursive dir search on {}'.format(source_path))
found_source = 0
for root, dirnames, filenames in os.walk(source_path):
    found_source = 1
    for filename in filenames:
        if filename.endswith('smr'):
            path_to_mkdir = os.path.join(target_path, os.path.relpath(root, source_path))
            if not os.path.exists(path_to_mkdir):
                os.makedirs(path_to_mkdir)
            print('reading {} ...'.format(os.path.join(root, filename)))
            smr_content = File(os.path.join(root, filename))
            smr_content.read_channels()
            voltage_chan = smr_content.get_channel(0)

#             idx_0 = int(np.round(t_0 / voltage_chan.dt))
#             idx_end = int(np.round(t_end / voltage_chan.dt))
#             prange = slice(idx_0, idx_end)

            sss = SimpleSpikeSorter(voltage_chan.data, voltage_chan.dt)
            sss.freq_range = (0, 5000)
            sss.cs_cov_type = 'tied'
            sss.cs_num_gmm_components = 4
            sss.run()

            output_filename = os.path.join(path_to_mkdir, filename + '.pkl')
            with open(output_filename, 'wb') as output:
                print('writing {} ...'.format(output_filename))
                pickle.dump(smr_content, output, pickle.HIGHEST_PROTOCOL)

if found_source == 0:
    print('Path {} not found'.format(source_path))
print('End of script')

