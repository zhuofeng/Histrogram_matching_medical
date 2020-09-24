import numpy as np
import os

# histogram matching
def histeq(data):
    # data: np array, the CT data to be normalized
    nbr_bins = np.max(data) - np.min(data) + 1
    nbr_bins = int(nbr_bins)
    
    datahist, bins = np.histogram(data.flatten(), nbr_bins, normed=True)
    cdf = datahist.cumsum()
    cdf = (np.max(data) - np.min(data)) * cdf / cdf[-1]

    data2 = np.interp(data.flatten(), bins[:-1], cdf)
    data2 = np.ceil(data2)

    return data2.reshape(data.shape), cdf