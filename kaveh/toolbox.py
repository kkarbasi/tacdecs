from scipy.signal import resample
import numpy as np

def resample_to_freq(data, source_frequency, target_frequency):
    """
    resamples the input data from source_frequency to target_frequency
    """
    resample_ratio = float(target_frequency) / source_frequency
    if resample_ratio == 1:
        return data
    else:
        target_n_samples = int(np.size(data) * resample_ratio)
        resampled_data = resample(data, target_n_samples)
        return resampled_data


def closest_argmin(A, B):
    """
    Finds the indices of the nearest value in B to values in A
    Output is the same size as A
    Source: https://stackoverflow.com/a/45350318
    """
    L = B.size
    sidx_B = B.argsort()
    sorted_B = B[sidx_B]
    sorted_idx = np.searchsorted(sorted_B, A)
    sorted_idx[sorted_idx==L] = L-1
    mask = (sorted_idx > 0) & \
    ((np.abs(A - sorted_B[sorted_idx-1]) < np.abs(A - sorted_B[sorted_idx])) )
    return sidx_B[sorted_idx-mask]
